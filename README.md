Ubuntu Image Fetcher

This is a Python program that downloads an image from the internet and saves it to a folder called Fetched_Images.

Features

Ask the user for an image URL (or use a default if none is given).

Check if the link is really an image.

Create a safe filename for the image.

Save the image inside the Fetched_Images folder.

Requirements

Python 3

Install the library:

pip install requests

How to Run

Clone or download this project.

Open a terminal in the project folder.

Run the script:

python fetch_image.py


Enter an image URL or just press Enter to use the default image.

Example Run
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter the image URL (or press Enter to use a default image):
Using default image URL: https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png
✓ Successfully fetched: Example.png
✓ Image saved to Fetched_Images/Example.png

Project Files
fetch_image.py     # The main script
Fetched_Images/    # Folder where images are saved
README.md          # This file
