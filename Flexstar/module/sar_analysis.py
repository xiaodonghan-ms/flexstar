import os
import re
import sys
import tkinter as tk
from tkinter import ttk


def find_first_part(line):
    # Split the line into parts
    parts = line.split()

    # Iterate through the parts
    for part in parts:
        # Check if the part contains letters and is not "AM" or "PM"
        if re.search(r'[a-zA-Z]', part) and part not in ["AM", "PM"]:
            return part
    return "Unknown"  # Return Unknown if no valid part is found


def run(folder_path, selected_file):
    # Construct the full path to the selected SAR file
    file_path = os.path.join(folder_path, selected_file)
    sections = {}
    current_section = None
    section_lines = []
    last_is_average = False

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            # Skip empty lines and lines containing "Linux" or "linux"
            if not line or "Linux" in line:
                continue

            # Check for the "Average" keyword to identify new sections
            if line.startswith("Average:"):
                # Continue collecting lines for the current section
                if current_section and section_lines:
                    section_lines.append(line)

                last_is_average = True
            else:
                if last_is_average:
                    sections[current_section] = "\n".join(section_lines)

                    current_section = None
                    section_lines = []
                    last_is_average = False

                # Continue collecting lines for the current section
                if current_section and section_lines:
                    section_lines.append(line)
                else:
                    # Start a new section
                    current_section = find_first_part(line)  # Get the second word as section name
                    section_lines = [line]  # Start collecting lines for this section

        # Save the last section if it exists
        if current_section and section_lines:
            sections[current_section] = "\n".join(section_lines)

    return sections


def update_display(folder_path, selected_file, treeview, section_var):
    sections = run(folder_path, selected_file)
    selected_section = section_var.get()

    # Clear the existing columns and rows in the Treeview
    treeview.delete(*treeview.get_children())
    treeview["columns"] = []  # Reset columns

    # Get the data for the selected section
    content = sections.get(selected_section, [])

    if not content:
        return  # No content to display

    # Determine the columns based on the first line of content
    content_list = content.split("\n")
    first_line_parts = content_list[0].split()
    num_columns = len(first_line_parts)

    # Set up columns
    treeview["columns"] = [first_line_parts[i] for i in range(num_columns)]
    for i in range(num_columns):
        treeview.heading(first_line_parts[i], text=first_line_parts[i])
        treeview.column(first_line_parts[i], anchor=tk.CENTER)

    # Insert new rows for the selected section
    for line in content_list[1:]:
        parts = line.split()  # Split the line into parts for table display
        treeview.insert("", tk.END, values=parts)


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

    drop_down_frame = tk.Frame(window)
    drop_down_frame.pack(pady=10)

    # Dropdown for selecting SAR files
    selected_file_var = tk.StringVar(value=sar_files[0] if sar_files else "")
    file_dropdown = ttk.Combobox(drop_down_frame, textvariable=selected_file_var, values=sar_files, state="readonly")
    file_dropdown.pack(side=tk.LEFT, padx=5)  # Align to the left

    # Dropdown for selecting sections
    section_var = tk.StringVar(value="")
    section_dropdown = ttk.Combobox(drop_down_frame, textvariable=section_var, state="readonly")
    section_dropdown.pack(side=tk.LEFT, padx=5)  # Align to the left

    # Frame for the Treeview
    treeview_frame = tk.Frame(window)
    treeview_frame.pack(expand=True, fill='both', padx=10, pady=10)

    # Treeview to display SAR file content
    treeview = ttk.Treeview(treeview_frame, show='headings')
    treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scrollbars for the Treeview
    v_scrollbar = ttk.Scrollbar(treeview_frame, orient=tk.VERTICAL, command=treeview.yview)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    h_scrollbar = ttk.Scrollbar(window, orient=tk.HORIZONTAL, command=treeview.xview)
    h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    treeview.configure(yscrollcommand=v_scrollbar.set)
    treeview.configure(xscrollcommand=h_scrollbar.set)

    # Update Treeview when a new file is selected
    def on_file_select(event):
        selected_file = selected_file_var.get()
        sections = run(folder_path, selected_file)
        section_dropdown['values'] = list(sections.keys())  # Update section dropdown
        if len(sections.keys()) > 0:
            section_dropdown.current(0)  # Select the first section by default
        update_display(folder_path, selected_file, treeview, section_var)

    # Update Treeview when a new section is selected
    def on_section_select(event):
        update_display(folder_path, selected_file_var.get(), treeview, section_var)

    file_dropdown.bind("<<ComboboxSelected>>", on_file_select)
    section_dropdown.bind("<<ComboboxSelected>>", on_section_select)

    # Initial display of the first SAR file (if available)
    if sar_files:
        on_file_select(None)

    window.mainloop()


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    create_gui(folder)
