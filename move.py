import os
import shutil

source = "D:/Downloads"
dest = "D:/Desktop/downloaded photos"

list1 = os.listdir(source)
#print(list1)

for file in list1:
    name,ext = os.path.splitext(file)
    print(name,ext)

    if ext == "":
        continue
    list2 = ['.txt','.docx','.png','.gif','.jpg']    

    if ext == list2:
        path1 = source + "/" + file 
        path2 = dest + "/" + "image_files"
        path3 = dest + "/" + "image_files" + "/" + file

    if os.path.exists(path2):
         print("moving_files" + file)
         shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("moving_files_speacial_edition" + file)
        shutil.move(path1,path3)



