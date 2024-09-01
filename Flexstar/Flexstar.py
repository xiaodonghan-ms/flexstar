import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
import subprocess

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_var.set(folder_path)
    folder_text.delete('1.0', tk.END)  # Clear previous text
    folder_text.insert(tk.END, folder_path)  # Insert the new folder path

def run_module():
    folder_path = folder_var.get()
    selected_module = module_var.get()
    
    if not folder_path:
        messagebox.showwarning("Warning", "Please select a folder.")
        return
    
    if selected_module == "Select Module":
        messagebox.showwarning("Warning", "Please select a module.")
        return

    # Run the selected module in a new process
    try:
        subprocess.Popen(["python", selected_module, folder_path])
    except Exception as e:
        messagebox.showerror("Error", f"Error running module: {e}")

# Create the main window
root = tk.Tk()
root.title("Log Parser")
root.geometry("600x400")

folder_var = tk.StringVar()
module_var = tk.StringVar(value="Select Module")

# Create UI elements
frame = tk.Frame(root)
frame.pack(pady=10, padx=10, fill='x')

browse_button = tk.Button(frame, text="Browse Folder", command=browse_folder)
browse_button.pack(side='left', padx=5)

# Use ScrolledText for folder path display
folder_text = ScrolledText(frame, height=1, wrap='word', width=40)
folder_text.pack(side='left', padx=5, fill='x', expand=True)

module_label = tk.Label(root, text="Select Module:")
module_label.pack(pady=5)

modules = ["a.py", "b.py", "c.py"]
module_dropdown = ttk.Combobox(root, textvariable=module_var, values=modules)
module_dropdown.pack(pady=5, padx=10, fill='x')

run_button = tk.Button(root, text="Run", command=run_module)
run_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
