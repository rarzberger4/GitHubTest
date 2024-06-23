import os
import sys
import winreg as reg

def add_right_click_option():
    try:
        # Get the path to the Python executable
        python_exe = sys.executable

        # Get the path to the script
        script_path = os.path.abspath(__file__)

        # Get the path to run.py
        run_script_path = os.path.join(os.path.dirname(script_path), "run.py")

        # Create a new key for the context menu handler
        key_path = r"Software\Classes\*\shell\PrettifyXML"
        try:
            key = reg.CreateKey(reg.HKEY_CURRENT_USER, key_path)
            reg.SetValueEx(key, "", 0, reg.REG_SZ, "Prettify XML")
            reg.CloseKey(key)
        except Exception as e:
            print(f"Error creating key: {e}")

        # Set the command to run run.py with the file path as argument
        command_path = f'"{python_exe}"'
        command_args = f'"{run_script_path}" "%1"'
        command = f'{command_path} {command_args}'
        try:
            key = reg.CreateKey(reg.HKEY_CURRENT_USER, key_path + r"\command")
            reg.SetValueEx(key, "", 0, reg.REG_SZ, command)
            reg.CloseKey(key)
        except Exception as e:
            print(f"Error setting command: {e}")

        print("Right-click option 'Prettify XML' added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    add_right_click_option()
