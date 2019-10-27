'''
TASK: Create a python script that checks all files in the directory, and puts all picture files in a folder called "Pictures"
'''

'''
QUESTIONS:
How to check all the files in the directory? 
How to check if they are pictures?
How to create a folder called "Pictures" in the directory?
How to group all the pictures identified earlier into the "Pictures" folder?
'''

import os
import shutil 

dirpath = os.getcwd()

def createFolder(dirpath):
    try:
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
    except OSError:
        print ('Error: Creating directory. ' +  dirpath)
        
def main():
    createFolder('./Pictures/')
    for f_name in os.listdir(dirpath):
        if f_name.endswith('.png') or f_name.endswith('.jpg'):
            shutil.move(f_name,'./Pictures/')

if __name__ == "__main__":
    main()