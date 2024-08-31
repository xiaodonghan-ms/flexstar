import tkinter as tk
from tkinter import filedialog, messagebox
from multiprocessing import Process
import os
import time

# Example module functions (these would be in their respective .py files)
def module_a(folder_path):
    time.sleep(2)  # Simulate processing
    result = f"Module A processed folder: {folder_path}\nFiles: {os.listdir(folder_path)}"
    return result

def module_b(folder_path):
    time.sleep(2)  # Simulate processing
    result = f"Module B processed folder: {folder_path}\nTotal files: {len(os.listdir(folder_path))}"
    return result

def module_c(folder_path):
    time.sleep(2)  # Simulate processing
    result = f"Module C processed folder: {folder_path}\nFiles: {os.listdir(folder_path)}"
    return result

# A dictionary to map module names to their functions
modules = {
    "Module A": module_a,
    "Module B": module_b,
    "Module C": module_c,
}

def run_module(module_name, folder_path):
    # Start a new process for the selected module
    process = Process(target=execute_module, args=(module_name, folder_path))
    process.start()

def execute_module(module_name, folder_path):
    result = modules[module_name](folder_path)
    display_result(result)

def display_result(result):
    # Create a new Tkinter window to display the result
    result_window = tk.Tk()  # Create a new main window for results
    result_window.title("Module Result")
    
    # Set a different layout for the result window
    result_label = tk.Label(result_window, text=result, padx=20, pady=20)
    result_label.pack()

    close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
    close_button.pack(pady=10)

def on_run():
    folder_path = folder_var.get()
    selected_module = module_var.get()
    if not folder_path or selected_module == "Select a Module":
        messagebox.showwarning("Warning", "Please select a folder and a module.")
        return
    run_module(selected_module, folder_path)

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_var.set(folder_selected)

# Create the main window
root = tk.Tk()
root.title("Module Runner")

# Variable to hold the folder path
folder_var = tk.StringVar()

# Button to browse for a folder
browse_button = tk.Button(root, text="Browse Folder", command=browse_folder)
browse_button.pack(pady=10)

# Label to show the selected folder
folder_label = tk.Label(root, textvariable=folder_var)
folder_label.pack(pady=5)

# Dropdown for module selection
module_var = tk.StringVar(root)
module_var.set("Select a Module")  # Default option
module_menu = tk.OptionMenu(root, module_var, *modules.keys())
module_menu.pack(pady=20)

# Button to run the selected module
run_button = tk.Button(root, text="Run Module", command=on_run)
run_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
