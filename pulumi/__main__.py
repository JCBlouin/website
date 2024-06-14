"""jcblouin.com website"""

import json
import mimetypes
import os

from pulumi import export, FileAsset
import pulumi
import pulumi_aws as aws



web_bucket = aws.s3.Bucket('www.jcblouin.com',
    bucket="www.jcblouin.com",
    website=aws.s3.BucketWebsiteArgs(
        index_document="index.html",
    ))

content_dir = "webroot"
for file in os.listdir(content_dir):
    filepath = os.path.join(content_dir, file)
    mime_type, _ = mimetypes.guess_type(filepath)
    obj = aws.s3.BucketObject(file,
        bucket=web_bucket.id,
        source=FileAsset(filepath),
        content_type=mime_type)

def public_read_policy_for_bucket(bucket_name):
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                f"arn:aws:s3:::{bucket_name}/*",
            ]
        }]
    })

bucket_name = web_bucket.id
bucket_policy = aws.s3.BucketPolicy("bucket-policy",
    bucket=bucket_name,
    policy=bucket_name.apply(public_read_policy_for_bucket))

# Route 53 for DNS

domain = aws.route53.Zone("jcblouindotcom",
    comment="HostedZone created by Route53 Registrar",
    name="jcblouin.com",
    opts=pulumi.ResourceOptions(protect=True))

www = aws.route53.Record("www",
    zone_id=domain.zone_id,
    name="www.jcblouin.com",
    type="A",
    aliases=[aws.route53.RecordAliasArgs(
        name="s3-website-us-east-1.amazonaws.com.",
        zone_id=web_bucket.hosted_zone_id,
        evaluate_target_health=False,
    )])

root = aws.route53.Record("root",
    zone_id=domain.zone_id,
    name=domain.name,
    type="A",
    aliases=[aws.route53.RecordAliasArgs(
        name=www.fqdn,
        zone_id=domain.zone_id,
        evaluate_target_health=False,
    )])

# ACM for SSL Certs

www_cert = aws.acm.Certificate("www_cert",
    domain_name=www.fqdn,
    validation_method="DNS")

www_cert_validation_record = aws.route53.Record("www_cert_validation_record",
    name=www_cert.domain_validation_options[0].resource_record_name,
    records=[www_cert.domain_validation_options[0].resource_record_value],
    ttl=60,
    type=www_cert.domain_validation_options[0].resource_record_type,
    zone_id=domain.zone_id
    )

www_certificate_validation_status = aws.acm.CertificateValidation("www_cert_validation_status",
    certificate_arn=www_cert.arn,
    )

root_cert = aws.acm.Certificate("root_cert",
    domain_name=root.fqdn,
    validation_method="DNS")

root_cert_validation_record = aws.route53.Record("root_cert_validation_record",
    name=root_cert.domain_validation_options[0].resource_record_name,
    records=[root_cert.domain_validation_options[0].resource_record_value],
    ttl=60,
    type=root_cert.domain_validation_options[0].resource_record_type,
    zone_id=domain.zone_id
    )

root_certificate_validation_status = aws.acm.CertificateValidation("root_cert_validation_status",
    certificate_arn=root_cert.arn,
    )

# Export the name of the bucket
export('bucket_name', web_bucket.id)
export('website_url', web_bucket.website_endpoint)
