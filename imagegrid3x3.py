import os
from PIL import Image
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import math

# Function to resize images with higher quality
def resize_images(images_dir, output_size=(600, 600)):
    resized_images = []
    for filename in os.listdir(images_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(images_dir, filename)
            img = Image.open(img_path)
            img_resized = img.resize(output_size, Image.BICUBIC)  # Use bicubic for better quality
            resized_images.append(img_resized)
    return resized_images

# Function to plot images in a grid while maintaining aspect ratio
def plot_images(images, num_cols=3):
    num_images = len(images)
    num_rows = math.ceil(num_images / num_cols)
    
    # Calculate figure size based on the number of columns
    fig_width = 10
    fig_height = fig_width / num_cols * num_rows
    
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(fig_width, fig_height))
    fig.subplots_adjust(hspace=0.3, wspace=0.3)
    
    for i, ax in enumerate(axs.flat):
        if i < num_images:
            img = images[i]
            ax.imshow(img)
            ax.axis('off')
        else:
            ax.axis('off')  # Hide the subplot if there are fewer images than subplots
    
    plt.show()

# Function to ask user for directory
def ask_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory = filedialog.askdirectory(title="Select Directory Containing Images")
    return directory

# Main function
def main():
    images_dir = ask_directory()
    if images_dir:
        resized_images = resize_images(images_dir)
        plot_images(resized_images)

if __name__ == "__main__":
    main()
