"""
    compiled with pyinstaller v. 5.1
    pyinstaller -F -w -i recycle.ico --distpath ../ 'Module Remover.py'
"""

import sys
from tkinter import filedialog
import tkinter.messagebox

import file_system
import GUI

root_path = filedialog.askdirectory(initialdir='.\\', title="Select a root directory for search") or '.\\'
root_search = sys.argv[1] if len(sys.argv) > 1 else 'node_modules'

detected_dirs = file_system.run_search(root_path, root_search)

if len(detected_dirs) == 0:
    tkinter.messagebox.showinfo(title="No matches", message=f"No {root_search} folders was found in tree.")
    sys.exit()

directories_to_rm = GUI.confirm_paths(detected_dirs)

try:
    file_system.rm_folders(directories_to_rm)
    tkinter.messagebox.showinfo(title="Successfully removed", message="Modules successfully deleted.")
except PermissionError:
    tkinter.messagebox.showerror(title="Insufficient permission", message="Lacking permission to remove folder(s).")


