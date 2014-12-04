from bottle import run, template, static_file, view, Bottle

app = Bottle()

@app.route('/')
@app.route('/hello/<name>')
@view('blank-page')
def greet(name='Stranger'):
	return { 'get_url':  app.get_url } 

@app.route('/export')
@view('export')
def export():
	return { 'get_url':  app.get_url } 

@app.route('/import')
@view('import')
def export():
	return { 'get_url':  app.get_url } 

@app.route('/attributes')
@view('attributes')
def attributs():
	return { 'get_url':  app.get_url } 

@app.route('/static/:path#.+#', name='static')
def static(path):
	return static_file(path, root='static')

run(app, host='localhost', port=8080, debug=True)
