#documentation: https://stackoverflow.com/questions/38944102/how-to-continue-drawing-a-rectangle-while-dragging-the-mouse-once-the-left-butto

import cv2

refPt = []
#final_boundaries = []
image = None

def click_and_crop(event, x, y, flags, param):

    global refPt, image, final_boundaries #initialize global variables so they can be accessed outside of this callback function

    final_boundaries=[] #initialize the final boundaries of the image
    
    if event == cv2.EVENT_MOUSEMOVE and flags != cv2.EVENT_FLAG_LBUTTON:
        clone = image.copy()
        cv2.line(clone, (x,y), (x+150, y), (0, 255, 0), 2)
        cv2.line(clone, (x,y), (x, y+150), (0, 255, 0), 2)
        cv2.imshow("image", clone)

    elif event == cv2.EVENT_LBUTTONDOWN: #first initial click 
        refPt = [(x, y)]
    
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON: #while the left mouse button is still being held and dragged
        clone = image.copy()
        cv2.rectangle(clone, refPt[0], (x, y), (0, 255, 0), 2)
        cv2.imshow("image", clone)

    elif event == cv2.EVENT_LBUTTONUP: #if the left mouse button is released 
        refPt.append((x, y))
        final_boundaries.append((refPt[0],refPt[1]))
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)
        cv2.destroyAllWindows()

    #elif event == cv2.EVENT_RBUTTONDOWN: #if the right mouse button is pressed
     #   cv2.destroyAllWindows()

def draw_box(image_path):
    global image
    image = cv2.imread(image_path) #convert to image boundary
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return final_boundaries

#image_path = r"C:\Users\VE040400\Desktop\app_projects\automation\stock.jpg"

#boundaries = draw_box(image_path)
#print(boundaries[0])

#print("x1", boundaries[0][0][0])
#print("y1", boundaries[0][0][1])
#print("x2", boundaries[0][1][0])
#print("y2", boundaries[0][1][1])