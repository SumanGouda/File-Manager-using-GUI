## 🗂️ File Organizer using Python
A simple Python script that organizes files in a selected folder into subfolders based on their file extensions. Built using tkinter, os, and shutil.

## 🚀 Features
Choose any folder on your system using a GUI

Automatically organizes files by extension (e.g., .jpg, .pdf, .mp3)

Skips folders and empty files

Creates folders if they don't exist

Clean and modular object-oriented design using a class

## 📦 Requirements
Python 3.x

Built-in libraries only:
> os
> shutil
> tkinter

## 🛠️ How to Run
1. Clone the repo or download the script.
2. Run the script.
3. Select the folder you want to organize when prompted.

## 📁 Folder Structure Example
# Before:
/Downloads
    song.mp3
    image.jpg
    document.pdf

# After running:
/Downloads
    /mp3
        song.mp3
    /jpg
        image.jpg
    /pdf
        document.pdf

## 📄 License
This project is open-source and free to use under the MIT License.

ChatGPT said:
Sure! Here's the updated README.md with an Author section added at the end:

markdown
Copy code
# File Organizer Project

This Python project helps organize files in a selected folder based on their file extensions. Files are automatically moved into newly created subfolders named after their extensions (e.g., `.jpg`, `.pdf`, etc.).

## Features

- Automatically sorts files into folders based on extension.
- Skips existing folders and only moves files.
- Uses a graphical interface to select the folder (via `tkinter`).

## Technologies Used

- Python
- tkinter (for folder selection dialog)
- os module
- shutil module

## How to Use

1. Run the script.
2. A folder selection window will pop up. Choose the folder you want to organize.
3. The program will create folders for each file type and move corresponding files into them.

## Example

Before:
📁 Downloads
┣━ image.jpg
┣━ document.pdf
┗━ script.py

After running the script:
📁 Downloads
┣━ jpg
┃ ┗━ image.jpg
┣━ pdf
┃ ┗━ document.pdf
┗━ py
┗━ script.py


## Author

- **Suman Gouda**  
  [GitHub Profile](https://github.com/SumanGouda)

---

Feel free to improve or customize it for your needs!




  

