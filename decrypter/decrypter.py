#!python3
import os
import codecs
import time
import subprocess
from shutil import copyfile

currentDirectory = os.getcwd()

currentFiles = []

isKikiriki = False
isWolf = False
isRpgMakerOld = False

#change drive 
os.chdir('D:')

#for tyrano builder
#windows + R
#%temp%
#search for a folder like nw1234_5678

#decrypters
DECRYPTERS_FOLDER = os.path.join('Games', 'Emuladores y roms', 'emu tools', 'decrypters')

KIKIRIKI = 'D:\\' + os.path.join(DECRYPTERS_FOLDER, 'Kikiriki', 'kikiriki.exe')
RPG_MAKER_MV = 'D:\\' + os.path.join(DECRYPTERS_FOLDER, 'rpg maker', 'RPG_Maker_MV_Decrypter_jar_0.1.3.1_hotfix', 'RPG Maker MV Decrypter.jar')
RPG_MAKER_OLD = 'D:\\' + os.path.join(DECRYPTERS_FOLDER, 'rpg maker', 'RPGMakerDecrypter_1.0', 'RPGMakerDecrypter-cli.exe')
WOLF = 'D:\\' + os.path.join(DECRYPTERS_FOLDER, 'wolf', 'WolfDec.exe')
RENPY = 'D:\\' + os.path.join(DECRYPTERS_FOLDER, 'renpy', 'UnRen.bat')


if os.path.exists(os.path.join(currentDirectory, 'www')) :
  outputDir = os.path.join(currentDirectory, 'decrypted')
  if not os.path.exists(outputDir) :
    os.makedirs(outputDir)

  command = ('java -jar "' + RPG_MAKER_MV + '"' +
             ' ' + '"' + currentDirectory + '"' +
             ' ' + '"' + outputDir + '"')   
  
  print("COMMAND TO EXECUTE IS\n")
  print (command)
  subprocess.call(command)    
  print ("DECOMPILED")
elif os.path.exists(os.path.join(currentDirectory, 'renpy')) :
  #copy unren to game folder
  source = RENPY
  target = os.path.join(currentDirectory, 'UnRen.bat')
  copyfile(source, target)   
  
  command = (target)
  print("COMMAND TO EXECUTE IS\n")
  print (command)
  subprocess.call(command)
  print ("DECOMPILED")
else :
  # r=>root, d=>directories, f=>files
  for r, d, f in os.walk(currentDirectory):
    for item in f:
      if item.endswith('.xp3'):            
        isKikiriki = True
        currentFiles.append(os.path.join(item))      
      elif item.endswith('.wolf'):
        isWolf = True
        currentFiles.append(os.path.join(item))
      elif item.endswith('.rgssad'):
        isRpgMakerOld = True
        currentFiles.append(os.path.join(item))
      elif item.endswith('.rgss2a'):
        isRpgMakerOld = True
        currentFiles.append(os.path.join(item))  
      elif item.endswith('.rgss3a'):
        isRpgMakerOld = True
        currentFiles.append(os.path.join(item))        

  if isKikiriki:
    print("KIKIRIKI DETECTED\n")
    for file in currentFiles :
      outputDir = 'dec_' + file.rsplit('.', 1)[0]
      command = ('"' + KIKIRIKI + '"' +
                 ' -i ' + '"' + os.path.join(currentDirectory, file) + '"' +
                 ' -o ' + '"' + os.path.join(currentDirectory, outputDir) + '"')
      print("COMMAND TO EXECUTE IS\n")
      print (command)
      subprocess.call(command)    
      print ("DECOMPILED")
      
  elif isWolf :    
    print("WOLF DETECTED\n")
    files = []       
    
    for file in currentFiles :               
      files.append('"' + os.path.join(currentDirectory, file) + '"')

    command = ('"' + WOLF + '" ' + " ".join(files))
    print("COMMAND TO EXECUTE IS\n")
    print (command)
    subprocess.call(command)    
    print ("DECOMPILED")
    
  elif isRpgMakerOld :    
    print("RPG MAKER OLD DETECTED\n")    
    
    outputDir = os.path.join(currentDirectory, 'decrypted')
    
    for file in currentFiles :               
      currentFile = '"' + os.path.join(currentDirectory, file) + '"'

      command = ('"' + RPG_MAKER_OLD + '" ' + currentFile + ' --output="' + outputDir + '"')
      print("COMMAND TO EXECUTE IS\n")
      print (command)
      subprocess.call(command)    
      print ("DECOMPILED")  
    
time.sleep(2)