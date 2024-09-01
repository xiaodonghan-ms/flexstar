import os
import sys
import tkinter as tk

def run(folder_path):
    log_files = [f for f in os.listdir(folder_path) if f.endswith('.log')]
    log_count = len(log_files)
    result = f"Total .log files: {log_count}\nLog Files:\n" + "\n".join(log_files)
    return result

def create_gui(folder_path):
    result = run(folder_path)

    window = tk.Tk()
    window.title("Log File Count Results")

    label = tk.Label(window, text="Log File Count Results", font=("Arial", 14))
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
