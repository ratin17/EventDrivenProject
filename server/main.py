# author : Mehrab Rabbi Ratin
#  e-mail: ratin.cse@gmail.com

#  for phitron lab assignment 2


import glob
import shutil
import os

source_path = '..\source\*'
dest_path = '..\destination\\'
b='\\'
postfix = [1,2,3]
srcPath='..\source\\'


while True:

    source_object = glob.glob(source_path)
    
    #iterating all the files in source folder
    for obj in range(len(source_object)):
        object_path = source_object[obj]
        
        #getting the file name
        object_name = object_path.split(b)[-1].split('.')
        pre = object_name[-2]
        post = object_name[-1]
        
        #managing the text files
        if post=="txt":

            #getting the file in server directory
            shutil.copy(object_path, '.')

            f=open(object_path,"r")
            lines=f.readlines() #saving all the lines 
            f.close()

            os.remove(f'{srcPath}{pre}.{post}')

            zipPath='.\zipFolder'
            os.mkdir(zipPath) # making folder for zipping
            for item in postfix:
                filename = pre + '_' + str(item) + '.' + post
                print(f'\nCoppying {filename} with {item*10} lines from {pre}.{post}\n')
                shutil.copy(f".\{pre}.{post}", f"{zipPath}\{filename}")

                f=open(f"{zipPath}\{filename}","w")
                f.write("")  #making the file empty
                f.close()

                f=open(f"{zipPath}\{filename}","a")
                for line in range(0,item*10): 
                    f.write(lines[line])
                f.close()
            
            
            #zipping the folder with files
            shutil.make_archive(f'{dest_path}{pre}', format='zip', root_dir=zipPath)
            shutil.rmtree(zipPath) # delete the folder after makig zip

            os.remove(f".\{pre}.{post}") #deleting file copied from source

            shutil.unpack_archive(f'{dest_path}{pre}.zip',dest_path)
            os.remove(f'{dest_path}{pre}.zip')

        if post=="py":

            print(f"\nExecuting in {srcPath}{pre}.{post}")
            print("|''''''''''''''''''''''''''''''''''''''|\n")
            try:
                exec(open(f'{srcPath}{pre}.{post}').read())
            except:
                print(f"\nSome error occured in {srcPath}{pre}.{post}\n")

            print("\n|______________________________________|\n")

            os.remove(f'{srcPath}{pre}.{post}')
            




