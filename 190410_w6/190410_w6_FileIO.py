
import cv2
  
img = cv2.imread('HDR.jpg',0) 

newimg = cv2.equalizeHist(img) 
  
cv2.imwrite('HDR2.jpg', newimg) 
  
