import os
import urllib.request

url = input("Enter Your URL: ")
path = input("Enter Your Path: ")
fileName = input("Enter Your File Name: ")
fileType = input("Enter Your File Type: ")
fullName = fileName + '.' + fileType

print("Downloading...")
os.chdir(path)
urllib.request.urlretrieve(url, fullName)
print("Downloaded succesfully in " + path + " as " + fullName)
