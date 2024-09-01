import os
import sys

def main(folder_path):
    log_files = [f for f in os.listdir(folder_path) if f.endswith('.log')]
    log_count = len(log_files)
    result = f"Total .log files: {log_count}\nLog Files:\n" + "\n".join(log_files)
    print(result)

if __name__ == "__main__":
    main(sys.argv[1])
