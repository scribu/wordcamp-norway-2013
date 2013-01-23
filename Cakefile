fs = require('fs')
watch = require('watch')
mustache = require('mustache')
marked = require('marked')
require('js-yaml')

marked.setOptions(
	gfm: true
	pedantic: false
	sanitize: false
)

prepare_slide = (slide) ->
	for own key, value of slide
		if typeof value is 'object'
			continue

		if key is 'class'
			continue

		if key is 'markdown'
			path = 'src/' + value
			try
				slide[key] = marked(fs.readFileSync path, 'utf8')
			catch err
				console.error path + " doesn't exist"

			continue

		if key is 'code'
			path = 'src/' + value
			try
				value = fs.readFileSync path, 'utf8'
			catch err
				console.error path + " doesn't exist"

		slide[key] = {}
		slide[key][key] = value

	null

task 'watch', 'Watch the /src/ folder for changes', (options) ->
	invoke 'build'

	watch.createMonitor 'src', (monitor) ->
		monitor.on "changed", (f, curr, prev) ->
			if f.match /^[^\.]+\.[^\.~]+$/
				console.log f + ' changed'
				invoke 'build'

task 'build', 'Generate the slides', (options) ->
	try
		slide_list = require('./src/slides.yml')
	catch err
		console.error err.stack
		return

	for slide in slide_list['slides']
		prepare_slide slide

	template = fs.readFileSync './src/template.html', 'utf8'

	output = mustache.render(template, slide_list)

	fs.writeFileSync 'index.html', output
