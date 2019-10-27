# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:39:32 2019

@author: Rahul
"""
import os
import shutil
from datetime import datetime

def createFoldersInDirectory(folderStructure):
    split_direc = folderStructure.split('/')
    defaultdir = 'C:\\Users\\Rahul\\Desktop\\MyStaY aT emdEn\\Full time\\Applied companies\\Phase-2'
    for i in range(0,len(split_direc)):
        newdir = os.path.join(defaultdir,split_direc[i])
        folder_exist = doesFolderExist(newdir)
        
        if(folder_exist):
            if(i == 0):
                pass
            else:
                foldername = split_direc[1]+ datetime.now().strftime('%Y-%j')
                newdir = os.path.join(defaultdir,foldername)
                os.mkdir(newdir)                      
        else:
            os.mkdir(newdir)
        
        defaultdir = newdir 
        
def doesFolderExist(directory):
    if os.path.exists(directory):
        returntxt = True
    else:
        returntxt = False        
    return returntxt

def copyFile2Location(sourceLocation,targetLocation):
    shutil.copy(sourceLocation,targetLocation)
