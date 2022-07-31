#!python3
import os
import time
import subprocess
from shutil import copyfile
from shutil import rmtree
import re

#on end, rar files inside folder

currentDirectory = os.getcwd()

currentFiles = []

#change drive
os.chdir('D:')

IRFAN_VIEW = 'D:\\' + os.path.join('Files', 'apps', 'PortableApps', 'PortableApps', 'IrfanViewPortable', 'IrfanViewPortable.exe')
RAR = 'D:\\' + os.path.join('Files', 'apps', 'Winrar', 'Rar.exe')
PARENT_FOLDER =  os.path.abspath(os.path.join(currentDirectory, os.pardir))

#create temp folder
outputDir = os.path.join(currentDirectory, 'temp')

if not os.path.exists(outputDir) :
  os.makedirs(outputDir)

#count how many images will be converted
totalImages = 0
convertPending = 0

imagePattern = '.*(\.jpg|\.jpeg|\.png|\.gif)$'
dontConvertPattern = '.*(\.gif)$'

# r=>root, d=>directories, f=>files
for r, d, f in os.walk(currentDirectory) :
  for item in f:
    if re.match(imagePattern, item) :
      totalImages+=1
      if '.jpg' in item :
        convertPending+=1
      if '.jpeg' in item :
        convertPending+=1
      if '.png' in item :
        convertPending+=1
      if '.webp' in item :
        convertPending+=1

#iterate all files, and if matched, process them
# r=>root, d=>directories, f=>files
counter = 1
for r, d, f in os.walk(currentDirectory) :
  for item in f:
    if re.match(dontConvertPattern, item) :
      print("Processing " + str(counter) + '/' + str(totalImages))
      source = os.path.join(currentDirectory, item)
      target = os.path.join(outputDir, item)
      copyfile(source, target)
      counter+=1
  break

#then, convert jpg
print("Remaining " + str(convertPending) + " files will be converted")
command = ('"' + IRFAN_VIEW +'" *.jpg /convert=temp\\*.webp')
subprocess.call(command)

#then, convert jpeg
command = ('"' + IRFAN_VIEW +'" *.jpeg /convert=temp\\*.webp')
subprocess.call(command)

#then, convert png
command = ('"' + IRFAN_VIEW +'" *.png /convert=temp\\*.webp')
subprocess.call(command)

#then, convert webp
command = ('"' + IRFAN_VIEW +'" *.webp /convert=temp\\*.webp')
subprocess.call(command)

#finally, rar files
print("Compressing files")
fileName = currentDirectory.split(os.sep)[-1]
command = ('"' + RAR +'" a -ep "'+ os.path.join(PARENT_FOLDER, fileName + '.rar') + '" "' + outputDir + '"')
subprocess.call(command)

time.sleep(2)
