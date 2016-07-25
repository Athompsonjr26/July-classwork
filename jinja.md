# [Jinja Designer Docs](http://jinja.pocoo.org/docs/dev/templates/)

To render a variable or expression to the page, you surround it with double curly braces like so:

{{ project.name }}

## Control Structures

Control structures such as for loops and if statements are surround by curly-brace-percent-sign pairs: {% %}.

### For Loops

The following code uses a for loop to render a list of usernames as a ul:

<ul>
{% for user in users %}
  <li>{{ user.username }}</li>
{% endfor %}
</ul>

### If Statements

The following code uses an if statement to render a log out link if the user is logged in, or a login link and a signup link if he is not.

{% if logged_in %}
  <a href="/logout">Log out</a>
{% else %}
  <a href="/login">Log In</a> |
  <a href="/signup">Sign Up</a>
{% endif %}

## Template Inheritance

Jinja supports template inheritance - which is conceptually like object inheritance. Template inheritance is commonly used to reused a common layout throughout a site. You will have a base template that represents the common layout, and a child template that represents a specific page in the application. The base template will setup a number of "blocks" which the child template can override using the identical syntax. A block definition looks like this:

{% block BLOCK_NAME %}
BLOCK_CONTENT
{% endblock %}

The child template would then use the extend statement to extend the base template, thus inheriting everything that the base template has. The example below extends the base template called "layout.html"

{% extend "layout.html" %}

### Full Template Inheritance Example

layout.html:

<!DOCTYPE html>
<html lang="en">
<head>
  <title>{{title}}</title>
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>

projects.html

{% extend "layout.html" %}
{% block body %}
<h1>Project List</h1>
<ul>
  {% for project in projects %}
  <li>{{project.name}}</li>
  {% endfor %}
</ul>
{% endblock %}
