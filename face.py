import cv2
capInput = cv2.VideoCapture(0)
if not capInput.isOpened():
	print('Capture failed because of camera')
ret, img = capInput.read()
cv2.imwrite('face1.png', img)
img = cv2.imread('face1.png')
imgWindowName = 'ImageCaptured'
imgWindow = cv2.namedWindow(imgWindowName)
cv2.imshow(imgWindowName, img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
