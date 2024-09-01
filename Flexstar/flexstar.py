import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

"""
App: Flexstar
Author: Anton Han
Email: xiaodonghan@microsoft.com
"""

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_var.set(folder_path)
        folder_text.delete('1.0', tk.END)  # Clear existing text
        folder_text.insert(tk.END, folder_path)  # Insert selected path

def run_module():
    # Function to run the selected module
    folder_path = folder_text.get('1.0', tk.END).strip()
    folder_var.set(folder_path)
    selected_module = module_var.get()

    if not folder_path:
        messagebox.showwarning("Warning", "Please select a folder.")
        return

    if selected_module == "Select Module":
        messagebox.showwarning("Warning", "Please select a module.")
        return

    # Run the selected module in a new process
    try:
        subprocess.Popen(["python", os.path.join('module', selected_module), folder_path])
    except Exception as e:
        messagebox.showerror("Error", f"Error running module: {e}")

def load_modules():
    # Automatically load all .py files from the module folder
    module_folder = 'module'
    modules = [f for f in os.listdir(module_folder) if f.endswith('.py')]
    return modules

# Create the main window
root = tk.Tk()
root.title("Flexstar")
root.configure(bg="#f0f0f0")  # Light background color

# Calculate screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size
window_width = 800
window_height = 600

# Calculate position for centering
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set window geometry
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

folder_var = tk.StringVar()
module_var = tk.StringVar(value="Select Module")

# Create UI elements
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20, padx=20, fill='x')

# Browse button (in first row)
browse_button = tk.Button(frame, text="Browse Folder", command=browse_folder, bg="#4CAF50", fg="white", font=("Arial", 10))
browse_button.pack(pady=10)  # Add padding below

# ScrolledText for folder path display (in second row)
folder_text = ScrolledText(frame, height=1, wrap='word', bg="#ffffff", font=("Arial", 10))
folder_text.pack(pady=10)  # Add padding below

# Module selection
module_label = tk.Label(root, text="Select Module:", bg="#f0f0f0", font=("Arial", 12))
module_label.pack(pady=10)

# Load modules and populate the dropdown
modules = load_modules()
module_dropdown = ttk.Combobox(root, textvariable=module_var, values=modules, state="readonly", font=("Arial", 10))
module_dropdown.pack(pady=10)

# Run button
run_button = tk.Button(root, text="Run Module", command=run_module, bg="#2196F3", fg="white", font=("Arial", 10))
run_button.pack(pady=10)

# Version remark at the bottom right
version_label = tk.Label(root, text="Flexstar 2.0.0.0", anchor='e', bg="#f0f0f0", font=("Arial", 10))
version_label.pack(side='bottom', anchor='e', padx=20, pady=20)

# Start the GUI event loop
root.mainloop()
