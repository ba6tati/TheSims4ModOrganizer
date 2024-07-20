from customtkinter import *
from tkinter import messagebox, filedialog
from app.utils import create_profile
import os
import shutil
import json
import pandas as pd

class MainWindow(CTk):
    def __init__(self, **kwargs):
        super().__init__()
        
        # self.ts4_path = ''
        self.user = kwargs.pop('user', None)
        
        self.ts4_user_files = kwargs.pop('ts4_user_files', None)
        
        if not os.path.exists('data'):
            if os.path.exists(self.ts4_user_files):
                preserveFiles = messagebox.askyesno(title='WARNING', message='User files for The Sims 4 are found. Do you want to preserve them?')
                    
                if preserveFiles:
                    for element in os.listdir(self.ts4_user_files):
                        shutil.move(os.path.join(self.ts4_user_files, element), os.path.join(self.ts4_user_files, 'defaultProfile', element))
                            
                    with open('data', 'w+') as f:
                        pass
                        
                    create_profile('defaultProfile')
        
        """
        with open('data', 'r+') as f:
            foundPath = False
            
            for line in f.readlines():
                if line.startswith('ts4_path'):
                    foundPath = True
                    self.ts4_path = line.split('=')
                    
            if not foundPath:
                messagebox.showwarning(title='WARNING', message='The program could not find The Sims 4 path. Please navigate to the installation directory.')
                
                while True:
                    directory = os.path.join(filedialog.askdirectory(title='Select The Sims 4 installation directory'), 'Game/Bin/TS4_x64.exe')
                    
                    if os.path.exists(directory):
                        self.ts4_path = directory
                        break
                    else:
                        messagebox.showerror(title='ERROR', message='TS4_x64.exe was not found. Please navigate to The Sims 4 installation directory')
        """
        
        
                    
        self.title('TS4 Profile Organizer')
        
        self.create_button = CTkButton(self, text='Create New')
        self.create_button.pack()
        
    def check_for_existing_files(self):
        user = os.environ.get('USERNAME')
        
        # if os.path.exists()