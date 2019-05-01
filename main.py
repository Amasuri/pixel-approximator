#python 2.7.13

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
            #print(pixel)

#print("\nClose if you aren't okay with the pallette")
#print("Enter to continue")
#raw_input()


print("\nloading source files..")
default_dir = os.getcwd()
os.chdir(default_dir + "\Source")
source_files = {}
for filename in os.listdir("."):
    if filename.endswith('.png'):
        source_files[filename] = Image.open(filename)


print("\napproximating...\n")
os.chdir(default_dir + "\Result")
for file in source_files.keys():
    print("file: " + file)
    width, height = source_files[file].size

    #create pixmap
    pMap = source_files[file].load()

    #run the script to change pixels to those of the pallette
    for x in range(width):
        for y in range(height):
            pMap[x, y] = chkpix.find_approximate(pMap[x, y], pallette_colors)

    source_files[file].save(file)
    pass



print("\ndone, press enter to exit")
raw_input()
