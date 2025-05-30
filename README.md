# chatgptcodex-test

This repository contains a Python script for demonstrating basic file I/O operations.

## `io_demo.py`

`io_demo.py` is a command-line script that allows users to:

*   **Read a file:** Prompts the user for a filename and displays its content on the console.
*   **Write to a file:** Prompts the user for a filename and content, then writes the content to the specified file.

### How to Run

1.  Make sure you have Python installed on your system.
2.  Navigate to the directory containing `io_demo.py` in your terminal.
3.  Run the script using the following command:

    ```bash
    python io_demo.py
    ```
4.  The script will then prompt you to choose an action (read, write, or exit) and guide you through the selected operation.

### Error Handling

The script includes basic error handling for common issues such as:

*   File not found when trying to read.
*   Permission errors when trying to write.
*   Other unexpected I/O errors.

User-friendly messages will be displayed in case of such errors.