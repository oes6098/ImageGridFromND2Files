import os
from PIL import Image
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

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

# Function to plot images in a grid with no more than 3 columns
def plot_images(images, num_cols=3):
    num_images = len(images)
    num_rows = (num_images - 1) // num_cols + 1
    plt.figure(figsize=(10, 10))
    for i, img in enumerate(images):
        plt.subplot(num_rows, num_cols, i + 1)
        plt.imshow(img)
        plt.axis('off')
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
