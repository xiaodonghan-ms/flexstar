import os

def main(folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)
        # Filter for text files
        text_files = [f for f in files if f.endswith('.txt')]
        
        if text_files:
            # Read the contents of the first text file found
            with open(os.path.join(folder_path, text_files[0]), 'r') as file:
                content = file.read()
            results = f"Module C: Contents of '{text_files[0]}':\n\n{content}"
        else:
            results = f"Module C: No text files found in '{folder_path}'."
        
        return results
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    import sys
    print(main(sys.argv[1]))

