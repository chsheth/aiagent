import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    fullpath = os.path.join(abs_working_directory, file_path)
    abs_file_path = os.path.abspath(fullpath)
    #MAX_CHARS = 10000
    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: Cannot reach '{file_path}' as it is outside the permitted working directory"
    elif not os.path.isfile(abs_file_path):
        return f"Error: File not found or is not a regular file: '{file_path}'"
    else:
        try:
            with open(abs_file_path, 'r') as f:
                content = f.read(MAX_CHARS)
            return content
        except Exception as e:
            return f"Error: {e}"






