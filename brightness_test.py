import cv2
import numpy as np

image = cv2.imread("Lenna.png")	#path of the image to be read
value = 30						#brightness value
br = np.where((255 - image) < value,255,image+value)	#add brightness value to the image pixel. if image+value > 255, new value is 255
br[(br < (value+10,value+10,value+10)).all(2)]=0	
cv2.imwrite("br_img.png",br)
du = np.where(image < value,0,image-value)	#subtract brightness value from the image pixel. if image-value < 0, new value is 0
cv2.imwrite("du_img.png",du)