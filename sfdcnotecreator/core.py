# -*- coding: utf-8 -*-
import controller
import os
from pathlib import Path

def processnotes():
    #Construct Output Directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    directory = "Output"
    outputpath = os.path.join(dir_path, directory)
    dataLoader = controller.Controller('DSN=DSMOD')
    df = dataLoader.query('SELECT * FROM "ContentNote"')
    df['FILENAME'] = outputpath + '/' + df['TITLE'].map(str) + '.txt'
    Path(outputpath).mkdir(parents=True, exist_ok=True)
    #Create the TextFiles
    writetofile(df)
    #RemoveContentFromDF
    df = df.drop('CONTENT', 1)
    #RemoveOwnerId Due to visibility problem
    df = df.drop('OWNERID', 1)
    #Write CSV to Output Directory
    df.to_csv(outputpath + '/CONTENTNOTEIMPORT.csv',index=False)
    return 0

def writetofile(df):
    for index, row in df.iterrows():
        f = open(row['FILENAME'], 'w')
        f.write(str(row['CONTENT']))
        f.close()

processnotes()