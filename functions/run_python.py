import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    """
    Executes a Python file with specified arguments in a given working directory.

    Args:
        working_directory (str): The directory where the command should be executed.
        file_path (str): The path to the Python file to execute.
        args (list, optional): A list of arguments to pass to the Python script. Defaults to [].

    Returns:
        str: The output of the script (stdout and stderr combined), or an error message.
    """
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        command = ["python3", file_path] + args
        completed_process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            cwd=working_directory,
            timeout=30
        )

        output = []
        if completed_process.stdout:
            output.append(f"STDOUT:\n{completed_process.stdout}")
        if completed_process.stderr:
            output.append(f"STDERR:\n{completed_process.stderr}")
        
        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")

        if not output:
            return "No output produced."
            
        return "\n".join(output)

    except subprocess.TimeoutExpired:
        return f"Error: Process timed out after 30 seconds."
    except FileNotFoundError:
        return f'Error: File "{file_path}" not found.'
    except Exception as e:
        return f"Error: executing Python file: {e}"
