---
layout: page
title: Sailing
permalink: /sailing/
---

{% include image name="kitten.png" caption="Awww a kitten." %}


<ul>
  {% for post in site.categories.sailing %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

