import os
import sys
import pandas as pd
import tkinter as tk
import pandas as pd
from tkinter import ttk

"""
Module: net_config
Author: Ken Zhang
Email: devilken20131984@gmail.com
"""

#formatting "ip -o addr" output
def formatting_ip_o_addr(folder_path):
    filepath = os.path.join(folder_path, 'sos_commands/networking/ip_-o_addr')
    with open(filepath, 'r',encoding="utf8") as f:
        content = f.readlines()
    output_lines = []
    output_header = ["Interface", "ipv4_v6","IP", "other_info"]
    
    for line in content:
        output_line = []
        line_split = line.split()
        output_line.append(line_split[1])
        output_line.append(line_split[2])
        output_line.append(line_split[3])
        output_line.append(" ".join(line_split[4:]))
        output_lines.append(output_line)
    return output_header,output_lines
    
def formatting_netstat_iconnection(folder_path):
    filepath = os.path.join(folder_path, r'sos_commands/networking/netstat_-W_-neopa')
    with open(filepath, 'r') as f:
        content = f.readlines()
    content = content[2:content.index('Active UNIX domain sockets (servers and established)\n')]
    output_lines = []
    output_header = ["Proto", "Recv-Q", "Send-Q", "Local Address", "Foreign Address", "State", "User","Inode","PID/Program name","Timer"]
    for line in content:
        line_split = line.split()
        if len(line_split) == 12:
            line_split[-4] = " ".join(line_split[-4:-2])
            line_split.remove(line_split[-3])
        if len(line_split) == 10:
            line_split.insert(5, " ")
        line_split[-2] = " ".join(line_split[-2:])
        line_split.remove(line_split[-1])
        output_lines.append(line_split)
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