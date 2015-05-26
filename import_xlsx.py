from openpyxl import load_workbook
import os

def importation(file):
    try:
        wb = load_workbook(filename=file, read_only=True)
        
        
        mySession=[];
        
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

            mySession.append(myAttribut)

        print(mySession)
        os.remove(file)
    
    except:
        os.remove(file)



