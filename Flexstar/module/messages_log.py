import os
import sys
import pandas as pd
import tkinter as tk
import pandas as pd

"""
Module: systemd_analysis
Author: Ken Zhang
Email: devilken20131984@gmail.com
"""

#formatting /var/log/messages output
def formatting_journalctl_a(filepath):
    with open(filepath, 'r',encoding="utf8") as f:
        content = f.readlines()
    content = content[1:]
    output_lines = []
    output_header = ["DateTime", "Hostname", "Process", "Message"]
    for line in content:
        output_line = []
        line_split = line.split()
        output_line.append(" ".join(line_split[0:3]))
        output_line.append(line_split[3])
        output_line.append(line_split[4])
        output_line.append(" ".join(line_split[5:]))
        output_lines.append(output_line)
    return output_header,output_lines

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