# ImageGrid
 
 Quickly create grid of png images from ND2 file zstacks

 Useful when you want to visualize many microscopy images at once

 1. Drag ijm file into Fiji/ImageJ
 2. Run the ijm file and select directory of ND2 files 
        This code performs a z-stack on the image, then splits color channels into individual images, then saves a png for each color and a merged png of all colors in an output folder within the same directory
 3. Run the ipynb file and select directory of PNG images (output folder generated from fiji macro)
        It outputs 4xn(depending on how many images you have) grid of images
        Works on square or half rectangle pngs
        Optionally can adjust brightness of different channels and add title to image grid