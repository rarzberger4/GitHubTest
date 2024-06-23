import sys
import subprocess
import os

def main():
    # Check if exactly one argument is provided
    if len(sys.argv) != 2:
        print("Usage: python main.py <argument>")
        return

    # Get the argument provided
    argument = sys.argv[1]

    # Get the absolute path to main.py
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main.py'))

    # Run main.py with the provided argument
    subprocess.run(["python", path, argument])

if __name__ == "__main__":
    main()
