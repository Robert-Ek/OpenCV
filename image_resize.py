import os
import cv2
from file_selector import search_for_file_path

def resize_img(parent_dir, new_width):

    #iterate over current files in read directory
    for child_folder in os.listdir(parent_dir):

        child_dir = os.path.join(parent_dir, child_folder) #get path of child directory

        try:
            for file in os.listdir(child_dir): #look at each file in the child directory

                img_name = file #get the file name in the child directory
                img_path = os.path.join(child_dir, img_name) #get the path of the image
                
                print("Current img path:", img_path) #print the current image path
                
                img = cv2.imread(img_path) #get the current image data

                if img.shape[1] < img.shape[0]:

                    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) #turn the image 90 degrees

                print("image size (W x H):", img.shape[1], img.shape[0])
                
                scale = (new_width/img.shape[1])
                print("scale value:", scale)
                
                w = int(img.shape[1] * scale) #get the width and height of the image
                h = int(img.shape[0] * scale)
                
                print("new calculated width and height", w, h)
                print("\n")
                
                dim = (w, h)
                new_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) #downsize image
                new_img =cv2.blur(src=new_img, ksize=(5, 5)) #blur the downsized image
                cv2.imwrite(img_path, new_img)
                
        except: #when it hits the thumbs.db file it wont explode
            continue
            
title = "Please select the parent directory"
parent_dir = search_for_file_path(title)
new_width = 750
        
resize_img(parent_dir, new_width)