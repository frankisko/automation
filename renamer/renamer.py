#!python3
import os
import time
import subprocess
from shutil import copyfile
from shutil import rmtree
import re

current_directory = os.getcwd()
file_prefix = os.path.basename(current_directory)

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

# r=>root, d=>directories, f=>files
i = 1;
for r, d, f in os.walk(current_directory) :    
  for item in natural_sort(f):    
    if item != "renamer.bat":
      root, extension = os.path.splitext(item)      
    
      old_file_name = os.path.join(current_directory, item)
      new_file_name = os.path.join(current_directory, file_prefix + " - " + str(i).rjust(2, '0') + extension)

      #print(old_file_name)
      #print(new_file_name)
      i+=1
      os.rename(old_file_name, new_file_name)      
      #print(item)

time.sleep(2)