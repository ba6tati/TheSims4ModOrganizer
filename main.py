import os, shutil
from tkinter import messagebox

from app import MainWindow
from app.utils import create_profile

if __name__ == '__main__':
    user = os.environ.get('USERNAME')
    ts4_user_files = f'C:\\Users\\{user}\\Documents\\Electronic Arts\\The Sims 4 Profiles'
    
    if not os.path.exists('data'):
        if os.path.exists(ts4_user_files):
            preserveFiles = messagebox.askyesno(title='WARNING', message='User files for The Sims 4 are found. Do you want to preserve them?')
                
            if preserveFiles:
                for element in os.listdir(ts4_user_files):
                    shutil.move(os.path.join(ts4_user_files, element), os.path.join(ts4_user_files, 'defaultProfile', element))
                        
                with open('data', 'w+') as f:
                    pass
                    
                create_profile('defaultProfile')
                    
    root = MainWindow(user=user, ts4_user_files=ts4_user_files)
    root.mainloop()