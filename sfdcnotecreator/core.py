# -*- coding: utf-8 -*-
import os
import pyodbc
import pandas as pd
from pathlib import Path

def processnotes():
    #Construct Output Directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    directory = "Output"
    outputpath = os.path.join(dir_path, directory)
    dsnname = input("Please Provide the ODBC DSN Name: ")
    cnctn = pyodbc.connect('DSN=' + dsnname) #DSMOD
    query = input("Please provide the query eg. SELECT * FROM SFDCSTG.ContentNote : ")
    df = pd.read_sql(query, cnctn) #SELECT * FROM "ContentNote"
    df['FILENAME'] = outputpath + '/' + df['TITLE'].map(str) + '.txt'
    Path(outputpath).mkdir(parents=True, exist_ok=True)
    #Create the TextFiles
    writetofile(df)
    #RemoveContentFromDF
    df = df.drop('CONTENT', axis=1)
    #RemoveOwnerId Due to visibility problem
    df = df.drop('OWNERID', axis=1)
    #Write CSV to Output Directory
    df.to_csv(outputpath + '/CONTENTNOTEIMPORT.csv',index=False)
    print('Output Has Been Generated at ' + outputpath) 

def writetofile(df):
    for index, row in df.iterrows():
        f = open(row['FILENAME'], 'w')
        f.write(str(row['CONTENT']))
        f.close()
        