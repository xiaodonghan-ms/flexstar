import os
import sys
import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

"""
Module: system_property
Author: Anton Han
Email: xiaodonghan@microsoft.com
"""

def parse_os_property(folder_path):
    os_file_path = os.path.join(folder_path, 'etc/redhat-release')
    if not os.path.isfile(os_file_path):
        return "OS Information: Not found"

    with open(os_file_path, 'r') as file:
        return file.readlines()

def parse_interrupts(folder_path):
    interrupts_file_path = os.path.join(folder_path, 'proc/interrupts')
    if not os.path.isfile(interrupts_file_path):
        return "Interrupts Information: Not found"

    with open(interrupts_file_path, 'r') as file:
        return file.readlines()

def parse_memory(folder_path):
    memory_file_path = os.path.join(folder_path, 'sos_commands/memory/free')
    if not os.path.isfile(memory_file_path):
        return "Memory Information: Not found"

    with open(memory_file_path, 'r') as file:
        return file.readlines()

def parse_io(folder_path):
    io_file_path = os.path.join(folder_path, 'sos_commands/filesys/df_-al_-x_autofs')
    if not os.path.isfile(io_file_path):
        return "I/O Information: Not found"

    with open(io_file_path, 'r') as file:
        return file.readlines()

def parse_network_ethtool(folder_path):
    network_info = {}

    sos_networking_path = os.path.join(folder_path, 'sos_commands/networking')

    if os.path.isdir(sos_networking_path):
        for file in os.listdir(sos_networking_path):
            if file.startswith("ethtool_-i_"):
                nic_name = file.split('_')[2]  # Extract NIC name from the file name
                full_path = os.path.join(sos_networking_path, file)

                with open(full_path, 'r') as f:
                    # Read the contents of the file and store in the dictionary
                    network_info[nic_name] = f.read().strip()

    else:
        return "Network Information: Not found"

    return network_info

def parse_sosreport(folder_path):
    parsed_data = {
        'OS Information': parse_os_property(folder_path),
        'Interrupt Information': parse_interrupts(folder_path),
        'Memory Information': parse_memory(folder_path),
        'I/O Information': parse_io(folder_path),
        'Network Information': parse_network_ethtool(folder_path),
    }
    return parsed_data

def create_gui(log_file_path):
    parsed_info = parse_sosreport(log_file_path)

    # Create a new Tkinter window
    result_window = tk.Tk()
    result_window.title("Parsed System Property")
    # Get the screen dimensions
    screen_width = result_window.winfo_screenwidth()
    screen_height = result_window.winfo_screenheight()

    # Set the window size to be maximized but not fullscreen
    result_window.geometry(f"{screen_width}x{screen_height - 80}+0+0")

    result_text = ScrolledText(result_window, wrap='word', width=80, height=25)
    result_text.pack(fill='both', expand=True)

    # Display the parsed information
    for category, info in parsed_info.items():
        result_text.insert(tk.END, f"{category}:\n")
        if isinstance(info, dict):
            for key, value in info.items():
                result_text.insert(tk.END, f"  {key}: {value}\n")
        else:
            for item in info:
                result_text.insert(tk.END, f"  {item}\n")
        result_text.insert(tk.END, "\n")  # Blank line for better readability

    result_window.mainloop()

def main(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory")
        return

    create_gui(folder_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python system_property.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    main(folder_path)
