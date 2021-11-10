## MacApp File
## This file is used to implement code used to run scripts for Mac

import os
import time
from ErrorReport import ErrorList
from Mac import FileSystem

def Main():
   with os.scandir(FileSystem.Desktop) as FilesLocation:
      for File in FilesLocation:
         if File.is_file():
            Created = time.strftime('%d/%m/%Y', time.gmtime(os.stat(File).st_ctime))
            Modified = time.strftime('%d/%m/%Y', time.gmtime(os.path.getmtime(File)))
            
            print("="*80)
            print("File Name: ", File.name)
            print("Created: ", Created)
            print("Modified: ", Modified)
            print("="*80)
            print()

Main()
