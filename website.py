from bottle import run, template, static_file, view, Bottle, request
from sys import argv
import json
import fit
import codecs
import methods
import plot
import kcalc
import kcal44
import kcalc55
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
        if query['number'] == 3:
            return {'k':kcalc.calculk(query['k']['k1'],query['k']['k2'],query['k']['k3'])}
        elif query['number'] == 4:
            return {'k':kcalc.calculk4(query['k']['k1'],query['k']['k2'],query['k']['k3'],query['k']['k4'])}
        elif query['number'] == 5:
            return {'k':kcalc.calculk4(query['k']['k1'],query['k']['k2'],query['k']['k3'],query['k']['k4'], query['k']['k5'])}

    elif query['type'] == "svg":
        dictionary = query['data']
        min = query['min']
        max = query['max']
        liste_cord = query['liste_cord']
        width=query['width']
        return plot.generate_svg_plot(dictionary, min, max, liste_cord, width)


    elif query['type'] == "export_xls":
        return export_xls.generate_fichier(query['data'])


#exporter le fichier
@app.route('/export_download/fichier.xlsx', name='export')
def export():
    val = static_file('fichier.xlsx', root='')
    os.remove('fichier.xlsx')
    return val

@app.route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

#for local or heroku app
try:
    if argv[1]=="local": #for local application, add local param: "$python website.py local"
        run(app, host='localhost', port=8080, debug=True)
    else:
        app.run(host='0.0.0.0', port=argv[1])
except:
    print "You need to specify an argument (local for local testing: $python website.py local)"
