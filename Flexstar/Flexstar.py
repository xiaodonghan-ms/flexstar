import tkinter as tk
from tkinter import filedialog, messagebox, ttk
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

    # Run the selected module in a new process
    try:
        result = subprocess.run(
            ["python", selected_module, folder_path],
            capture_output=True,
            text=True,
            check=True
        )
        output_window(result.stdout)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running module: {e.stderr}")

def output_window(output):
    result_window = tk.Toplevel(root)
    result_window.title("Parse Results")
    
    text_area = tk.Text(result_window, wrap='word')
    text_area.insert('1.0', output)
    text_area.pack(expand=True, fill='both')
    
    button_close = tk.Button(result_window, text="Close", command=result_window.destroy)
    button_close.pack()

# Create the main window
root = tk.Tk()
root.title("Log Parser")

folder_var = tk.StringVar()
module_var = tk.StringVar(value="Select Module")

# Create UI elements
frame = tk.Frame(root)
frame.pack(pady=10)

browse_button = tk.Button(frame, text="Browse Folder", command=browse_folder)
browse_button.pack(side='left', padx=5)

folder_label = tk.Label(frame, textvariable=folder_var)
folder_label.pack(side='left', padx=5)

module_label = tk.Label(root, text="Select Module:")
module_label.pack(pady=5)

modules = ["a.py", "b.py", "c.py"]
module_dropdown = ttk.Combobox(root, textvariable=module_var, values=modules)
module_dropdown.pack(pady=5)

run_button = tk.Button(root, text="Run", command=run_module)
run_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
