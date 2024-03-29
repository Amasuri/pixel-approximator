#python 2.7.13
from __future__ import print_function

#-------------------------------------------------

import sys, os, time
if sys.version_info[0] > 2:
  print("Python 2 only!")
  sys.exit(1)

#--------------------------------------------------

import check_pixel as chkpix
import PIL as pil
from PIL import Image

#-------------------------------------------------

print("Change the pallette of file to an approx from pallette.png")
print("Works on every .png file in directory.")
print("Press enter...")
raw_input()

print("\nInput magnitude of difference number (you'd want either 1 or 5, but feel free to experiment! Some things are looking better after magnitude of 1, but others are after magnitude 5!\n")
inputMag = raw_input()
if(inputMag.isdigit()):
    chkpix._MAGNITUDE = int(inputMag)

print("\nsearching pallette file...")
pallette_file = Image.open("pallette.png").convert('RGBA')
width, height = pallette_file.size

print("\nconstructing a pallette color list...")
pallette_colors = []
for x in range(width):
    for y in range(height):
        pixel = pallette_file.getpixel((x, y))
        if pixel not in pallette_colors:
            pallette_colors.append(pixel)

print("\ncompiling palette values...")
chkpix.compile_palette(pallette_colors)


print("\nloading source files..")
default_dir = os.getcwd()
os.chdir(default_dir + "\Source")
source_files = {}
for filename in os.listdir("."):
    if filename.endswith('.png'):
        source_files[filename] = Image.open(filename)


print("\napproximating...\n")
os.chdir(default_dir + "\Result")
total_time = 0.0
for file in source_files.keys():
    start_time = time.time()

    print("file: " + file, end = " ")
    width, height = source_files[file].size

    #create pixmap
    pMap = source_files[file].load()

    #run the script to change pixels to those of the pallette
    for x in range(width):
        for y in range(height):
            pMap[x, y] = chkpix.find_approximate(pMap[x, y])

    source_files[file].save(file)
    end_time = time.time()
    total_time += end_time - start_time
    print(str(round(end_time - start_time, 2)) + " seconds")
    pass


print("\ntotal time: " + str(round(total_time, 2)) + " seconds")
print("\ndone, press enter to exit")
raw_input()
