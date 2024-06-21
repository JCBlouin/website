---
layout: page
title: Technology
permalink: /technology/
---

# Technology Posts

<ul>
  {% for post in site.categories.technology %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
