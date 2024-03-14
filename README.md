# ImageGrid
 
 Quickly create grid of png images from ND2 file zstacks

 1. Drag ijm file into Fiji/ImageJ
 2. Run the ijm file and select directory of ND2 files 
        This code performs a z-stack on the image, adjusts the brightness of each color, then saves an image for each color and a merged image all as png files in an output folder within the same directory
 3. Run the ipynb file and select directory of PNG images (output folder generated from fiji macro)
        It outputs 4xn(depending on how many images you have) grid of images
        Works on square or half rectangle pngs