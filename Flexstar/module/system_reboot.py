import os
import sys
import tkinter as tk
import glob

"""
Module: system_reboot
Author: Anton Han
Email: xiaodonghan@microsoft.com
"""

def parse_reboot_events(folder_path):
    reboot_events = []

    # Define the paths to check for messages files
    log_patterns = [
        os.path.join(folder_path, 'var', 'log', 'messages*'),
        os.path.join(folder_path, 'sos_strings', 'logs', 'messages*')
    ]

    # Use glob to match all messages files in both locations
    for pattern in log_patterns:
        for log_file in glob.glob(pattern):
            try:
                with open(log_file, 'r') as f:
                    for line in f:
                        # Check for reboot-related keywords
                        if 'reboot' in line.lower() or 'shutdown' in line.lower():
                            reboot_events.append(line.strip())
            except Exception as e:
                reboot_events.append(f"Error reading {log_file}: {str(e)}")

    return reboot_events

def run(folder_path):
    # Parse reboot events
    reboot_events = parse_reboot_events(folder_path)
    if reboot_events:
        return "Reboot Events:\n" + "\n".join(reboot_events)
    else:
        return "No Reboot Events Found."

def create_gui(folder_path):
    result = run(folder_path)

    window = tk.Tk()
    window.title("Parsed OS Reboot")
    # Get the screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window size to be maximized but not fullscreen
    window.geometry(f"{screen_width}x{screen_height - 80}+0+0")

    text_area = tk.Text(window, wrap='word', height=20, width=70)
    text_area.insert('1.0', result)
    text_area.pack(expand=True, fill='both', padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    create_gui(folder)
