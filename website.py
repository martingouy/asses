from bottle import run, template, static_file, view, Bottle, request
from sys import argv
import json
import fit
import codecs
import methods
import plot
import kcalc
import os
import export_xls

app = Bottle()

@app.route('/export')
@view('export')
def export():
    return { 'get_url':  app.get_url }

@app.route('/import')
@view('import')
def export():
    return { 'get_url':  app.get_url }

@app.route('/')
@app.route('/attributes')
@view('attributes')
def attributs():
    return { 'get_url':  app.get_url }

@app.route('/questions')
@view('questions')
def questions():
    return { 'get_url':  app.get_url }

@app.route('/k_calculus')
@view('k_calculus')
def k_calculus():
    return { 'get_url':  app.get_url }

@app.route('/ajax', method="POST")
def ajax():
    reader = codecs.getreader("utf-8")
    query = json.load(reader(request.body))
    
    if query['type'] == "question":
        if query['method']=='PE':
            return methods.PE(float(query['min_interval']),float(query['max_interval']),float(query['proba']), int(query['choice']), str(query['mode']))
        elif query['method']=='LE':
            return methods.LE(float(query['min_interval']),float(query['max_interval']),float(query['proba']), int(query['choice']), str(query['mode']))
        elif query['method']=='CE_Constant_Prob':
            return methods.CE(float(query['min_interval']),float(query['max_interval']),float(query['gain']), int(query['choice']), str(query['mode']))
        else:
            return query['method']
    elif query['type'] == "calc_util":
        return fit.regressions(query['points'])

    elif query['type'] == "k_calculus":
        print("on va calculer k_calculus sur le fichier kcalc")
        return {'k':kcalc.calculk(query['k1'],query['k2'],query['k3'])}

    elif query['type'] == "svg":
        dictionary = query['data']
        min = query['min']
        max = query['max']
        liste_cord = query['liste_cord']
        return plot.generate_svg_plot(dictionary, min, max, liste_cord)


    elif query['type'] == "export_xls":
        return export_xls.generate_fichier(query['data'])


#exporter le fichier
@app.route('/export_download/:path#.+#', name='export')
def export(path):
    val = static_file(path, root='export')
    os.remove(path)
    return val

@app.route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

#run(app, host='localhost', port=8080, debug=True)
app.run(host='0.0.0.0', port=argv[1])
