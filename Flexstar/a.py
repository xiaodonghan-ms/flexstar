import os
import sys

def main(folder_path):
    files = os.listdir(folder_path)
    file_count = len(files)
    result = f"Total files: {file_count}\nFiles:\n" + "\n".join(files)
    print(result)

if __name__ == "__main__":
    main(sys.argv[1])
