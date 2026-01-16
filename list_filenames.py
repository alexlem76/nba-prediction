import os

def list_filenames(directory_path):
    try:
        # Ensure the path exists and is a directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"'{directory_path}' is not a valid directory.")

        # List only files (not subdirectories)
        files = [os.path.splitext(f)[0] for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return files

    except Exception as e:
        print(f"Error: {e}")
        return []