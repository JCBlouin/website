# www.jcblouin.com
## Infrastructure and deployment pipeline

### Goal:
Host a website which can be updated easily in low-connectivity situations.

Will be useful for sailing blog and international travel.

Minimum bandwith requirements. Git pushes and MRs trigger site test and build steps.


### Technologies:
- Jekyll
    - Builds static html website from markdown
- Pulumi
    - Defines and deploys cloud infrastructure
- GitLab Runners
    - Automates site updates and infrastructure changes

### TODO
- write pipeline config file
- create the jekyll site