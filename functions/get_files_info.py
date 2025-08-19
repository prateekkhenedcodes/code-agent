import os 

def get_files_info(working_directory, directory="."):

    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)

    if not absolute_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    try:
        list_dir = os.listdir(full_path)
    except Exception as e:
        return f"Error: {str(e)}"
    result = ""
    for item in list_dir:
        item_path = os.path.join(full_path, item)
        try:
            result += f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}\n"
        except Exception as e:
            return f"Error: {str(e)}"
    return result