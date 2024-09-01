import os
import sys

def main(folder_path):
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    if txt_files:
        with open(os.path.join(folder_path, txt_files[0]), 'r') as file:
            content = file.read()
        result = f"Contents of {txt_files[0]}:\n{content}"
    else:
        result = "No .txt files found."
    print(result)

if __name__ == "__main__":
    main(sys.argv[1])
