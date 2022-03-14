import os
import shutil
import tkinter as tk
from tkinter import filedialog

i = 0
import os
print("WELCOME TO PICTURE CLEANER! THIS APPLICATION WILL COPY YOUR OLD PICTURES AND RENAMED IT IN NEW FOLDER")
print("Give the path of the images: ")
Path = input()+ "\\"
directory = os.fsencode(Path)
i = 0
j = 0
k = 0
print("How many pictures/folder?")
syöte = input() 
folderSize = int(syöte)
print("Which name you want to for your pictures?")
pictureName = input()

for file in os.listdir(directory):
    FolderNumber = str(j)
    New_Folder= Path+FolderNumber
    if not os.path.exists(New_Folder):
        print("Created new directory in this location: "+ New_Folder)
        os.mkdir(New_Folder)

    Number = str(k)
    filename = os.fsdecode(file)
    if(filename.endswith(".jpg") or filename.endswith(".png")):
        if(filename.endswith(".jpg")):
            print(filename)
            old_name = Path + filename
            new_name = Path + pictureName +" "+ Number + ".jpg"
            os.rename(old_name,new_name)
            try:
                shutil.move(new_name,New_Folder )
                print("File copied successfully.")
 
            # If source and destination are same
            except shutil.SameFileError:
                print("Source and destination represents the same file.")
                
        if(filename.endswith(".png")):
            print(filename)
            old_name = Path + filename
            new_name = Path +pictureName +" "+ Number +".png"
            os.rename(old_name,new_name)
            try:
                shutil.move(new_name,New_Folder )
                print("File moved successfully.")
 
            # If source and destination are same
            except shutil.SameFileError:
                print("That file already in the location..")
            
    else:
        continue
    i = i+1
    k = k+1
    if(i==folderSize):
        i=0
        j = j+1

       