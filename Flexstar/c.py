import os
import sys
import tkinter as tk

def run(folder_path):
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    if txt_files:
        with open(os.path.join(folder_path, txt_files[0]), 'r') as file:
            content = file.read()
        result = f"Contents of {txt_files[0]}:\n{content}"
    else:
        result = "No .txt files found."
    return result

def create_gui(folder_path):
    result = run(folder_path)
    window = tk.Toplevel()
    window.title("Text File Content")

    label = tk.Label(window, text="Text File Content", font=("Arial", 14))
    label.pack(pady=10)

    text_area = tk.Text(window, wrap='word', height=15, width=50)
    text_area.insert('1.0', result)
    text_area.pack(expand=True, fill='both', padx=10, pady=10)

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(pady=10)

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    print(run(folder))
