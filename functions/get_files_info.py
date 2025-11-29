import os

def get_files_info(working_directory, directory="."):
    # print('---')
    # print(working_directory)
    # print('---')
    # print(directory)
    abs_working_directory = os.path.abspath(working_directory)

    #print(f"Working directory: {abs_working_directory}")
    fullpath=os.path.join(abs_working_directory, directory)
    #print(f"Full path directory: {fullpath}")
    abs_directory = os.path.abspath(fullpath)
    #print(f"Absolute directory: {abs_directory}")
    print(f"Result for '{directory}' directory:")
    if not os.path.isdir(abs_directory):
        print(f'    Error: "{directory}" is not a directory')
    elif not abs_directory.startswith(abs_working_directory):
        print(f'    Error: Cannot list "{directory}" as it is outside the permitted working directory')
    else:
        list_dir = os.listdir(abs_directory)
        for name in list_dir:
            filepath = os.path.join(abs_directory, name)
            filesize = os.path.getsize(filepath)
            is_dir = os.path.isdir(filepath)
            #print(is_dir)
            print(f"    - {name}: file_size={filesize} bytes, is_dir={is_dir}")
