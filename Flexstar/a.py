import os

def main(folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)
        # Filter out directories, only keep files
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
        
        # Simulate log parsing results
        results = f"Module A: Found {len(files)} files in '{folder_path}':\n" + "\n".join(files)
        return results
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    import sys
    print(main(sys.argv[1]))

