import os
import urllib.request
from Lib.gui import IDMGui

def myprint():
    print("test")
instance=IDMGui("idm")
button=instance.createButton(myprint,text="khar",width=300)
instance.setPosition(button,x=200,y=100)
input=instance.createInputField("erfan:")
instance.setPosition(input,x=100,y=200)
instance.resizeWindow()
instance.run()


# url = input("Enter Your URL: ")
# path = input("Enter Your Path: ")
# fileName = input("Enter Your File Name: ")
# fileType = input("Enter Your File Type: ")
# fullName = fileName + '.' + fileType

# print("Downloading...")
# os.chdir(path)
# urllib.request.urlretrieve(url, fullName)
# print("Downloaded succesfully in " + path + " as " + fullName)
