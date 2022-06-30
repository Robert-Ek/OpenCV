import cv2

img_path = r"C:\Users\VE040400\OneDrive - Honda\Desktop\app_projects\automation\test_parent\child 2\PWP-R20220629_084516.jpg"

img = cv2.imread(img_path)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

blur_img =cv2.blur(src=img, ksize=(5, 5))
cv2.imshow('blurred', blur_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

