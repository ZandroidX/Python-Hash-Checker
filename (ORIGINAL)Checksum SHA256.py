import hashlib
import sys
import os
from tkinter import filedialog
import tkinter as tk
#from progress.bar import Bar

hashTypes = ['sha256' , 'md5', 'sha1']

sysPath = sys.path[0]

root = tk.Tk()
root.withdraw()

filePath = filedialog.askopenfilename(initialdir = "~/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

root.update()

fileSize = os.path.getsize(filePath)
print("\nfile is: " + str(fileSize) + " bytes")
root.wm_deiconify()
root.grid_location(200, 300)

def SHA256(filePath):
   """"This function returns the SHA-1 hash
   of the file passed into it"""
   print("Processing SHA256...")

   # make a hash object
   h = hashlib.sha256()

   # open file for reading in binary mode
   with open(filePath,'rb') as file:

       # loop till the end of the file
      chunk = 0
      iteration = 0
      onePercent = fileSize / 100
      while chunk != b'':
           if iteration == onePercent:
              print(iteration)
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           #every 1024 bytes
           iteration += 1024
           h.update(chunk)
   # return the hex representation of digest
   return h.hexdigest()



def MD5(filePath):
   print("processing MD5...")

   h = hashlib.md5()

   with open(filePath, 'rb') as file:

      chunk = 0

      while chunk != b'':

         chunk = file.read(1024)
         h.update(chunk)

      return h.hexdigest()


def SHA1(filePath):
   print("SHA1 processing")

   h = hashlib.sha1()

   with open(filePath, 'rb') as file:

      chunk = 0

      while chunk != b'':

         chunk = file.read(1024)
         h.update(chunk)

      return h.hexdigest()


fileType = input("specify checksum type: " + "(md5, sha1, sha256)" + "\n")

if fileType.lower() == "md5":
    message = MD5(filePath)
    print("MD5:\n" + message + "\n")
elif fileType.lower() == "sha256":
    message = SHA256(filePath)
    print("SHA256:\n" + message + "\n")
elif fileType.lower() == "sha1":
    message = SHA1(filePath)
    print("SHA1:\n" + message + "\n")

elif fileType.lower() not in hashTypes:
    print("Invalid file type \n\n")