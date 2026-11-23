
import os
import string
from config import MAX_CHARS

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Retrieves the content of a file in the working directory, up to a maximum number of characters",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target_file_path = os.path.commonpath([absolute_path, target_file_path]) == absolute_path

        if not valid_target_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" is not a file'

        with open(target_file_path, 'r') as file:
            content = file.read(MAX_CHARS)
            if file.read(1):
                 content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    
    except Exception as e:
        return f"Error: {e}"
