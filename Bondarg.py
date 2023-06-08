# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 22:16:45 2023

@author: EMILIANO
"""

import openpyxl
import pandas as pd
##Workbook va en mayusculas la primera
from openpyxl import Workbook


Excelworkbook=openpyxl.load_workbook("D:\Documentos\GitHub\Practica-Pyhton-Bond-Arg\Dataset bonos arg usd.xlsx")
Excelsheet=Excelworkbook.active

#obtener los titulos
titulos= next(Excelsheet.values)[0:]

bondarg=pd.DataFrame(Excelsheet.values,columns=titulos)
bondarg=bondarg.drop(bondarg.index[0])

# creamos las columnas de diferencia de precio entre AE38-AL30 y Al41 - AL30
bondarg["Diferencia Precio 38-30"]=bondarg[" AE38D "]-bondarg[" AL30D "]
bondarg["Diferencia Precio 41-30"]=bondarg[" AL41D "]-bondarg[" AL30D "]
media_38_30=bondarg["Diferencia Precio 38-30"].mean()
media_41_30=bondarg["Diferencia Precio 41-30"].mean()


# ##Workbook va en mayusculas la primera
# nuevoexcel=Workbook()
# nuevoexcel_sheet=nuevoexcel.active

# nuevoexcel=bondarg
# nuevoexcel.save("datasetarg.xlsx")