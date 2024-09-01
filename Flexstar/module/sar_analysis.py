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


def update_display(folder_path, selected_file, text_area, section_var):
    sections = run(folder_path, selected_file)
    selected_section = section_var.get()
    content = sections.get(selected_section, "Section not found.")

    text_area.delete('1.0', tk.END)  # Clear existing text
    text_area.insert('1.0', content)  # Insert new content


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
        sections = run(folder_path, selected_file)
        section_dropdown['values'] = list(sections.keys())  # Update section dropdown
        if len(sections.keys()) > 0:
            section_dropdown.current(0)  # Select the first section by default
        update_display(folder_path, selected_file, text_area, section_var)

    # Update text area when a new section is selected
    def on_section_select(event):
        update_display(folder_path, selected_file_var.get(), text_area, section_var)

    file_dropdown.bind("<<ComboboxSelected>>", on_file_select)
    section_dropdown.bind("<<ComboboxSelected>>", on_section_select)

    # Initial display of the first SAR file (if available)
    if sar_files:
        on_file_select(None)

    window.mainloop()


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    create_gui(folder)
