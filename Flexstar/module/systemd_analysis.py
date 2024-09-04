import os
import sys
import pandas as pd
import tkinter as tk
import pandas as pd
import numpy as np
"""
Module: systemd_analysis
Author: Ken Zhang
Email: devilken20131984@gmail.com
"""
#formatting systemctl list-units
def formatting_systemctl_listunites(filepath):
    with open(filepath, 'r') as f:
        content = f.readlines()
    content = content[:-6]
    output_lines = []
    output_header = content[0].split()
    for line in content[1:]:
        line_split = line.split()
        output_line = line_split[:4]
        output_line.append(' '.join(line_split[4:]))
        output_lines.append(output_line)
    return output_header,output_lines

#formatting systemctl list-units-files
def formatting_systemctl_listunitfiles(filepath):
    with open(filepath, 'r') as f:
        content = f.readlines()
    content = content[:-2]
    output_header = []
    output_lines = []
    output_header.append(" ".join(content[0].split()[0:2]))
    output_header.append(content[0].split()[2])
    output_header.append(" ".join(content[0].split()[3:]))
    for line in content[1:]:
        output_lines.append(line.split())
    return output_header,output_lines

#Return data as Pandas DataFrame
def df_formated(output_header, output_lines):
    df_output = pd.DataFrame(output_lines, columns=output_header)
    return df_output




def create_gui(folder_path):
    result = run(folder_path)

    window = tk.Tk()
    window.title("Sar Analysis")
    # Get the screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window size to be maximized but not fullscreen
    window.geometry(f"{screen_width}x{screen_height - 80}+0+0")

    label = tk.Label(window, text="Sar Analysis", font=("Arial", 14))
    label.pack(pady=10)

    text_area = tk.Text(window, wrap='word', height=15, width=50)
    text_area.insert('1.0', result)
    text_area.pack(expand=True, fill='both', padx=10, pady=10)

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    create_gui(folder)
