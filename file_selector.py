import tkinter
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

def search_for_file_path (title):
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title=title)
    print(tempdir)
    return tempdir #returns the string that is the directory of choice


#file_path_variable = search_for_file_path()
#print ("\nfile_path_variable = ", file_path_variable)