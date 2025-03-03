---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---
# Welcome to My Blog

<nav>
  <ul>
    <li><a href="/sailing/">Sailing</a></li>
    <li><a href="/technology/">Technology</a></li>
  </ul>
</nav>

## Recent Posts

<ul>
  {% for post in site.posts limit:5 %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>