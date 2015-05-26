# -*- coding: utf-8 -*-

import numpy as np
import json
import fit
import random


import xlsxwriter


def generate_fichier(data):
    
    # On crée un "classeur"

    r = random.randint(1,1000)
    classeur = xlsxwriter.Workbook('fichier'+str(r)+'.xlsx')
    # On ajoute une feuille au classeur
    
    
    
    for monAttribut in data['attributes']:
        
        feuille = classeur.add_worksheet(monAttribut['name'])
     
        
        format01 = classeur.add_format()
        format01.set_num_format('0.00')
        
        formatCoeff = classeur.add_format()
        formatCoeff.set_num_format('0.000000')
        
        formatTitre = classeur.add_format()
        formatTitre.set_bg_color('#C0C0C0')
        formatTitre.set_bold()
        
        formatNom = classeur.add_format()
        formatNom.set_font_color('#D95152')
        formatNom.set_align('center')
        formatNom.set_bold()
        #ici on va mettre toutes les infos sur l'attribut
        
        
        
        #feuille.merge_range('A1:B1','Attribut')
        feuille.write(0,0, 'Attribut', formatTitre);
        feuille.write(0,1, '', formatTitre);
        feuille.write(1, 0, 'Name',formatNom)
        feuille.write(2, 0, 'Unit',formatNom)
        feuille.write(3, 0, 'Val_min',formatNom)
        feuille.write(4, 0, 'Val_max',formatNom)
        feuille.write(5, 0, 'Method',formatNom)
        feuille.write(6, 0, 'Mode',formatNom)
        feuille.write(7, 0, 'Active',formatNom)
        
        feuille.write(1, 1, monAttribut['name'])
        feuille.write(2, 1, monAttribut['unit'])
        feuille.write(3, 1, monAttribut['val_min'])
        feuille.write(4, 1, monAttribut['val_max'])
        feuille.write(5, 1, monAttribut['method'])
        feuille.write(6, 1, monAttribut['mode'])
        feuille.write(7, 1, monAttribut['checked'])
        
        #ensuite on va mettre les points obtenus:
        #feuille.merge_range('C1:D1','Points')
        feuille.write(0,2, 'Points', formatTitre);
        feuille.write(0,3, '', formatTitre);
        feuille.write(1, 2, "Y")
        feuille.write(1, 3, "X")
        #on va maintenant les remplir
        lignePoint=0
        
        for monPoint in monAttribut['questionnaire']['points']:
           feuille.write(lignePoint+2, 2, monPoint[0])
           feuille.write(lignePoint+2, 3, monPoint[1])
           lignePoint=lignePoint+1
        
        #Ensuite on s'occupe de la fonction d'utilité
        #feuille.merge_range('E1:F1','Utility Function')
        # on fait une regression à l'aide des points que l'on a dans le questionnaire et on envoit tout ça dans la fonction regressions du fichier fit.py
        points=monAttribut['questionnaire']['points']

        if len(points)>0:
            if monAttribut['mode']=="normal":
                points.append([monAttribut['val_max'], 1]);
                points.append([monAttribut['val_min'], 0]);
            else:
                points.append([monAttribut['val_max'], 0]);
                points.append([monAttribut['val_min'], 1]);

            #go for fit regression using our points
            utilities=fit.regressions_under_list_form(points);
        else:
            #no need of fit regression because we don't have point
            utilities=[]
        ligne=0;


        for utility in utilities:
        
            feuille.write(ligne,4, 'Utility Function', formatTitre);
            feuille.write(ligne,5, '', formatTitre);
            feuille.write(ligne+1, 4, "type",formatNom)
            feuille.write(ligne+2, 4, "a",formatNom)
            feuille.write(ligne+3, 4, "b",formatNom)
            feuille.write(ligne+4, 4, "c",formatNom)
            feuille.write(ligne+5, 4, "d",formatNom)
            feuille.write(ligne+6, 4, "r2",formatNom)
            
            
            
            #feuille.write(ligne, 5, utility)
            #Dans le cas ou la fonciton d'utilité est de type exp
            #on cherche quel est notre type de fonction d'utilite

            if utility['type']=='exp':
                feuille.write(ligne+1, 5, "exponential")
            if utility['type']=='quad':
                feuille.write(ligne+1, 5, "quadratic")
            if utility['type']=='pow':
                feuille.write(ligne+1, 5, "power")
            if utility['type']=='log':
                feuille.write(ligne+1, 5, "logarithm")
            if utility['type']=='lin':
                feuille.write(ligne+1, 5, "linear")

            #On rempli les coefficients
            try:
                #On remplit d'abord le dernier car pour les coefficients d ça s'arretera
                feuille.write(ligne+6, 5, utility['r2'], formatCoeff)
                feuille.write(ligne+2, 5, utility['a'], formatCoeff)
                feuille.write(ligne+3, 5, utility['b'], formatCoeff)
                feuille.write(ligne+4, 5, utility['c'], formatCoeff)
                feuille.write(ligne+5, 5, utility['d'], formatCoeff)
            except:
                pass


            feuille.write(ligne+0,6, 'Calculated points', formatTitre);
            feuille.write(ligne+0,7, '', formatTitre);
            #On va maintenant generer plusieurs points
            amplitude=(monAttribut['val_max']-monAttribut['val_min'])/10.0
            for i in range(0,11):
                feuille.write(ligne+1+i, 6, i*amplitude )
                if utility['type']=='exp':
                    feuille.write(ligne+1+i, 7, funcexp(i*amplitude, utility['a'], utility['b'], utility['c']))
                elif utility['type']=='quad':
                    feuille.write(ligne+1+i, 7, funcquad(i*amplitude, utility['a'], utility['b'], utility['c']))
                elif utility['type']=='pow':
                    feuille.write(ligne+1+i, 7, funcpuis(i*amplitude, utility['a'], utility['b'], utility['c']))
                elif utility['type']=='log':
                    feuille.write(ligne+1+i, 7, funclog(i*amplitude, utility['a'], utility['b'], utility['c'], utility['d']))
                elif utility['type']=='lin':
                    feuille.write(ligne+1+i, 7, funclin(i*amplitude, utility['a'], utility['b']))

            #Ensuite on fait le Chart ! (le diagramme)
            chart5 = classeur.add_chart({'type': 'scatter',
                                        'subtype': 'smooth'})

            # Configure the first series.
            chart5.add_series({
                              'name':       utility['type'],
                              'categories': '='+monAttribut['name']+'!$G$'+str(ligne+2)+':$G$'+str(ligne+12),
                              'values':     '='+monAttribut['name']+'!$H$'+str(ligne+2)+':$H$'+str(ligne+12),
     
                              })
     
            # Add a chart title and some axis labels.
            chart5.set_title ({'name': 'Utility Function'})

            # Set an Excel chart style.
            chart5.set_style(4)
            chart5.set_x_axis({
                             'min': monAttribut['val_min'],
                             'max': monAttribut['val_max']
                             })

            # Insert the chart into the worksheet (with an offset).
            feuille.insert_chart('I'+str(1+ligne), chart5, {'x_offset': 25, 'y_offset': 10})
            
            ligne+=15;

    for mesK in data['k_calculus']:
        feuille = classeur.add_worksheet("Multi attribute "+mesK['method'])
    

        
        formatTitre = classeur.add_format()
        formatTitre.set_bg_color('#C0C0C0')
        formatTitre.set_bold()
        
        formatNom = classeur.add_format()
        formatNom.set_font_color('#D95152')
        formatNom.set_align('center')
        formatNom.set_font_size(12)
        formatNom.set_bold()
        #ici on va mettre toutes les infos sur l'attribut
        
        feuille.write(0,0, 'K', formatTitre);
        feuille.set_column(0, 0, 15);
        feuille.write(0,1, 'Value', formatTitre);
        feuille.write(0,2, 'Attribute', formatTitre);
        feuille.set_column(2, 2, 50);
        feuille.write(0,3, 'IDAttribute', formatTitre);
        feuille.set_column(3, 3, 15);

        ligne=1
        for monK in mesK['k']:
            feuille.write(ligne, 0, monK['ID'], formatNom)
            feuille.write(ligne, 1, monK['value'])
            feuille.write(ligne, 2, json.dumps(monK['attribute']))
            feuille.write(ligne, 3, json.dumps(monK['ID_attribute']))
            ligne=ligne+1
    

        feuille.write(ligne, 0, "K", formatNom)
        feuille.write(ligne, 1, mesK['GK'])

    # Ecriture du classeur sur le disque
    classeur.close()

    #On retourne le nom du fichier
    return 'fichier'+str(r)

