import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import pandas as pd


root = Tk()
root.geometry("600x400")
root.title("ML Based Smart Recognition System")
root.config(bg="black")
l1=Label(root,text="Enter Your name")
l1.place(x=10, y=180,width=200,height=40)

img_name = Entry(root)
img_name.place(x=160, y=180,width=200,height=40)


l2=Label(root,text="Enter Your Roll-No")
l2.place(x=10, y=210,width=200,height=40)

img_roll  = Entry(root)
img_roll.place(x=160,y=210,width=200,height=40)
def click():
    hello = img_name.get()
    roll = img_roll.get()
    cam = cv2.VideoCapture(0)
    #cv2.namedWindow("MHSSP Smart Attendance System")
    img_c = 0
    while True:

        ret, frame = cam.read()
        # cv2.imshow("Frame",frame)
        if not ret:
            print("Faolded")
        cv2.imshow("tesr", frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        elif key % 256 == 32:
            img_res = str(hello)+"_"+str(roll) + ".jpg"
            cv2.resize(frame, (250, 200))
            cv2.imwrite("./ImagesBasic/"+img_res, frame)
            # print("ScreenShot Taken")
            messagebox.showinfo("Registeration Info", "Registeration Successfull of the Student " + str(hello))


            img_c += 1

    cam.release()
    cam.destroyAllWindows()


l1 = Label(root, text="Welcome you are In MHSSP Smart Attendance System", font=("Impact",19), fg="white",bg="black")
l1.grid(row=1,column=1)

btn = Button(root, text="Register Student", fg="white", bg="green", command=click,font=("times new roman",15))
btn.place(x=250,y=270,width=140,height=70)







































def att():



    path = 'ImagesBasic'
    images = []
    className = []
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        className.append(os.path.splitext(cl)[0])
    print(className)



    def findencodings(images):
        encodelist = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodelist.append(encode)
        return encodelist
    def markattend(name):
        with open('Attendance.csv','r+') as f:
            mydataList = f.readline()
            namelist = []
            for line in mydataList:
                entry = line.split(',')
                namelist.append(entry[0])
            if name not in namelist:
                now = datetime.now()
                dateString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dateString}')
                data = pd.read_csv("Attendance.csv")
                data.drop_duplicates(subset="Name", keep="first", inplace=True)
                df = data
                df.to_csv("output.csv")





    encodelistknown = findencodings(images)
    print("Encoding Completed !!!")

    cap = cv2.VideoCapture(0)
    while True:
        success,img = cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        faceCur = face_recognition.face_locations(imgS)
        encodeCur = face_recognition.face_encodings(imgS,faceCur)

        for encodeFace,faceloc in zip(encodeCur,faceCur):
            matches = face_recognition.compare_faces(encodelistknown,encodeFace)
            faceDis = face_recognition.face_distance(encodelistknown,encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = className[matchIndex].upper()
                
                #print(name)
                y1,x2,y2,x1 = faceloc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                markattend(name)
            else:
                name = className[matchIndex].upper()
                # print(name)
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('webcam',img)
        k = cv2.waitKey(1)
        if k == 27:
            break
        #if k == ord("q"):
         #   break



btn=Button(root,text="Take Attendance",command=att,bg="Red",fg="white",font=("times new roman",15)).place(x=70,y=270,width=140,height=70)

root.mainloop()
