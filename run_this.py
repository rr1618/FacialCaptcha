# This file contains the funciton(
# 1. draw_boundary()
# 2.true_click()
# 3.setMouseCallback
import coordinates
import cv2
import copy
import numpy as np
# load all the cascasde classifier xml file
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyesCascade = cv2.CascadeClassifier('ojoI.xml')
noseCascade = cv2.CascadeClassifier('Nariz.xml')
mouthCascade = cv2.CascadeClassifier('Mouth.xml')
# Load the image as a numpy array
img=cv2.resize(cv2.imread('TestImage.jpg'),(413,531))
rahul = cv2.resize(cv2.imread('TestImage.jpg'),(413,531))

coords=coordinates.detect(rahul,faceCascade,eyesCascade,noseCascade,mouthCascade)
# print(coords)
# store the coordinates of the face
face=coords[0]
# Correct the coordinates irrespective of the cropped coordinates, in case if the right eye is detected first
for i in range(1,5):
    coords[i][0]+=face[0]
    coords[i][1]+=face[0]
# a check between left and right eye
if(coords[1][0]>coords[2][0]):
    temp=copy.deepcopy(coords[1])
    coords[1]=copy.deepcopy(coords[2])
    coords[2]=temp
colors={"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255),"dblue":(0,247,255)}
color=iter({"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255),"dblue":(0,247,255)})
text=iter(["Face","LEye","REye","Nose","Mouth"])
# draw bounday on the parts of the face
def draw_boundary(img,text,color,colors):
    for i in coords:
        c=colors.get(next(color))
        x,y,w,h=i[0],i[1],i[2],i[3]
        cv2.rectangle(img, (x,y), (x+w, y+h),c, 2)
        cv2.putText(img, next(text), (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.6, c, 1, cv2.LINE_AA)
    return img
img=draw_boundary(img,text,color,colors)
cv2.imshow("show",img)
flag=0
counter=-1
# true_click()  checks if the click is on the right position
def true_click(u,v):
    global counter
    global flag
    if(counter==0):
        if(face[0]<=u and face[0]+face[2]>=u and face[1]<=v and face[1]+face[3]>=v ):
            print ("click on left  eye")
        else:
            counter=-1
            flag+=1
            print ("wrong click, restart again Click on the Face")
    elif(counter==1):
        if(coords[1][0]<=u and coords[1][0]+coords[1][2]>=u and coords[1][1]<=v and coords[1][1]+coords[1][3]>=v ):
            print ("click on right eye")
        else:
            counter=-1
            flag+=1
            print ("wrong click, restart again Click on the Face")
    elif(counter==2):
        if(coords[2][0]<=u and coords[2][0]+coords[2][2]>=u and coords[2][1]<=v and coords[2][1]+coords[2][3]>=v ):
            print ("click on nose tip")
        else:
            counter=-1
            flag+=1
            print ("wrong click, restart again Click on the Face")

    elif(counter==3):
        if(coords[3][0]<=u and coords[3][0]+coords[3][2]>=u and coords[3][1]<=v and coords[3][1]+coords[3][3]>=v ):
            print ("click on mouth")
        else:
            counter=-1
            flag+=1
            print ("wrong click, restart again Click on the Face")
    elif(counter==4):
        if(coords[4][0]<=u and coords[4][0]+coords[4][2]>=u and coords[4][1]<=v and coords[4][1]+coords[4][3]>=v ):
            print("Confirmed you are not a robot")
            counter+=1
        else:
            counter=-1
            flag+=1
            print ("wrong click,restart again Click on the Face\n Or press 1 to see all")

# mouse callback function
print("click on the face")
def mouse(event,x,y,flags,param):
    global counter
    global flag
    if event == cv2.EVENT_LBUTTONDOWN:
        counter+=1
    if event == cv2.EVENT_LBUTTONUP:
        check=true_click(x,y)
        if(flag==3):
            print("MayDay! SkyNet is Arriving Earth")
            exit(0)
        if(counter==5):
            exit(0)

cv2.namedWindow("image")
cv2.imshow('image',rahul)
cv2.setMouseCallback('image',mouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
# 1
