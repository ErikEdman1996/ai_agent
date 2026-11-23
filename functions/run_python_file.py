import subprocess
import os

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file in the working directory with optional arguments",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Python file to execute, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target_file_path = os.path.commonpath([absolute_path, target_file_path]) == absolute_path

        if not valid_target_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist'
        if not target_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file_path]
        if args:
            command.extend(args)

        result = subprocess.run(command, capture_output=True, text=True, cwd=absolute_path, timeout=30)
        output_str = ""
        
        if result.returncode != 0:
            output_str = f"Process exited with code {result.returncode}"
        if result.stdout is None or result.stderr is None:
            output_str += "\nNo output produced"
        else:
            output_str += f"\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        return output_str.strip()
            
    except Exception as e:
        return f"Error: executing Python file: {e}"
