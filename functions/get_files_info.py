import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_directory = os.path.normpath(os.path.join(absolute_path, directory))
        valid_target_directory = os.path.commonpath([absolute_path, target_directory]) == absolute_path

        if not valid_target_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'

        files_info = os.listdir(target_directory)
        formatted_lines = []
        for file in files_info:
            file_path = os.path.join(target_directory, file)
            file_size = os.path.getsize(file_path)
            is_directory = os.path.isdir(file_path)
            result_str = f"- {file_path}: file_size={file_size} bytes, is_dir={is_directory}"
            formatted_lines.append(result_str)

        return "\n".join(formatted_lines)

    except Exception as error:
        return f"Error: {error}"
