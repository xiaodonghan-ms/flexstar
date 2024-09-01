import os
import sys
import tkinter as tk
from tkinter import messagebox

def run(folder_path):
    files = os.listdir(folder_path)
    file_count = len(files)
    result = f"Total files: {file_count}\nFiles:\n" + "\n".join(files)
    return result

def create_gui(folder_path):
    result = run(folder_path)
    window = tk.Toplevel()
    window.title("File Count Results")

    label = tk.Label(window, text="File Count Results", font=("Arial", 14))
    label.pack(pady=10)

    text_area = tk.Text(window, wrap='word', height=15, width=50)
    text_area.insert('1.0', result)
    text_area.pack(expand=True, fill='both', padx=10, pady=10)

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(pady=10)
    
    #window.mainloop()

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    #create_gui(folder)
    print(run(folder))
