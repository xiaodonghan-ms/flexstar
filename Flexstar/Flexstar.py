import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import time

# Example module functions
def module_a(folder_path):
    time.sleep(2)  # Simulate processing
    return f"Module A processed folder: {folder_path}\nFiles: {os.listdir(folder_path)}"

def module_b(folder_path):
    time.sleep(2)  # Simulate processing
    return f"Module B processed folder: {folder_path}\nTotal files: {len(os.listdir(folder_path))}"

def module_c(folder_path):
    time.sleep(2)  # Simulate processing
    return f"Module C processed folder: {folder_path}\nFiles: {os.listdir(folder_path)}"

modules = {
    "Module A": module_a,
    "Module B": module_b,
    "Module C": module_c,
}

def display_result(result):
    # Create a new Toplevel window to display the result
    result_window = tk.Toplevel(root)
    result_window.title("Module Result")
    
    # Create a scrolled text area for displaying results
    result_text = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=50, height=20)
    result_text.pack(expand=True, fill='both', padx=10, pady=10)

    # Insert the result into the text area
    result_text.insert(tk.END, result)
    result_text.config(state=tk.DISABLED)  # Make it read-only

    # Close button to close the result window
    close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
    close_button.pack(pady=10)

def on_run():
    folder_path = folder_var.get()
    selected_module = module_var.get()
    if not folder_path or selected_module == "Select a Module":
        messagebox.showwarning("Warning", "Please select a folder and a module.")
        return
    
    # Hide the main window
    #root.withdraw()

    # Execute the selected module and display the result
    result = modules[selected_module](folder_path)
    display_result(result)
    
    # Show the main window again after displaying the result
    root.deiconify()

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
