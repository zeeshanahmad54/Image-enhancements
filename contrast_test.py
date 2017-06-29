'''
The script applies the ax + b formula on the image ( RGB format itself ), where a = contrast
																				x = image
																				b = brightness 

'''
import cv2
import numpy as np

img = cv2.imread("img.png")	#path of the image to be read
cv2.imshow("original",img)
cv2.waitKey(0)

array_alpha = np.array([1.98])	#array_alpha (a) controls contrast (a>1 means more contrast and 0<a<1 less contrast)	

new_img = cv2.multiply(new_img, array_alpha)  

cv2.imshow("newimg",new_img)
cv2.waitKey(0)