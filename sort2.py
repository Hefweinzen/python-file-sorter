import os
import shutil

'''
objective: figure out how to get it to run everywhere
'''

path = input("Enter Downloads path:")
file_name = os.listdir(path)

destination = input("Enter Sorted Destination:")


folder_name = ["Apps", "Code", "Images", "Sounds", "Text", "Videos", "zMisc"]

#list of common file endings
applications = [".exe",".lnk"] 
codes = [".c",".py",".java",".cpp",".js",".html",".css",".php", ".R"]
images = [".jpeg",".png",".jpg",".gif", ".webp"]
sounds = [".mp3",".wav",".m4a"]
text = [".doc",".txt",".pdf",".xlsx",".docx",".xls",".rtf"]
videos = [".mp4",".mkv", ".mov", ".avi", ".wmv"]

#makes folders in destination to sort to
for folder in folder_name:
    if not os.path.exists(destination + "/" + folder):
        os.mkdir(destination + folder)
        print(folder + " folder has been created \n")

#sorts the files
for file in file_name:
    misc = True

    for ex in applications:
        if file.endswith(ex):
            shutil.move(path + file, destination + "Apps/" + file)
            misc = False

    for ex in codes:
        if file.endswith(ex):
            shutil.move(path + file, destination + "Code/" + file)
            misc = False

    for ex in images:
        if file.endswith(ex):
            shutil.move(path + file, destination + "Images/" + file)
            misc = False

    for ex in sounds:
        if file.endswith(ex):
            shutil.move(path + file, destination + "Sounds/" + file)
            misc = False

    for ex in text:
        if file.endswith(ex):
            shutil.move(path + file, destination + "Text/" + file)
            misc = False

    for ex in videos:
        if file.endswith(ex):
            shutil.move(path + file, destination + "Videos/" + file)
            misc = False

    if misc == True:
        shutil.move(path + file, destination + "zMisc/" + file)

    print(file + " has been moved\n")

print("success")