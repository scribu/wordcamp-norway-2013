---
layout: default
title: Command Line Learnings For Make Benefit Glorious Nation of WordPress
---
<article>
<h1>Hello,</h1>

My name is Cristi Burcă.

The Internet calls me **scribu**.

I work on/with WordPress.
</article>

<article>
<h1>
	Command Line Learnings<br>
	For Make Benefit<br>
	Glorious Nation of WordPress
</h1>

<img id="boratpose" class="to-build centered vcentered" src="./assets/img/boratpose.jpg" />

<p>WordCamp Norway 2013</p>
</article>

<article>
<h1>Command Line Interface?</h1>

Haven't those gone extinct since the 90's?!
</article>

<article>
<h1>What is WP-CLI?</h1>

<ul class="build">
	<li>a command line interface for WordPress
	<li>written in PHP
	<li>free and open source
	<li>available on <a href="http://wp-cli.org">wp-cli.org</a>
</ul>
</article>

<article>
<h1>What is WP-CLI good for?</h1>
</article>

<article>
<h2>Automation</h2>

<div class="to-build">

<p>Task: Set up a cron script that periodically updates everything.</p>

<pre>
{% include update.sh %}
</pre>

</div>
</article>

<article>
<h2>Integration</h2>

<div class="to-build">

<p>Task: Access data in a WP install from a Python script.</p>

<pre>
{% include wp.py %}
</pre>

</div>

</article>

<article>
<h2>Long running jobs</h2>

Task: Regenerate all thumbnails on a site.

<div class="in-the-middle to-build">
	<h3>GUI:</h3>

	<ul>
		<li>send AJAX request for each image
		<li>405 LOC
	</ul>
</div>

<div class="in-the-middle to-build">
	<h3>CLI:</h3>

	<ul>
		<li>simple <code>foreach</code> loop
		<li>117 LOC
	</ul>
</div>
</article>

<article>
<h2>Interactive debugging</h2>

<div class="to-build">
	<p>Task: Fool around.</p>

{% capture raw %}{% include repl.txt %}{% endcapture raw %}

<pre>{{ raw | escape }}</pre>

</div>

<p id="boratgreat" class="blue to-build"><strong>Great success!</strong></p>
</article>

<article>
<h2>Code generation</h2>

Task: Create a plugin that registers a custom post type and a taxonomy.

<pre>
{% include scaffold.sh %}
</pre>

</article>

<article>
<h2>What about X?</h2>

WP-CLI is extensible; it will look for commands defined inside WordPress plugins or themes.

All you have to do is make sure WP-CLI is running:

```
if ( defined( 'WP_CLI' ) && WP_CLI ) {
	require __DIR__ . '/my-cli-command.php';
}
```

More info:

[github.com/wp-cli/wp-cli/wiki/Creating-Commands](https://github.com/wp-cli/wp-cli/wiki/Creating-Commands)
</article>

<article>
<h2>How did WP-CLI get started?</h2>

* Andreas Creten started it in early September, 2011.
* I started contributing to it in late September, 2011.
* Front page of Hacker News in October, 2011.
* New contributors, additional features, talks at WordCamps etc.
</article>

<article>
<q>If you can not able do it from command line, is not worth do it.</q>
<div class="author">DevOps Borat</div>
</article>

<article>
<h2>Thanks!</h2>

* Site: [scribu.net](http://scribu.net)
* Twitter: [@scribu](http://twitter.com/scribu)
* Github: [@scribu](http://github.com/scribu)
</article>
