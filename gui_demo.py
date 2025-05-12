import tkinter
import os
import shutil
from tkinter import filedialog

class File_organizer:
    def __init__(self):
        self.folder = filedialog.askdirectory(title="Select your folder")

    
    def organize (self):
        if not self.folder:
            print("No folder selected.")
            return
        
        for file in os.listdir(self.folder):
            file_path = os.path.join(self.folder,file)
            
            if os.path.isdir(file_path):
                continue
            
            _, ext = os.path.splitext(file)
            ext = ext[1:]
            
            new_folder = os.path.join(self.folder, ext)
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
                
            shutil.move(file_path, os.path.join(new_folder,file))
            
organizer = File_organizer()
organizer.organize()

            

                

