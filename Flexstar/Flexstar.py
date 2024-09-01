import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import scrolledtext
import importlib
import subprocess

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_var.set(folder_path)

def run_module():
    folder_path = folder_var.get()
    selected_module = module_var.get()
    
    if not folder_path:
        messagebox.showwarning("Warning", "Please select a folder.")
        return
    
    if selected_module == "Select Module":
        messagebox.showwarning("Warning", "Please select a module.")
        return

    # Dynamically import the selected module
    module = importlib.import_module(selected_module[:-3])  # Remove .py extension
    module.create_gui(folder_path)

# Create the main window
root = tk.Tk()
root.title("Log Parser")
root.geometry("600x400")  # Set the size of the main window

folder_var = tk.StringVar()
module_var = tk.StringVar(value="Select Module")

# Create UI elements
frame = tk.Frame(root)
frame.pack(pady=10, padx=10, fill='x')

browse_button = tk.Button(frame, text="Browse Folder", command=browse_folder)
browse_button.pack(side='left', padx=5)

# Use a ScrolledText widget for the folder path
folder_label = scrolledtext.ScrolledText(frame, height=1, wrap='word', width=40)
folder_label.pack(side='left', padx=5, fill='x', expand=True)
folder_label.config(state='normal')  # Allow editing
folder_label.bind("<Key>", lambda e: "break")  # Prevent editing

def update_folder_label(*args):
    folder_label.config(state='normal')
    folder_label.delete('1.0', tk.END)
    folder_label.insert(tk.END, folder_var.get())
    folder_label.config(state='disabled')

folder_var.trace("w", update_folder_label)

module_label = tk.Label(root, text="Select Module:")
module_label.pack(pady=5)

modules = ["a.py", "b.py", "c.py"]
module_dropdown = ttk.Combobox(root, textvariable=module_var, values=modules)
module_dropdown.pack(pady=5, padx=10, fill='x')

run_button = tk.Button(root, text="Run", command=run_module)
run_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
