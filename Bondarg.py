# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 22:16:45 2023

@author: EMILIANO
"""

import openpyxl
import pandas as pd
##Workbook va en mayusculas la primera
from openpyxl import Workbook


Excelworkbook=openpyxl.load_workbook("H:\Documentos\Practica Pyhton Bond Arg\Dataset bonos arg usd.xlsx")
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
# como navegar por columnas con el iloc con cordenas
bono38=bondarg.iloc[0:,5
                    ]
# copiar un "Dataframe" y pegarlo en otro lado Copia 2 

# copia2
# bondarg2=bondarg

# # altero el original solo con la columna 
# bondarg=bondarg[" AE38D "]

bondarg_head10=bondarg[["Date"," AE38D "]].head(10)
bondarg_tail10=bondarg[["Date"," AE38D "]].tail(10)

bondarg_combinado=bondarg_head10.append(bondarg_tail10)


bondarg_combinado2= bondarg_head10.append(\
        [bondarg_tail10,bondarg_head10]    \
         )
    