from openpyxl import load_workbook
import os
import sys

def importation(file):
    
    try:
        wb = load_workbook(filename=file, read_only=True)
        
        
        mySession={'attributes':[], 'k_calculus':[{'method':'multiplicative', 'active':'false', 'k':[], 'GK':None},{'method':'multilinear','active':'false', 'k':[], 'GK':None}]}
        
        
        for sheet in wb:
            myAttribut={}
            ws = wb[sheet.title] # ws is now an IterableWorksheet
            myAttribut['name']=ws['B2'].value
            myAttribut['unit']=ws['B3'].value
            myAttribut['val_min']=ws['B4'].value
            myAttribut['val_max']=ws['B5'].value
            myAttribut['method']=ws['B6'].value
            myAttribut['mode']=ws['B7'].value
            myAttribut['checked']=ws['B8'].value
            
            myAttribut['questionnaire']={};
            
            
                                                              
            ligne=3
            number=0
            mesPoints=[]
            
            while ws['C'+str(ligne)].value!=None:
                mesPoints.append([ws['C'+str(ligne)].value, ws['D'+str(ligne)].value])
                ligne=ligne+1
                number=number+1
            
            myAttribut['questionnaire']['points']=mesPoints;
            myAttribut['questionnaire']['number']=number;
            
            mySession['attributes'].append(myAttribut)
     
        os.remove(file)
        return {'success':True, 'data':mySession}
    except:
        return {'success':False, 'data':sys.exc_info()[0]}





