import os

def main(folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)
        # Filter for log files
        log_files = [f for f in files if f.endswith('.log')]
        
        # Simulate log parsing results
        results = f"Module B: Found {len(log_files)} log files in '{folder_path}':\n" + "\n".join(log_files)
        return results
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    import sys
    print(main(sys.argv[1]))

