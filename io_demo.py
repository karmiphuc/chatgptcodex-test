# This is a Python script to demonstrate I/O operations.

def read_file():
  """Prompts the user for a filename, reads the file, and displays its content."""
  filename = input("Enter the filename to read: ")
  try:
    with open(filename, 'r') as f:
      content = f.read()
      print("\nFile content:\n")
      print(content)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def write_file():
  """Prompts the user for a filename and content, then writes the content to the file."""
  filename = input("Enter the filename to write to: ")
  content = input("Enter the content to write:\n")
  try:
    with open(filename, 'w') as f:
      f.write(content)
    print(f"\nContent successfully written to '{filename}'.")
  except PermissionError:
    print(f"Error: Permission denied to write to '{filename}'.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
  while True:
    choice = input("\nChoose an action:\n1. Read file\n2. Write file\n3. Exit\nEnter your choice (1/2/3): ")
    if choice == '1':
      read_file()
    elif choice == '2':
      write_file()
    elif choice == '3':
      print("Exiting program.")
      break
    else:
      print("Invalid choice. Please enter 1, 2, or 3.")
