import numpy as np
import cv2
def detect(img,faceCascade,eyesCascade,noseCascade,mouthCascade):
	# coordinates  of the face
	coords=faceCascade.detectMultiScale(img,1.1,10)
	if(len(coords[0])==4):
		# cropped image to look for other parts of the face
		img=img[coords[0][1]:coords[0][1]+coords[0][3],coords[0][0]:coords[0][0]+coords[0][2]]
		coords=getCoor(coords,img,eyesCascade,noseCascade,mouthCascade)
	return coords
def getCoor(coords,roi,eyesCascade,noseCascade,mouthCascade):
	# append the coordinates of eyes nose and mouth with the mouth
	eyeFea=eyesCascade.detectMultiScale(roi,1.3,20)
	noseFea=noseCascade.detectMultiScale(roi,1.3,4)
	mouthFea=mouthCascade.detectMultiScale(roi,1.3,20)
	if(len(eyeFea) and len(noseFea) and len(mouthFea)):
		coords=np.append(coords,eyeFea,0)
		coords=np.append(coords,noseFea,0)
		coords=np.append(coords,mouthFea,0)
	else:
		print("The Image is not clear or In right Posture, Upload a New One")
		exit(0)
	return coords
