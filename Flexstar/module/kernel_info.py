import os
import sys
import pandas as pd
import tkinter as tk
import pandas as pd
from tkinter import ttk

"""
Module: lsmod, sysctl-a
Author: Ken Zhang
Email: devilken20131984@gmail.com
"""

#formatting "lsmod" output
def formatting_lsmod(folder_path, ):
    filepath = os.path.join(folder_path, r'lsmod')
    with open(filepath, 'r') as f:
        content = f.readlines()
    output_header = content[0].split()
    output_lines = []
    for line in content[1:]:
        s_line = line.split()
        if len(s_line) == 3:
            s_line.append(" ")
        output_lines.append(s_line)
    return output_header,output_lines

#formatting "sysctl -a" output
def formatting_sysctl_a(folder_path):
    filepath = os.path.join(folder_path, r'sos_commands/kernel/sysctl_-a')
    with open(filepath, 'r') as f:
        content = f.readlines()
    output_lines = []
    output_header = ["Name", "Value"]
    for line in content:
        line_split = line.split('=')
        output_line = [line_split[0], line_split[1].strip()]
        output_lines.append(output_line)
    return output_header,output_lines

def df_formated(output_header, output_lines):
    df_output = pd.DataFrame(output_lines, columns=output_header)
    return df_output

def create_gui(folder_path,input_func):
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