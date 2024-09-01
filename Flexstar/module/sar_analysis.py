import os
import sys
import tkinter as tk
from tkinter import ttk


def run(folder_path, selected_file):
    # Construct the full path to the selected SAR file
    file_path = os.path.join(folder_path, selected_file)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        result = f"Contents of {selected_file}:\n{content}"
    else:
        result = "Selected file does not exist."
    return result


def update_display(folder_path, selected_file, text_area):
    result = run(folder_path, selected_file)
    text_area.delete('1.0', tk.END)  # Clear existing text
    text_area.insert('1.0', result)  # Insert new content


def create_gui(folder_path):
    # Construct the path to the SAR files
    folder_path = os.path.join(folder_path, 'var', 'log', 'sa')

    # Get the list of SAR files
    sar_files = [f for f in os.listdir(folder_path) if
                 f.startswith('sar') and os.path.isfile(os.path.join(folder_path, f))]

    window = tk.Tk()
    window.title("SAR Analysis")
    # Get the screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window size to be maximized but not fullscreen
    window.geometry(f"{screen_width}x{screen_height - 80}+0+0")

    # Dropdown for selecting SAR files
    selected_file_var = tk.StringVar(value=sar_files[0] if sar_files else "")
    file_dropdown = ttk.Combobox(window, textvariable=selected_file_var, values=sar_files, state="readonly")
    file_dropdown.pack(pady=10)

    # Frame for the text area
    text_frame = tk.Frame(window)
    text_frame.pack(expand=True, fill='both', padx=10, pady=10)

    # Text area to display SAR file content
    text_area = tk.Text(text_frame, wrap='word', height=15, width=50)
    text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Vertical scrollbar
    v_scrollbar = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text_area.yview)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Horizontal scrollbar
    h_scrollbar = tk.Scrollbar(window, orient=tk.HORIZONTAL, command=text_area.xview)
    h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    # Configure the text area to use the scrollbars
    text_area.config(yscrollcommand=v_scrollbar.set)
    text_area.config(xscrollcommand=h_scrollbar.set)

    # Update text area when a new file is selected
    def on_file_select(event):
        selected_file = selected_file_var.get()
        update_display(folder_path, selected_file, text_area)

    file_dropdown.bind("<<ComboboxSelected>>", on_file_select)

    # Initial display of the first SAR file (if available)
    if sar_files:
        update_display(folder_path, sar_files[0], text_area)

    window.mainloop()


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    create_gui(folder)
