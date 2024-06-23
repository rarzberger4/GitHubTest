import winreg as reg

def remove_right_click_option():
    try:
        # Specify the key path to delete
        key_path = r"Software\Classes\*\shell\PrettifyXML"

        # Delete the command subkey
        try:
            reg.DeleteKey(reg.HKEY_CURRENT_USER, key_path + r"\command")
        except Exception as e:
            print(f"Error deleting command subkey: {e}")

        # Delete the main key
        try:
            reg.DeleteKey(reg.HKEY_CURRENT_USER, key_path)
        except Exception as e:
            print(f"Error deleting main key: {e}")

        print("Right-click option 'Prettify XML' removed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    remove_right_click_option()