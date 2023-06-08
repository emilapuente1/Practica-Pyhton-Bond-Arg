# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 22:16:45 2023

@author: EMILIANO
"""

import openpyxl
import pandas as pd

Excelworkbook=openpyxl.load_workbook("H:\Documentos\Practica Pyhton Bond Arg\Dataset bonos arg usd.xlsx")
Excelsheet=Excelworkbook.active

bondarg=pd.DataFrame(Excelsheet.values)
