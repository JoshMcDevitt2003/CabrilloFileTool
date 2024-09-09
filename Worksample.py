import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog

def meets_criteria(filename):
    user_input = entry.get()
    if filename[0:2].lower() == user_input[0:2].lower() and user_input[-3:].lower() in filename.lower():
        return True
    return False

def process_files():
    base_dir = filedialog.askdirectory(title="Select Source Directory")
    destination_dir = filedialog.askdirectory(title="Select Destination Directory")
    
    if not base_dir or not destination_dir:
        messagebox.showerror("Error", "Please select both source and destination directories.")
        return

    counter = 0
    for subfolder in os.listdir(base_dir):
        source_dir = os.path.join(base_dir, subfolder)
        if os.path.isdir(source_dir):  
            for filename in os.listdir(source_dir):
                print(filename)
                if meets_criteria(filename):
                    counter += 1
                    file_path = os.path.join(source_dir, filename)
                    shutil.copy(file_path, destination_dir)
                    print(f"Copied: {filename} to {destination_dir}")
                    
    if counter == 0:
        messagebox.showinfo("No File Found", "No file matching the criteria found.")
    else:
        messagebox.showinfo("Operation Complete", f"Copied {counter} files to {destination_dir}")


root = tk.Tk()
root.title("File Copy Tool")


label = tk.Label(root, text="Enter Student Name:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Copy Files", command=process_files)
button.pack(pady=20)

root.mainloop()