#generate juste the file with utility function we checked
def generate_fichier_with_specification(data):
    
    r = random.randint(1,1000)
    classeur = xlsxwriter.Workbook('fichier'+str(r)+'.xlsx')
    # On ajoute une feuille au classeur
    
    
    
    for monAttribut in data['attributes']:
        #we first check if the attribute have a list o defined utility function

        
        feuille = classeur.add_worksheet(monAttribut['name'])
     
        
        format01 = classeur.add_format()
        format01.set_num_format('0.00')
        
        formatCoeff = classeur.add_format()
        formatCoeff.set_num_format('0.000000')
        
        formatTitre = classeur.add_format()
        formatTitre.set_bg_color('#C0C0C0')
        formatTitre.set_bold()
        
        formatNom = classeur.add_format()
        formatNom.set_font_color('#D95152')
        formatNom.set_align('center')
        formatNom.set_bold()
        #ici on va mettre toutes les infos sur l'attribut
        
        
        
        #feuille.merge_range('A1:B1','Attribut')
        feuille.write(0,0, 'Attribut', formatTitre);
        feuille.write(0,1, '', formatTitre);
        feuille.write(1, 0, 'Name',formatNom)
        feuille.write(2, 0, 'Unit',formatNom)
        feuille.write(3, 0, 'Val_min',formatNom)
        feuille.write(4, 0, 'Val_max',formatNom)
        feuille.write(5, 0, 'Method',formatNom)
        feuille.write(6, 0, 'Mode',formatNom)
        feuille.write(7, 0, 'Active',formatNom)
        
        feuille.write(1, 1, monAttribut['name'])
        feuille.write(2, 1, monAttribut['unit'])
        feuille.write(3, 1, monAttribut['val_min'])
        feuille.write(4, 1, monAttribut['val_max'])
        feuille.write(5, 1, monAttribut['method'])
        feuille.write(6, 1, monAttribut['mode'])
        feuille.write(7, 1, monAttribut['checked'])
        
        #ensuite on va mettre les points obtenus:
        #feuille.merge_range('C1:D1','Points')
        feuille.write(0,2, 'Points', formatTitre);
        feuille.write(0,3, '', formatTitre);
        feuille.write(1, 2, "Y")
        feuille.write(1, 3, "X")
        #on va maintenant les remplir
        lignePoint=0
        
        for monPoint in monAttribut['questionnaire']['points']:
           feuille.write(lignePoint+2, 2, monPoint[0])
           feuille.write(lignePoint+2, 3, monPoint[1])
           lignePoint=lignePoint+1
        
        #Ensuite on s'occupe de la fonction d'utilité
        #feuille.merge_range('E1:F1','Utility Function')
        # on fait une regression à l'aide des points que l'on a dans le questionnaire et on envoit tout ça dans la fonction regressions du fichier fit.py
        utilities=monAttribut['utilities']
        
        ligne=0;

        for utility in utilities:
        
            feuille.write(ligne,4, 'Utility Function', formatTitre);
            feuille.write(ligne,5, '', formatTitre);
            feuille.write(ligne+1, 4, "type",formatNom)
            feuille.write(ligne+2, 4, "a",formatNom)
            feuille.write(ligne+3, 4, "b",formatNom)
            feuille.write(ligne+4, 4, "c",formatNom)
            feuille.write(ligne+5, 4, "d",formatNom)
            feuille.write(ligne+6, 4, "r2",formatNom)
            
            
            
            #feuille.write(ligne, 5, utility)
            #Dans le cas ou la fonciton d'utilité est de type exp
            #on cherche quel est notre type de fonction d'utilite

            if utility['type']=='exp':
                feuille.write(ligne+1, 5, "exponential")
            if utility['type']=='quad':
                feuille.write(ligne+1, 5, "quadratic")
            if utility['type']=='pow':
                feuille.write(ligne+1, 5, "power")
            if utility['type']=='log':
                feuille.write(ligne+1, 5, "logarithm")
            if utility['type']=='lin':
                feuille.write(ligne+1, 5, "linear")

            #On rempli les coefficients
            try:
                #On remplit d'abord le dernier car pour les coefficients d ça s'arretera
                feuille.write(ligne+6, 5, utility['r2'], formatCoeff)
                feuille.write(ligne+2, 5, utility['a'], formatCoeff)
                feuille.write(ligne+3, 5, utility['b'], formatCoeff)
                feuille.write(ligne+4, 5, utility['c'], formatCoeff)
                feuille.write(ligne+5, 5, utility['d'], formatCoeff)
            except:
                pass


            feuille.write(ligne+0,6, 'Calculated points', formatTitre);
            feuille.write(ligne+0,7, '', formatTitre);
            #On va maintenant generer plusieurs points
            amplitude=(monAttribut['val_max']-monAttribut['val_min'])/10.0
            for i in range(0,11):
                feuille.write(ligne+1+i, 6, i*amplitude )
                if utility['type']=='exp':
                    feuille.write(ligne+1+i, 7, funcexp(i*amplitude, utility['a'], utility['b'], utility['c']))
                elif utility['type']=='quad':
                    feuille.write(ligne+1+i, 7, funcquad(i*amplitude, utility['a'], utility['b'], utility['c']))
                elif utility['type']=='pow':
                    feuille.write(ligne+1+i, 7, funcpuis(i*amplitude, utility['a'], utility['b'], utility['c']))
                elif utility['type']=='log':
                    feuille.write(ligne+1+i, 7, funclog(i*amplitude, utility['a'], utility['b'], utility['c'], utility['d']))
                elif utility['type']=='lin':
                    feuille.write(ligne+1+i, 7, funclin(i*amplitude, utility['a'], utility['b']))

            #Ensuite on fait le Chart ! (le diagramme)
            chart5 = classeur.add_chart({'type': 'scatter',
                                        'subtype': 'smooth'})

            # Configure the first series.
            chart5.add_series({
                              'name':       utility['type'],
                              'categories': '='+monAttribut['name']+'!$G$'+str(ligne+2)+':$G$'+str(ligne+12),
                              'values':     '='+monAttribut['name']+'!$H$'+str(ligne+2)+':$H$'+str(ligne+12),
     
                              })
     
            # Add a chart title and some axis labels.
            chart5.set_title ({'name': 'Utility Function'})

            # Set an Excel chart style.
            chart5.set_style(4)
            chart5.set_x_axis({
                             'min': monAttribut['val_min'],
                             'max': monAttribut['val_max']
                             })

            # Insert the chart into the worksheet (with an offset).
            feuille.insert_chart('I'+str(1+ligne), chart5, {'x_offset': 25, 'y_offset': 10})
            
            ligne+=15;


    for mesK in data['k_calculus']:
        feuille = classeur.add_worksheet("Multi attribute "+mesK['method'])
    

        
        formatTitre = classeur.add_format()
        formatTitre.set_bg_color('#C0C0C0')
        formatTitre.set_bold()
        
        formatNom = classeur.add_format()
        formatNom.set_font_color('#D95152')
        formatNom.set_align('center')
        formatNom.set_font_size(12)
        formatNom.set_bold()
        #ici on va mettre toutes les infos sur l'attribut
        
        feuille.write(0,0, 'K', formatTitre);
        feuille.set_column(0, 0, 15);
        feuille.write(0,1, 'Value', formatTitre);
        feuille.write(0,2, 'Attribute', formatTitre);
        feuille.set_column(2, 2, 50);
        feuille.write(0,3, 'IDAttribute', formatTitre);
        feuille.set_column(3, 3, 15);

        ligne=1
        for monK in mesK['k']:
            feuille.write(ligne, 0, monK['ID'], formatNom)
            feuille.write(ligne, 1, monK['value'])
            feuille.write(ligne, 2, json.dumps(monK['attribute']))
            feuille.write(ligne, 3, json.dumps(monK['ID_attribute']))
            ligne=ligne+1

        feuille.write(ligne, 0, "K", formatNom)
        feuille.write(ligne, 1, mesK['GK'])




    # Ecriture du classeur sur le disque
    classeur.close()

    #On retourne le nom du fichier
    return 'fichier'+str(r)





# Fucntions
def funcexp(x, a, b, c):			# fonction for the exponential regression
    return a * np.exp(-b * x) + c
        
def funcquad(x, a, b, c):			# fonction for the quadratic regression
    return c*x-b*x**2+a

def funcpuis(x, a, b, c):			# fonction for the puissance regression
    return a*(x**(1-b)-1)/(1-b) + c

def funclog(x, a, b, c, d):			# fonction for the logarithmic regression
    return a*np.log(b*x+c)+d

def funclin(x, a, b):				# fonction for the logarithmic regression
    return a*x+b


