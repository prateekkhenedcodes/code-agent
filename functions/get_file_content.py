import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):

    abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        content = ""
        with open(abs_path, "r") as f:
            content = f.read(MAX_CHARS)

        if os.path.getsize(abs_path) > MAX_CHARS:
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f'Error: reading file "{file_path}": {e}'

    return content
