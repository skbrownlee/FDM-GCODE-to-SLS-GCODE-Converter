import tkinter as tk
from tkinter import filedialog

def remove_words_starting_with_a_or_e(file_path):
    """
    Removes words from the file that start with 'A' or 'E'.
    
    :param file_path: Path to the file to be modified.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        modified_lines = []
        for line in lines:
            words = line.split()
            modified_words = [word for word in words if word[0].upper() not in ['A', 'E']]
            modified_line = ' '.join(modified_words)
            modified_lines.append(modified_line)

        with open(file_path, 'w') as file:
            file.write('\n'.join(modified_lines))

        print(f"File '{file_path}' has been modified successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def select_and_process_file():
    root = tk.Tk()
    root.withdraw() # We don't want a full GUI, so keep the root window from appearing
    file_path = filedialog.askopenfilename() # Show an "Open" dialog box and return the path to the selected file
    if file_path:
        remove_words_starting_with_a_or_e(file_path)
    else:
        print("No file selected.")

if __name__ == "__main__":
    select_and_process_file()
