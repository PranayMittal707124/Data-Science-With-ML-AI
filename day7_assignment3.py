import os
import shutil

# Define the source folder
src_folder = 'JECRC'

# Define the destination folders
image_folder = 'image_folder'
text_folder = 'text_folder'
pdf_folder = 'pdf_folder'

# Create the destination folders if they don't exist
if not os.path.exists(image_folder):
    os.makedirs(image_folder)
if not os.path.exists(text_folder):
    os.makedirs(text_folder)
if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)

# Iterate through all files in the source folder
for filename in os.listdir(src_folder):
    # Get the file extension
    file_ext = os.path.splitext(filename)[1].lower()

    # Filter out images
    if file_ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
        shutil.move(os.path.join(src_folder, filename), os.path.join(image_folder, filename))
    # Filter out text files
    elif file_ext in ['.txt', '.text']:
        shutil.move(os.path.join(src_folder, filename), os.path.join(text_folder, filename))
    # Filter out pdf files
    elif file_ext == '.pdf':
        shutil.move(os.path.join(src_folder, filename), os.path.join(pdf_folder, filename))