#import os
#import re

# Removes duplicate files by file name per directory

def remove_duplicates(directory):
    
  for root, dirs, files in os.walk(directory):
      filedict = {}
      
      for file in files:
          file = os.path.join(root, file)
          
          # check for duplicates 
          match = re.search(r'^(.*?)\((\d+)\)(\.[^.]*)?$', filename)
          
          if match:
              name = match.group(1)
              number = int(match.group(2))
              ext = match.group(3) or ''
              
              if name not in filedict:
                  filedict[name] = [(number, file, ext)]
              else:
                  filedict[name].append((number, file, ext))
                
        for name in filedict:
            files = filedict[name]
            
            files.sort(key=lamba x: x[0])
            
            print(files)
            
            latest = files[-1][1]
            ext = files[-1][2]
            
            for number, filepath, _ in files[:-1]:
                print(f"Deleted duplicate file: {filepath}")
                os.remove(filepath)
            
            os.rename(latest, os.path.join(root, f"{name}{ext}"))
            print(f"Renamed {latest} to {name}{ext})
            
    

def prompt_user():
    subfolders = [ f.name for f in os.scandir(folder) if f.is_dir() ]
    
    print("WARNING: This script deletes duplicate files. Files may be deleted.")
    input("Press the Enter key to continue.")
    
    print(" ")
    
    print(subfolders)
    
    directory = input("From which directory would you like to delete duplicate files?")
    
    return directory


if __name__ == '__main__':
    
    directory = prompt_user()
    remove_duplicates(os.path.expanduser(f"{os.getcwd()/{}}"))
              
              
