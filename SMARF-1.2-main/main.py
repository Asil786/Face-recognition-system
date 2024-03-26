import cv2
import numpy as np
import face_recognition
from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import pandas as pd
import matplotlib.pyplot as plt

# Opening the images from the specified dir.
'''
img_m=face_recognition.load_image_file('ImagesBasic/thor_m.jpg')
img_m=cv2.cvtColor(img_m,cv2.COLOR_BGR2RGB)
img_t=face_recognition.load_image_file('ImagesBasic/thor_test.jpg')
img_t=cv2.cvtColor(img_t,cv2.COLOR_BGR2RGB)


# dectecting the faces from the images
faceloc=face_recognition.face_locations(img_m)[0]
encode_m=face_recognition.face_encodings(img_m)[0]
cv2.rectangle(img_m,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)


faceloct=face_recognition.face_locations(img_t)[0]
encode_t=face_recognition.face_encodings(img_t)[0]
cv2.rectangle(img_t,(faceloct[3],faceloct[0]),(faceloct[1],faceloct[2]),(255,0,255),2)


# find face distances

results=face_recognition.compare_faces([encode_m],encode_t)
dis=face_recognition.face_distance([encode_m],encode_t)
print(results,dis)
cv2.putText(img_t,f'{results} {round(dis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)



cv2.imshow("mohd mustufa",img_m)
cv2.imshow("mohd mustufa test",img_t)


cv2.waitKey(0)'''



Window.size = (500,500)

class cameraApp(App):
    def build(self):
        global cam
        cam = Camera()
        global txt
        txt = TextInput(text="Enter the name",size_hint_y=(.1,.8))

        btn = Button(text="Open WebCam",size_hint=(.1,.1),font_size=35,background_color = 'blue',on_press=self.capture)

        layout = GridLayout(rows = 3,cols=1)

        layout.add_widget(cam)
        layout.add_widget(btn)
        layout .add_widget(txt)
        return layout
    def capture(self,*args):
        global cam
        cam.export_to_png('{}.png'.format(txt))
        print("Image Captured and saved in current working directory ")


if __name__ == '__main__':
    cameraApp().run()







