import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a file in the working directory, creating the file if it does not exist",
        "parameters": {
            "type": "object",
            "properties": {        
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to the file",
                },
            },
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target_file_path = os.path.commonpath([absolute_path, target_file_path]) == absolute_path

        if not valid_target_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file_path):
            return f'Error: "{file_path}" is a directory, cannot write content to it'

        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

        with open(target_file_path, 'w') as file:
            if file.write(content) > 0:
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            else:
                return f'Error: Failed to write to "{file_path}"'

    except Exception as e:
        return f"Error: {e}"