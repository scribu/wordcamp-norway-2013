## What is this?

This is the [html5slides][1] script embeded into a [Jekyll][2] site.

## Why do you need Jekyll?

Because I frequently need to embed code snippets. If I was using a plain HTML file, I would have to manually escape them.

With Jekyll, I can create a separate file in the `_includes` directory and escape it programatically.

Example:

```html
{% capture code %}{% include repl.txt %}{% endcapture raw %}

<pre>{{ code | escape }}</pre>
```

## Setup

Have [Jekyll][2] installed:

```bash
sudo gem install jekyll
```

## Build and view

```bash
jekyll --server --auto
```

[1]: https://code.google.com/p/html5slides/
[2]: http://jekyllrb.com
