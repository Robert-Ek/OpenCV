import os
import numpy as np
import pandas as pd

from bounding_box import draw_box
from file_selector import search_for_file_path

#rename a file in a given directory
def create_data_csv(parent_dir, write_dir, gs_folder, csv_name):
    
    count = 1
    #iterate over current files in read directory
    for child_folder in os.listdir(parent_dir):
        
        child_dir = os.path.join(parent_dir, child_folder) #get path of child directory
        
        try:
            for file in os.listdir(child_dir): #look at each file in the child directory
                
                img_name = file #get the file name in the child directory
                img_path = os.path.join(child_dir, img_name) #get the path of the image
                print("Current img path:", img_path) #print the current image path

                boundaries = draw_box(img_path) #get the current box coordinates
                print("Print BOUNDARIES:", boundaries)
                print("\n")

                label = os.path.split(child_dir)[-1] #get the parent folder name of the current img (aka the label of the img)

                gs_path = r"gs://{0}/{1}/{2}".format(gs_folder, child_folder, img_name) #get the gsutil path based on the input parameters
                
                x1 = boundaries[0][0][0]
                y1 = boundaries[0][0][1]
                x2 = boundaries[0][1][0]
                y2 = boundaries[0][1][1]

                print("boundaries for image:", count)
                print(boundaries)
                print(x1,y1,x2,y2)

                #row data has the following format: [set,]image_path[,label,x1,y1,x2,y1,x2,y2,x1,y2]
                row_data = np.array([[gs_path, label, r"{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(x1,y1,x2,y1,x2,y2,x1,y2)]], dtype='object') #get row data information
                #print(row_data)
                #print("\n")
                
                if count == 1: #for the first iteration set the data to the row data
                    data = row_data
                    count += 1 
                
                else: #for all the other iterations stack the data on top of the next
                    data = np.vstack([data, row_data])
                    count += 1 
        except: #this is for the thumbs.db file at the end of the current directory
            continue #do nothing and continue to the next folder

    csv_name = "{}.csv".format(csv_name)
    path = os.path.join(write_dir, csv_name)
    pd.DataFrame(data).to_csv(path, header=None, index=None) #save data

parent_dir = search_for_file_path("Select your parent directory")
write_dir = search_for_file_path("Select directory to write .csv")
gs_folder = "grommet_detector"
csv_name = "grommets"

create_data_csv(parent_dir, write_dir, gs_folder, csv_name)

#gs://grommet_detector/CBP-20220512_133457.jpg