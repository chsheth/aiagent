
import os
import subprocess
import sys


def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        # Prefer running as a module (python -m) from the project root so package imports work.
        env = os.environ.copy()
        project_root = os.path.abspath(os.path.join(abs_working_dir, os.pardir))
        existing_py_path = env.get("PYTHONPATH", "")
        env["PYTHONPATH"] = project_root + (os.pathsep + existing_py_path if existing_py_path else "")

        # Compute module name relative to project root and run using -m
        rel_path = os.path.relpath(abs_file_path, project_root)
        module_name = None
        if rel_path.endswith(".py"):
            module_name = rel_path[:-3].replace(os.sep, ".")

        if module_name:
            commands = [sys.executable, "-m", module_name]
            run_cwd = project_root
        else:
            commands = [sys.executable, abs_file_path]
            run_cwd = abs_working_dir

        if args:
            commands.extend(args)

        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=run_cwd,
            env=env,
        )
        output = []
        if result.stdout:
            print(result.stdout)
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
            print(result.stderr)
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"


#------from boot dev version------
# import os
# import subprocess


# def run_python_file(working_directory, file_path, args=None):
#     abs_working_dir = os.path.abspath(working_directory)
#     abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
#     if not abs_file_path.startswith(abs_working_dir):
#         return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
#     if not os.path.exists(abs_file_path):
#         return f'Error: File "{file_path}" not found.'
#     if not file_path.endswith(".py"):
#         return f'Error: "{file_path}" is not a Python file.'
#     try:
#         commands = ["python", abs_file_path]
#         if args:
#             commands.extend(args)
#         result = subprocess.run(
#             commands,
#             capture_output=True,
#             text=True,
#             timeout=30,
#             cwd=abs_working_dir,
#         )
#         output = []
#         if result.stdout:
#             output.append(f"STDOUT:\n{result.stdout}")
#         if result.stderr:
#             output.append(f"STDERR:\n{result.stderr}")

#         if result.returncode != 0:
#             output.append(f"Process exited with code {result.returncode}")

#         return "\n".join(output) if output else "No output produced."
#     except Exception as e:
#         return f"Error: executing Python file: {e}"


# -------------------
# def run_python_file(working_directory, file_path, args=[]):
#     abs_working_directory = os.path.abspath(working_directory)
#     abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
#     if not abs_file_path.startswith(abs_working_directory):
#         return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'
#     if not os.path.exists(abs_file_path):
#         return f'Error: File "{file_path}" not found.'
#     if not file_path.endswith(".py"):
#         return f'Error: "{file_path}" is not a Python file.'
#     try:
#         completed_process = subprocess.run(
#             ["python", abs_file_path] + args,
#             cwd=abs_working_directory,
#             capture_output=True,
#             text=True,
#             check=True,
#             timeout=30
#         )
        
#         if completed_process.stdout == '':
#             return f"No output produced"
#         else:
#             return f"STDOUT: {completed_process.stdout} \n STDERR: {completed_process.stderr}"
#     except subprocess.CalledProcessError as e:
#         return f"Process exited with code {completed_process.returncode}"
#     except Exception as e:
#         return f"Error: executing Python file: {e}"