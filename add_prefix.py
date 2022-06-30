import tkinter
from tkinter import filedialog
import os

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    print(tempdir)
    return tempdir #returns the string that is the directory of choice

#rename a file in a given directory
def add_prefix(read_dir, prefix): #prefix):
    
    #iterate over current files in read directory
    for curr_file in os.listdir(read_dir):
        
        old_name = curr_file #get old file name
        new_name = prefix+curr_file #create new file name based on input prefix
        
        #get the old file path
        old_path = os.path.join(read_dir, old_name)
        
        #get new file path
        new_path = os.path.join(read_dir, new_name)
        os.rename(old_path, new_path) #rename the old file with the new name

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

read_dir = search_for_file_path()

#print("read directory:", read_dir)
prefix = "PWP-R"

add_prefix(read_dir, prefix)