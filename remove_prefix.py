import os
import tkinter
from tkinter import filedialog

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    print(tempdir)
    return tempdir #returns the string that is the directory of choice

#remove "n" characters from beginning of file namecolo
def remove_prefix(read_dir, n): #prefix):
    
    #iterate over current files in read directory
    for curr_file in os.listdir(read_dir):
        
        old_name = curr_file #get old file name
        new_name = curr_file[n:] #eliminate prefix
        
        #get the old file path
        old_path = os.path.join(read_dir, old_name)
        
        #get new file path
        new_path = os.path.join(read_dir, new_name)
        os.rename(old_path, new_path) #rename the old file with the new name

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

read_dir = search_for_file_path()
n = 5

remove_prefix(read_dir, n)