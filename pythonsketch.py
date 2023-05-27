import cv2 
image=cv2.imread("C:/Users/AMMU/Downloads/WhatsApp Image 2023-04-30 at 21.55.07.jpeg")
#apply grey filter converts color # blue green 
#red to gray  which is a module in cv2 
grey_filter =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_filter)
blur=cv2.GaussianBlur(invert,(21,21),0)
invertedblur=cv2.bitwise_not(blur) #have qualities of our need
#providing sketch filter
sketch_filter=cv2.divide(grey_filter,invertedblur,scale=256.0)
cv2.imwrite("output.png",sketch_filter)