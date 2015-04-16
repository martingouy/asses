# -*- coding: utf-8 -*-

import numpy as np
import json


import xlsxwriter


def generate_fichier(data):
    
    # On creer un "classeur"
    classeur = xlsxwriter.Workbook('export/fichier.xlsx')
    # On ajoute une feuille au classeur
    feuille = classeur.add_worksheet("feuille 1")
    
    ligne=0
    
    
    for monAttribut in data['attributes']:

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
        #ici on va mettre toutes les infos sur l'attribu
        
        
        
        #feuille.merge_range('A1:B1','Attribut')
        feuille.write(ligne,0, 'Attribut', formatTitre);
        feuille.write(ligne,1, '', formatTitre);
        feuille.write(ligne+1, 0, 'name',formatNom)
        feuille.write(ligne+2, 0, 'unit',formatNom)
        feuille.write(ligne+3, 0, 'val_min',formatNom)
        feuille.write(ligne+4, 0, 'val_max',formatNom)
        feuille.write(ligne+5, 0, 'method',formatNom)
        feuille.write(ligne+6, 0, 'mode',formatNom)
        feuille.write(ligne+7, 0, 'completed',formatNom)
        
        feuille.write(ligne+1, 1, monAttribut['name'])
        feuille.write(ligne+2, 1, monAttribut['unit'])
        feuille.write(ligne+3, 1, monAttribut['val_min'])
        feuille.write(ligne+4, 1, monAttribut['val_max'])
        feuille.write(ligne+5, 1, monAttribut['method'])
        feuille.write(ligne+6, 1, monAttribut['mode'])
        feuille.write(ligne+7, 1, monAttribut['completed'])
        
        #ensuite on va mettre les points obtenus:
        #feuille.merge_range('C1:D1','Points')
        feuille.write(ligne,2, 'Points', formatTitre);
        feuille.write(ligne,3, '', formatTitre);
        feuille.write(ligne+1, 2, "Y")
        feuille.write(ligne+1, 3, "X")
        #on va maintenant les remplir
        lignePoint=0
        
        for monPoint in monAttribut['questionnaire']['points']:
           feuille.write(ligne+lignePoint+2, 2, monPoint[0])
           feuille.write(ligne+lignePoint+2, 3, monPoint[1])
           lignePoint=lignePoint+1
        
        #Ensuite on s'occupe de la fonction d'utilité
        #feuille.merge_range('E1:F1','Utility Function')
        feuille.write(ligne,4, 'Utility Function', formatTitre);
        feuille.write(ligne,5, '', formatTitre);
        feuille.write(ligne+1, 4, "type",formatNom)
        feuille.write(ligne+2, 4, "a",formatNom)
        feuille.write(ligne+3, 4, "b",formatNom)
        feuille.write(ligne+4, 4, "c",formatNom)
        feuille.write(ligne+5, 4, "d",formatNom)
        feuille.write(ligne+6, 4, "r2",formatNom)
        
        #puis on va la remplir
        utility=monAttribut['questionnaire']['utility']
        #feuille.write(ligne, 5, utility)
        #Dans le cas ou la fonciton d'utilité est de type exp
        #on cherche quel est notre type de fonction d'utilite
        UtilityType=''
        try:
            utility=utility['exp']
            feuille.write(ligne+1, 5, "exponential")
            UtilityType='exp'
        except:
            pass
        try:
            utility=utility['quad']
            feuille.write(ligne+1, 5, "quadratic")
            UtilityType='quad'
        except:
            pass
        try:
            utility=utility['pow']
            feuille.write(ligne+1, 5, "power")
            UtilityType='pow'
        except:
            pass
        try:
            utility=utility['log']
            feuille.write(ligne+1, 5, "logarithm")
            UtilityType='log'
        except:
            pass
        try:
            utility=utility['lin']
            feuille.write(ligne+1, 5, "linear")
            UtilityType='lin'
        except:
            pass
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


        feuille.write(ligne,6, 'Calculated points', formatTitre);
        feuille.write(ligne,7, '', formatTitre);
        #On va maintenant generer plusieurs points
        amplitude=(monAttribut['val_max']-monAttribut['val_min'])/10
        for i in range(0,11):
            feuille.write(ligne+1+i, 6, i*amplitude )
            if UtilityType=='exp':
                feuille.write(ligne+1+i, 7, funcexp(i*amplitude, utility['a'], utility['b'], utility['c']))
            elif UtilityType=='quad':
                feuille.write(ligne+1+i, 7, funcquad(i*amplitude, utility['a'], utility['b'], utility['c']))
            elif UtilityType=='pow':
                feuille.write(ligne+1+i, 7, funcpuis(i*amplitude, utility['a'], utility['b'], utility['c']))
            elif UtilityType=='log':
                feuille.write(ligne+1+i, 7, funclog(i*amplitude, utility['a'], utility['b'], utility['c'], utility['d']))
            elif UtilityType=='lin':
                feuille.write(ligne+1+i, 7, funclin(i*amplitude, utility['a'], utility['b']))

        #Ensuite on fait le Chart ! (le diagramme)
        chart5 = classeur.add_chart({'type': 'scatter',
                                    'subtype': 'smooth'})

        # Configure the first series.
        chart5.add_series({
                          'name':       UtilityType,
                          'categories': '=feuille 1!$G$'+str(ligne+2)+':$G$'+str(ligne+12),
                          'values':     '=feuille 1!$H$'+str(ligne+2)+':$H$'+str(ligne+12),
 
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
        feuille.insert_chart('I'+str(ligne+1), chart5, {'x_offset': 25, 'y_offset': 10})

        #if UtilityType=='exp':
        

        # Ecrire "2" dans la cellule à la ligne 0 et la colonne 1
        ligne=ligne+16


    # Ecriture du classeur sur le disque
    classeur.close()

    #On retourne le nom du fichier
    return "fichier.xlsx"

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


