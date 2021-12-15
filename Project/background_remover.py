#pip install numpy (put in python terminal)
#python -m pip install pillow (run in the python terminal)
#install gdal (its really funky to do so (https://opensourceoptions.com/blog/how-to-install-gdal-for-python-with-pip-on-windows/))

#imports
import os
from os import path
import pathlib
from osgeo import gdal
from PIL import Image, ImageDraw, TiffImagePlugin
import numpy as np

#sets the scale and options for image conversion into a useable png
scale = '-scale'
options_list = [
    '-ot Byte',
    '-of PNG',
    scale
] 
options_string = " ".join(options_list)

#translates all of the images to PNGs
#sets the paths for the files to check if the exist
file1 = pathlib.Path(r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_blue.png")
file2 = pathlib.Path(r"C:\Users\New User\Desktop\392_Project\Reflectance\Ubaldo_GISproject_transparent_reflectance_blue.png")
#for the orthomosic images
#########################################################################################################
#if statment is there so it doesn't run this code if it doesn't need to
if file1.exists()==False:
    print("Started converting ortha images to pngs")
    gdal.Translate(
        r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_blue.png",
        r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_blue.tif",
        options = options_string
    )
    gdal.Translate(
        r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_green.png",
        r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_green.tif",
        options = options_string
    )
    gdal.Translate(
        r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_nir.png",
        r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_nir.tif",
        options = options_string
    )
    gdal.Translate(
        r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_red edge.png",
        r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_red edge.tif",
        options = options_string
    )
    gdal.Translate(
        r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_red.png",
        r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_red.tif",
        options = options_string
    )
#########################################################################################################

#for the reflectance images
#########################################################################################################
#if statment is there so it doesn't run this code if it doesn't need to
if file2.exists()==False:
    print("Started to convert reflect images to pngs")
    gdal.Translate(
        r"C:\Users\New User\Desktop\392_Project\Reflectance\Ubaldo_GISproject_transparent_reflectance_blue.png",
        r"C:\Users\New User\Desktop\392_Project\Reflectance\Ubaldo_GISproject_transparent_reflectance_blue.tif",
        options = options_string
    )
    gdal.Translate(
        r"C:\Users\New User\Desktop\392_Project\Reflectance\Ubaldo_GISproject_transparent_reflectance_green.png",
        r"C:\Users\New User\Desktop\392_Project\Reflectance\Ubaldo_GISproject_transparent_reflectance_green.tif",
        options = options_string
    )
    gdal.Translate(
        r"C:\Users\New User\Desktop\392_Project\Reflectance\Ubaldo_GISproject_transparent_reflectance_nir.png",
        r"C:\Users\New User\Desktop\392_Project\Reflectance\Ubaldo_GISproject_transparent_reflectance_nir.tif",
        options = options_string
    )
    gdal.Translate(
        r"C:\Users\New User\Desktop\392_Project\Reflectance\Ubaldo_GISproject_transparent_reflectance_red edge.png",
        r"C:\Users\New User\Desktop\392_Project\Reflectance\Ubaldo_GISproject_transparent_reflectance_red edge.tif",
        options = options_string
    )
    gdal.Translate(
        r"C:\Users\New User\Desktop\392_Project\Reflectance\Ubaldo_GISproject_transparent_reflectance_red.png",
        r"C:\Users\New User\Desktop\392_Project\Reflectance\Ubaldo_GISproject_transparent_reflectance_red.tif",
        options = options_string
    )
#########################################################################################################

#testing that the height and the width are correct
#print(height)
#print(width)

##testing color data for pixels
#print(Orth1_data[3000,2000])
'''
ColorTest = Orth1.getpixel((3000,2000))
r,g,b,a = ColorTest
print(ColorTest)
print(r)
print(g)
print(b)
print(a)
'''
#turns the images into a RGBA and loads it into an array
print("Opens the Images")
Orth1 = Image.open(r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_red.png").convert('RGBA')
Orth2 = Image.open(r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_blue.png").convert('RGBA')
Orth3 = Image.open(r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_green.png").convert('RGBA')
Orth4 = Image.open(r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_nir.png").convert('RGBA')
Orth5 = Image.open(r"C:\Users\New User\Desktop\392_Project\Orthomosiac\Ubaldo_GISproject_transparent_mosaic_red edge.png").convert('RGBA')

#sets the bounds for the image
height,width = Orth1.size

#array that stores the background pixels as 0 and the cotton as 1
print("creates the background 2d array")
background = [[0 for x in range(width)] for y in range(height)] 


#loads all the images
print("Loading the image data")
Orth1_data = Orth1.load()
Orth2_data = Orth2.load()
Orth3_data = Orth3.load()
Orth4_data = Orth4.load()
Orth5_data = Orth5.load()

#for loop to go through the image and finds the background
print("going through the loop to find the background")
for loop1 in range(height):
    for loop2 in range(width):
        r,g,b,a = Orth1.getpixel((loop1,loop2))
        if r >= 120:
            background[loop1][loop2] = 0
        else:
            background[loop1][loop2] = 1

#loop that uses background array to remove the background from all the ortha images
bFile = pathlib.Path(r"C:\Users\New User\Desktop\392_Project\red.png")
print("Checking to see if backgrounds need to be removed")
if bFile.exists() == False:
    print("going through the loop to remove the background from the images")
    for loop1 in range(height):
        for loop2 in range(width):
            if background[loop1][loop2] == 0:
                r,g,b,a = Orth1.getpixel((loop1,loop2))
                Orth1_data[loop1,loop2] = (0,0,0,0)
                r,g,b,a = Orth2.getpixel((loop1,loop2))
                Orth2_data[loop1,loop2] = (0,0,0,0)
                r,g,b,a = Orth3.getpixel((loop1,loop2))
                Orth3_data[loop1,loop2] = (0,0,0,0)
                r,g,b,a = Orth4.getpixel((loop1,loop2))
                Orth4_data[loop1,loop2] = (0,0,0,0)
                r,g,b,a = Orth5.getpixel((loop1,loop2))
                Orth5_data[loop1,loop2] = (0,0,0,0)


#checks to see if file exists and if not, it creates the image
print("Checking to see if the images exist")
if bFile.exists() == False:
    print("saving the images as new png images")
    Orth1.save("red.png")
    Orth2.save("blue.png")
    Orth3.save("green.png")
    Orth4.save("nir.png")
    Orth5.save("redEdge.png")


#loads the red band PNG without the background
print("Loading the NIR png")
nirBand = Image.open(r"C:\Users\New User\Desktop\392_Project\nir.png").convert('RGBA')
outLine_data = nirBand.load()

cFile = pathlib.Path(r"C:\Users\New User\Desktop\392_Project\border.png")
if cFile.exists() == False:
    print("Going through the loop to find the cotton")
    for loop1 in range(height):
        for loop2 in range(width):
            if background[loop1][loop2] == 1:
                r,g,b,a = nirBand.getpixel((loop1,loop2))
                pSum = r
                #top
                if loop1 == 0:
                    #top left
                    if loop2 == 0:
                        r2,g,b,a = nirBand.getpixel((loop1+1,loop2))
                        r3,g,b,a = nirBand.getpixel((loop1,loop2+1))
                        pSum = pSum + r2 + r3
                        print("Top Left")
                        if pSum >= 450 and pSum <= 510:
                            outLine_data[loop1,loop2] = (255,0,0,60)
                    #top right
                    elif loop2 == width-1:
                        r2,g,b,a = nirBand.getpixel((loop1-1,loop2))
                        r3,g,b,a = nirBand.getpixel((loop1+1,loop2))
                        pSum = pSum + r2 + r3
                        print("Top Right")
                        if pSum >= 450 and pSum <= 510:
                            outLine_data[loop1,loop2] = (255,0,0,60)
                    else:
                        r2,g,b,a = nirBand.getpixel((loop1,loop2-1))
                        r3,g,b,a = nirBand.getpixel((loop1,loop2+1))
                        r4,g,b,a = nirBand.getpixel((loop1+1,loop2))
                        pSum = pSum + r2 + r3 + r4
                        if pSum >= 600 and pSum <= 680:
                            outLine_data[loop1,loop2] = (255,0,0,60)
                #left
                elif loop2 == 0:
                    #bottom left
                    if loop1 == height-1:
                        r2,g,b,a = nirBand.getpixel((loop1-1,loop2))
                        r3,g,b,a = nirBand.getpixel((loop1,loop2+1))
                        pSum = pSum + r2 + r3
                        print("Bottom Left")
                        if pSum >= 450 and pSum <= 510:
                            outLine_data[loop1,loop2] = (255,0,0,60)
                    else:
                        r2,g,b,a = nirBand.getpixel((loop1-1,loop2))
                        r3,g,b,a = nirBand.getpixel((loop1,loop2+1))
                        r4,g,b,a = nirBand.getpixel((loop1+1,loop2))
                        pSum = pSum + r2 + r3 + r4
                        if pSum >= 600 and pSum <= 680:
                            outLine_data[loop1,loop2] = (255,0,0,60)
                #right
                elif loop2 == width-1:
                    #bottom right
                    if loop1 == height-1:
                        r2,g,b,a = nirBand.getpixel((loop1-1,loop2))
                        r3,g,b,a = nirBand.getpixel((loop1,loop2-1))
                        pSum = pSum + r2 + r3
                        print("Bottom Right")
                        if pSum >= 450 and pSum <= 510:
                            outLine_data[loop1,loop2] = (255,0,0,60)
                    else:
                        r2,g,b,a = nirBand.getpixel((loop1-1,loop2))
                        r3,g,b,a = nirBand.getpixel((loop1,loop2-1))
                        r4,g,b,a = nirBand.getpixel((loop1+1,loop2))
                        pSum = pSum + r2 + r3 + r4
                        if pSum >= 600 and pSum <= 680:
                            outLine_data[loop1,loop2] = (255,0,0,60)
                #bottom
                elif loop1 == height-1:
                    r2,g,b,a = nirBand.getpixel((loop1,loop2+1))
                    r3,g,b,a = nirBand.getpixel((loop1,loop2-1))
                    r4,g,b,a = nirBand.getpixel((loop1-1,loop2))
                    pSum = pSum + r2 + r3 + r4
                    if pSum >= 600 and pSum <= 680:
                        outLine_data[loop1,loop2] = (255,0,0,60)
                #not on the edge
                else:
                    r2,g,b,a = nirBand.getpixel((loop1,loop2-1))
                    r3,g,b,a = nirBand.getpixel((loop1,loop2+1))
                    r4,g,b,a = nirBand.getpixel((loop1-1,loop2))
                    r5,g,b,a = nirBand.getpixel((loop1+1,loop2))
                    pSum = pSum + r2 + r3 + r4
                    if pSum >= 750 and pSum <= 850:
                        outLine_data[loop1,loop2] = (255,0,0,60)                   

print("Checking to see if the cotton image exists")
if cFile.exists() == False:
    print("Saving the damage cotton image")
    nirBand.save("redCotton.png")

