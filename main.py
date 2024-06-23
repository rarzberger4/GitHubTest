import xml.dom.minidom
import sys, re

def prettify_xml(file_path):
    try:
        # Read the content of the XML file
        with open(file_path, 'r') as file:
            unpretty_xml = file.read()

        # Parse the unpretty XML
        dom = xml.dom.minidom.parseString(unpretty_xml)

        # Prettify the XML
        pretty_xml = dom.toprettyxml()

        # Remove blank lines
        pretty_xml = re.sub(r'^\s*\n', '', pretty_xml, flags=re.MULTILINE)

        # Add a comment indicating that the file was automatically prettified
        pretty_xml = f"<!-- This XML file was automatically prettified -->\n{pretty_xml}"

        # Overwrite the existing file with the prettified XML
        with open(file_path, 'w') as file:
            file.write(pretty_xml)
        
        print(f"XML file at {file_path} has been prettified and overwritten successfully.")

    except FileNotFoundError:
        print(f"File not found: {file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python prettify_xml.py <file_path>")
    else:
        file_path = sys.argv[1]
        prettify_xml(file_path)