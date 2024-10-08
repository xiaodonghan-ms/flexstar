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
def formatting_systemctl_listunites(folder_path):
    filepath = os.path.join(folder_path, r'sos_commands/systemd/systemctl_list-units')
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
def formatting_systemctl_listunitfiles(folder_path):
    filepath = os.path.join(folder_path, r'sos_commands/systemd/systemctl_list-unit-files')
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

def create_gui(folder_path, input_func):
    output_header, output_lines = input_func(folder_path)
    result = df_formated(output_header, output_lines)
    
    # Create the main window
    root = tk.Tk()
    root.title("Pandas DataFrame in Tkinter")
    
    # Create a Treeview widget
    tree = ttk.Treeview(root)
    tree["columns"] = list(result.columns)
    tree["show"] = "headings"   
    
    # Define the column headings
    for column in result.columns:
        tree.heading(column, text=column)
        # Add the data to the Treeview
    for index, row in result.iterrows():
        tree.insert("", "end", values=list(row))

    # Pack the Treeview widget
    tree.pack(expand=True, fill='both')

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    create_gui(folder)
