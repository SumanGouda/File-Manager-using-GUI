import tkinter
import os
import shutil
from tkinter import filedialog

class File_organizer:
    def __init__(self):
        self.folder = filedialog.askdirectory(title="Select your folder")
            #Opens the file manager window of PC which allows the user to select folder.

    
    def organize (self):
        if not self.folder:
            print("No folder selected.")
            return        #If no folder selected then the code stops here by printing an output "No folder selected."
        
        for file in os.listdir(self.folder):
            file_path = os.path.join(self.folder,file)       #Makes a path to the all the files in  the folder one by one.
            
            if os.path.isdir(file_path):
                continue    #Skips the next lines in that perticular loop if the file_path is a directory.
            
            _, ext = os.path.splitext(file)
            ext = ext[1:]
            
            new_folder = os.path.join(self.folder, ext)    #Makes a path to the new folder.
            if not os.path.exists(new_folder):         
                os.makedirs(new_folder)        #Creates the folder if it does not exists.
                
            shutil.move(file_path, os.path.join(new_folder,file))    #Moves the file from source to destination.
            
organizer = File_organizer()
organizer.organize()

            

                

