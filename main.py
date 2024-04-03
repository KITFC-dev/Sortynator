# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Version 1 (First Alpha)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Imports
import os
import shutil
import sys
import time
import webbrowser
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Function for .jpeg / .jpg / .png / .gif


def collectorimage(path, res_path):
    res_path = os.path.normpath(path)
    path = os.path.normpath(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file.lower().endswith('.jpeg') or file.lower().endswith('.jpg') or file.lower().endswith('.png') or file.lower().endswith('.bmp') or file.lower().endswith('.tiff') or file.lower().endswith('.webp') or file.lower().endswith('.jfif'):
                file_path = os.path.join(dirpath, file)
                nameimage = "Images"
                destination_dir = os.path.join(res_path, nameimage)

                if os.path.isdir(destination_dir): # якщо існує значить переносить файл
                    os.replace(file_path, os.path.join(destination_dir, file))
                    print(f"!! Folder {nameimage} is already created")
                else: # якщо папка не існує = створити
                    os.makedirs(destination_dir, exist_ok=True)
                    os.replace(file_path, os.path.join(destination_dir, file))
                    print(f"// Folder {nameimage} created")
                # Move files to the subfolder
                for filename in os.listdir(path):
                    if filename.lower().endswith('.gif'):
                        # Create folder if .gif exists
                        sub_folder_namegif = "GIFs"
                        sub_folder_pathgif = os.path.join(destination_dir, sub_folder_namegif)
                        if not os.path.exists(sub_folder_pathgif):
                            os.makedirs(sub_folder_pathgif)
                            print(f"> Subfolder {sub_folder_namegif} created")
                        else:
                            print(f"! SubFolder {sub_folder_namegif} is already created")
                        src = os.path.join(path, filename)
                        dst = os.path.join(sub_folder_pathgif, filename)
                        shutil.move(src, dst)
                # Move files to the subfolder
                for filename in os.listdir(path):
                    if filename.lower().endswith('.ico'):
                        # Create folder if .ico exists
                        sub_folder_nameico = "ICOs"
                        sub_folder_pathico = os.path.join(destination_dir, sub_folder_nameico)
                        if not os.path.exists(sub_folder_pathico):
                            os.makedirs(sub_folder_pathico)
                            print(f"> Subfolder {sub_folder_nameico} created")
                        else:
                            print(f"! SubFolder {sub_folder_nameico} is already created")
                        src = os.path.join(path, filename)
                        dst = os.path.join(sub_folder_pathico, filename)
                        shutil.move(src, dst)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Function for .mp4 / .avi / .wmv
def collectorvideo(path, res_path):
    res_path = os.path.normpath(path)
    path = os.path.normpath(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file.lower().endswith('.mp4') or file.lower().endswith('.avi') or file.lower().endswith('.wmv') or file.lower().endswith('.webm'):
                file_path = os.path.join(dirpath, file)
                namevideo = "Videos"
                destination_dir = os.path.join(res_path, namevideo)

                if os.path.isdir(destination_dir): # якщо існує значить переносить файл
                    os.replace(file_path, os.path.join(destination_dir, file))
                    print(f"!! Folder {namevideo} is already created")
                else: # якщо папка не існує = створити
                    os.makedirs(destination_dir, exist_ok=True)
                    os.replace(file_path, os.path.join(destination_dir, file))
                    print(f"// Folder {namevideo} created")
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Function for 3d
def collector3d(path, res_path):
    res_path = os.path.normpath(path)
    path = os.path.normpath(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file.lower().endswith('.stl') or file.lower().endswith('.obj') or file.lower().endswith('.fbx') or file.lower().endswith('.ply') or file.lower().endswith('.3ds') or file.lower().endswith('.iges') or file.lower().endswith('.step') or file.lower().endswith('.dxf') or file.lower().endswith('.amf') or file.lower().endswith('.blend') or file.lower().endswith('.blend1') or file.lower().endswith('.blend2') or file.lower().endswith('.dae'):
                file_path = os.path.join(dirpath, file)
                name3d = "3D Objects"
                destination_dir = os.path.join(res_path, name3d)

                if os.path.isdir(destination_dir): # якщо існує значить переносить файл
                    os.replace(file_path, os.path.join(destination_dir, file))
                    print(f"!! Folder {name3d} is already created")
                else: # якщо папка не існує = створити
                    os.makedirs(destination_dir, exist_ok=True)
                    os.replace(file_path, os.path.join(destination_dir, file))
                    print(f"// Folder {name3d} created")
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Function for .veg
def collectorvegas(path, res_path):
    res_path = os.path.normpath(path)
    path = os.path.normpath(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file.lower().endswith('.veg'):
                file_path = os.path.join(dirpath, file)
                namev = "Vegas Pro"
                destination_dir = os.path.join(res_path, namev)

                if os.path.isdir(destination_dir): # якщо існує значить переносить файл
                    os.replace(file_path, os.path.join(destination_dir, file))
                    print(f"!! Folder {namev} is already created")
                else: # якщо папка не існує = створити
                    os.makedirs(destination_dir, exist_ok=True)
                    os.replace(file_path, os.path.join(destination_dir, file))
                    print(f"// Folder {namev} created")
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN
path = input("Enter Path: ")
print("Sortynator will sort supported files to folders")
print("THIS IS BETA VERSION !! USE ON YOUR OWN RISK !!")
print("Press 'ENTER' to continue...")
input()
res_path = path
path_doc = os.path.join(path, "Documents")
if not os.path.exists(path):
    print("Path not found. Enter valid path (Example: D:\yourfolder\downloads)")
    input("Press 'ENTER' to continue...")
    sys.exit()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Collector Functions
collectorimage(path, res_path) #IMAGE
collectorvideo(path, res_path) #VIDEO
collector3d(path, res_path)    #3D
collectorvegas(path, res_path)
time.sleep(0.5)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Documents
# Create the Document folder
main_folder_name = "Documents"
main_folder_path = os.path.join(path, main_folder_name)
if not os.path.exists(main_folder_path):
    os.makedirs(main_folder_path)
    print("// Folder 'Documents' created")
else:
    print("!! Folder 'Documents' is already created")

# Move files to the subfolder
for filename in os.listdir(path):
    if filename.lower().endswith('.pdf'):
        # Create a Subfolders within the Document folder
        sub_folder_namep = "PDFs"
        sub_folder_pathp = os.path.join(main_folder_path, sub_folder_namep)
        if not os.path.exists(sub_folder_pathp):
            os.makedirs(sub_folder_pathp)
            print("> Subfolder 'DPFs' created")
        else:
            print("! SubFolder 'PDFs' is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathp, filename)
        shutil.move(src, dst)

for filename in os.listdir(path):
    if filename.lower().endswith('.txt'):
        # Move files to the subfolder
        sub_folder_namet = "TXTs"
        sub_folder_patht = os.path.join(main_folder_path, sub_folder_namet)
        if not os.path.exists(sub_folder_patht):
            os.makedirs(sub_folder_patht)
            print("> Subfolder 'TXTs' created")
        else:
            print("! SubFolder 'TXTs' is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_patht, filename)
        shutil.move(src, dst)

for filename in os.listdir(path):
    if filename.lower().endswith('.doc') or filename.lower().endswith('.docx') or filename.lower().endswith('.rtf'):
        # Move files to the subfolder
        sub_folder_namew = "Word Files"
        sub_folder_pathw = os.path.join(main_folder_path, sub_folder_namew)
        if not os.path.exists(sub_folder_pathw):
            os.makedirs(sub_folder_pathw)
            print("> Subfolder 'Word Files' created")
        else:
            print("! SubFolder 'Word Files' is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathw, filename)
        shutil.move(src, dst)

for filename in os.listdir(path):
    if filename.lower().endswith('.xls') or filename.lower().endswith('.xlsx'):
        # Move files to the subfolder
        sub_folder_namee = "Excels"
        sub_folder_pathe = os.path.join(main_folder_path, sub_folder_namee)
        if not os.path.exists(sub_folder_pathe):
            os.makedirs(sub_folder_pathe)
            print("> Subfolder 'Excels' created")
        else:
            print("! SubFolder 'Excels' is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathe, filename)
        shutil.move(src, dst)

for filename in os.listdir(path):
    if filename.lower().endswith('.ppt') or filename.lower().endswith('.pptx'):
        # Move files to the subfolder
        sub_folder_namepp = "PowerPoint"
        sub_folder_pathpp = os.path.join(main_folder_path, sub_folder_namepp)
        if not os.path.exists(sub_folder_pathpp):
            os.makedirs(sub_folder_pathpp)
            print("> Subfolder 'PowerPoint' created")
        else:
            print("! SubFolder 'PowerPoint' is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathpp, filename)
        shutil.move(src, dst)
time.sleep(0.1)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Adobe Cloud
# Create the Adobe folder
main_folder_name = "Adobe Cloud"
main_folder_path = os.path.join(path, main_folder_name)
if not os.path.exists(main_folder_path):
    os.makedirs(main_folder_path)
    print(f"// Folder {main_folder_name} created")
else:
    print(f"!! Folder {main_folder_name} is already created")

# Move files to the subfolder
# Photoshop
for filename in os.listdir(path):
    if filename.lower().endswith('.psd'):
        # Create a Subfolders within the Adobe Cloud folder
        sub_folder_namep = "Photoshop"
        sub_folder_pathp = os.path.join(main_folder_path, sub_folder_namep)
        if not os.path.exists(sub_folder_pathp):
            os.makedirs(sub_folder_pathp)
            print(f"> Subfolder {sub_folder_namep} created")
        else:
            print(f"! SubFolder {sub_folder_namep} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathp, filename)
        shutil.move(src, dst)
# Illustrator
for filename in os.listdir(path):
    if filename.lower().endswith('.ai'):
        sub_folder_namei = "Illustrator"
        sub_folder_pathi = os.path.join(main_folder_path, sub_folder_namei)
        if not os.path.exists(sub_folder_pathi):
            os.makedirs(sub_folder_pathi)
            print(f"> Subfolder {sub_folder_namei} created")
        else:
            print(f"! SubFolder {sub_folder_namei} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathi, filename)
        shutil.move(src, dst)
# InDesign
for filename in os.listdir(path):
    if filename.lower().endswith('.indd') or filename.lower().endswith('.idml'):
        sub_folder_nameid = "InDesign"
        sub_folder_pathid = os.path.join(main_folder_path, sub_folder_nameid)
        if not os.path.exists(sub_folder_pathid):
            os.makedirs(sub_folder_pathid)
            print(f"> Subfolder {sub_folder_nameid} created")
        else:
            print(f"! SubFolder {sub_folder_nameid} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathid, filename)
        shutil.move(src, dst)
# Premiere Pro
for filename in os.listdir(path):
    if filename.lower().endswith('.prproj'):
        sub_folder_namepp = "Premiere Pro"
        sub_folder_pathpp = os.path.join(main_folder_path, sub_folder_namepp)
        if not os.path.exists(sub_folder_pathpp):
            os.makedirs(sub_folder_pathpp)
            print(f"> Subfolder {sub_folder_namepp} created")
        else:
            print(f"! SubFolder {sub_folder_namepp} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathpp, filename)
        shutil.move(src, dst)
# After Effects
for filename in os.listdir(path):
    if filename.lower().endswith('.aep') or filename.lower().endswith('.aepx'):
        sub_folder_nameae = "After Effects"
        sub_folder_pathae = os.path.join(main_folder_path, sub_folder_nameae)
        if not os.path.exists(sub_folder_pathae):
            os.makedirs(sub_folder_pathae)
            print(f"> Subfolder {sub_folder_nameae} created")
        else:
            print(f"! SubFolder {sub_folder_nameae} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathae, filename)
        shutil.move(src, dst)
# Flash
for filename in os.listdir(path):
    if filename.lower().endswith('.fla') or filename.lower().endswith('.swf'):
        sub_folder_namef = "Flash"
        sub_folder_pathf = os.path.join(main_folder_path, sub_folder_namef)
        if not os.path.exists(sub_folder_pathf):
            os.makedirs(sub_folder_pathf)
            print(f"> Subfolder {sub_folder_namef} created")
        else:
            print(f"! SubFolder {sub_folder_namef} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathf, filename)
        shutil.move(src, dst)
time.sleep(0.2)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Move files to the Archives folder
# Photoshop
# (.zip, .rar, .7z, .tar, .gz, bz2, .xz,)
for filename in os.listdir(path):
    if filename.lower().endswith('.zip') or filename.lower().endswith('.rar') or filename.lower().endswith('.7z') or filename.lower().endswith('.tar') or filename.lower().endswith('.gz') or filename.lower().endswith('.bz2') or filename.lower().endswith('.xz'):
        # Adobe Cloud
        # Create the Adobe folder
        main_folder_name = "Archives"
        main_folder_path = os.path.join(path, main_folder_name)
        if not os.path.exists(main_folder_path):
            os.makedirs(main_folder_path)
            print(f"// Folder {main_folder_name} created")
        else:
            print(f"!! Folder {main_folder_name} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(main_folder_path, filename)
        shutil.move(src, dst)
time.sleep(0.1)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Move files to the Music folder
# Music
# (add music, wav,)
for filename in os.listdir(path):
    if filename.lower().endswith('.mp3') or filename.lower().endswith('.wav') or filename.lower().endswith('.aac') or filename.lower().endswith('.flac') or filename.lower().endswith('.ogg') or filename.lower().endswith('.wma') or filename.lower().endswith('.ape'):
        # Adobe Cloud
        # Create the Adobe folder
        main_folder_name = "Music"
        main_folder_path = os.path.join(path, main_folder_name)
        if not os.path.exists(main_folder_path):
            os.makedirs(main_folder_path)
            print(f"// Folder {main_folder_name} created")
        else:
            print(f"!! Folder {main_folder_name} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(main_folder_path, filename)
        shutil.move(src, dst)
        for filename in os.listdir(path):
            if filename.lower().endswith('.mid') or filename.lower().endswith('.midi'):
                sub_folder_namemidi = "MIDIs"
                sub_folder_pathmidi = os.path.join(main_folder_path, sub_folder_namemidi)
                if not os.path.exists(sub_folder_pathmidi):
                    os.makedirs(sub_folder_pathmidi)
                    print(f"> Subfolder {sub_folder_namemidi} created")
                else:
                    print(f"! SubFolder {sub_folder_namemidi} is already created")
                    src = os.path.join(path, filename)
                    dst = os.path.join(sub_folder_pathmidi, filename)
                    shutil.move(src, dst)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# [".js", ".py", ".java", ".class", ".cs", ".cpp", ".h", ".ts", ".php", ".swift", ".sql", ".r"]
# Create the Dev files folder
time.sleep(0.1)
main_folder_name = "Dev files"
main_folder_path = os.path.join(path, main_folder_name)
if not os.path.exists(main_folder_path):
    os.makedirs(main_folder_path)
    print(f"// Folder {main_folder_name} created")
else:
    print(f"!! Folder {main_folder_name} is already created")

# Move files to the subfolder
# BAT
for filename in os.listdir(path):
    if filename.lower().endswith('.bat'):
        # Create a Subfolders within the Adobe Cloud folder
        sub_folder_name1 = "BATs"
        sub_folder_path1 = os.path.join(main_folder_path, sub_folder_name1)
        if not os.path.exists(sub_folder_path1):
            os.makedirs(sub_folder_path1)
            print(f"> Subfolder {sub_folder_name1} created")
        else:
            print(f"! SubFolder {sub_folder_name1} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_path1, filename)
        shutil.move(src, dst)
# Python
for filename in os.listdir(path):
    if filename.lower().endswith('.py'):
        sub_folder_namep = "Python"
        sub_folder_pathp = os.path.join(main_folder_path, sub_folder_namep)
        if not os.path.exists(sub_folder_pathp):
            os.makedirs(sub_folder_pathp)
            print(f"> Subfolder {sub_folder_namep} created")
        else:
            print(f"! SubFolder {sub_folder_namep} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathp, filename)
        shutil.move(src, dst)
# Java Script
for filename in os.listdir(path):
    if filename.lower().endswith('.js'):
        sub_folder_namei = "Java Script"
        sub_folder_pathi = os.path.join(main_folder_path, sub_folder_namei)
        if not os.path.exists(sub_folder_pathi):
            os.makedirs(sub_folder_pathi)
            print(f"> Subfolder {sub_folder_namei} created")
        else:
            print(f"! SubFolder {sub_folder_namei} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathi, filename)
        shutil.move(src, dst)
# JAVA
for filename in os.listdir(path):
    if filename.lower().endswith('.java') or filename.lower().endswith('.jar'):
        sub_folder_nameid = "Java"
        sub_folder_pathid = os.path.join(main_folder_path, sub_folder_nameid)
        if not os.path.exists(sub_folder_pathid):
            os.makedirs(sub_folder_pathid)
            print(f"> Subfolder {sub_folder_nameid} created")
        else:
            print(f"! SubFolder {sub_folder_nameid} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathid, filename)
        shutil.move(src, dst)
# C#
for filename in os.listdir(path):
    if filename.lower().endswith('.cs'):
        sub_folder_namepp = "C#"
        sub_folder_pathpp = os.path.join(main_folder_path, sub_folder_namepp)
        if not os.path.exists(sub_folder_pathpp):
            os.makedirs(sub_folder_pathpp)
            print(f"> Subfolder {sub_folder_namepp} created")
        else:
            print(f"! SubFolder {sub_folder_namepp} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathpp, filename)
        shutil.move(src, dst)
# C++
for filename in os.listdir(path):
    if filename.lower().endswith('.cpp'):
        sub_folder_nameae = "C++"
        sub_folder_pathae = os.path.join(main_folder_path, sub_folder_nameae)
        if not os.path.exists(sub_folder_pathae):
            os.makedirs(sub_folder_pathae)
            print(f"> Subfolder {sub_folder_nameae} created")
        else:
            print(f"! SubFolder {sub_folder_nameae} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathae, filename)
        shutil.move(src, dst)
# TypeScript
for filename in os.listdir(path):
    if filename.lower().endswith('.ts'):
        sub_folder_nameg = "TypeScript"
        sub_folder_pathg = os.path.join(main_folder_path, sub_folder_nameg)
        if not os.path.exists(sub_folder_pathg):
            os.makedirs(sub_folder_pathg)
            print(f"> Subfolder {sub_folder_nameg} created")
        else:
            print(f"! SubFolder {sub_folder_nameg} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathg, filename)
        shutil.move(src, dst)

# PHP
for filename in os.listdir(path):
    if filename.lower().endswith('.php'):
        sub_folder_namef = "PHP"
        sub_folder_pathf = os.path.join(main_folder_path, sub_folder_namef)
        if not os.path.exists(sub_folder_pathf):
            os.makedirs(sub_folder_pathf)
            print(f"> Subfolder {sub_folder_namef} created")
        else:
            print(f"! SubFolder {sub_folder_namef} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathf, filename)
        shutil.move(src, dst)

# JSON
for filename in os.listdir(path):
    if filename.lower().endswith('.json'):
        sub_folder_namej = "JSON"
        sub_folder_pathj = os.path.join(main_folder_path, sub_folder_namej)
        if not os.path.exists(sub_folder_pathj):
            os.makedirs(sub_folder_pathj)
            print(f"> Subfolder {sub_folder_namej} created")
        else:
            print(f"! SubFolder {sub_folder_namej} is already created")
        src = os.path.join(path, filename)
        dst = os.path.join(sub_folder_pathj, filename)
        shutil.move(src, dst)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# END
time.sleep(2)
print('\n' * 99)
print(f"files was sorted, you can close app now\nTHANK YOU FOR USING SORTYNATOR")
print(f"\nthis is beta version,\nplease report any bugs/possible improvements")
print("\n"*2)
while True:
    end_input = input("You can choose one of the following:\n'credits','github'\n(contact via GitHub email)\n").lower()
    if end_input == "c" or end_input == "credits":
        print('\n' * 99)
        print("Credits:"
              "\nCode: @KITFC-dev (GitHub)"
              "\nTester: @KITFC-dev (GitHub)")
    elif end_input == "gh" or end_input == "github" or end_input == "g":
        print('\n' * 99)
        print("GitHub: https://github.com/KITFC-dev")
        time.sleep(1.7)
        git_hub_url = "https://github.com/KITFC-dev"
        webbrowser.open(git_hub_url)
    else:
        print("not valid command, you can close app now")
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Notes
#
#
#