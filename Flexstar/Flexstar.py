import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import scrolledtext
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
        output_window(result.stdout, selected_module)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running module: {e.stderr}")

def output_window(output, module):
    result_window = tk.Toplevel(root)
    result_window.title("Parse Results")

    if module == "a.py":
        # Layout for a.py
        label = tk.Label(result_window, text="File Count Results", font=("Arial", 14))
        label.pack(pady=10)
        text_area = tk.Text(result_window, wrap='word', height=15, width=50)
        text_area.insert('1.0', output)
        text_area.pack(expand=True, fill='both', padx=10, pady=10)
    elif module == "b.py":
        # Layout for b.py
        label = tk.Label(result_window, text="Log File Count Results", font=("Arial", 14))
        label.pack(pady=10)
        text_area = tk.Text(result_window, wrap='word', height=15, width=50)
        text_area.insert('1.0', output)
        text_area.pack(expand=True, fill='both', padx=10, pady=10)
    elif module == "c.py":
        # Layout for c.py
        label = tk.Label(result_window, text="Text File Content", font=("Arial", 14))
        label.pack(pady=10)
        text_area = tk.Text(result_window, wrap='word', height=15, width=50)
        text_area.insert('1.0', output)
        text_area.pack(expand=True, fill='both', padx=10, pady=10)

    button_close = tk.Button(result_window, text="Close", command=result_window.destroy)
    button_close.pack(pady=10)

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
