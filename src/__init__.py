# from pathlib import Path
try:
    from os import scandir
    import sys
    from tkinter import filedialog

    # root_path = sys.argv[1] if len(sys.argv) > 1 else '..\\test_dir_1'
    root_path = filedialog.askdirectory(
        initialdir='..\\',
        title="Select a root directory for search"
    ) or '..\\'

    root_search = 'node_modules'

    def scantree(path):
        """Recursively yield DirEntry objects for given directory."""
        for entry in scandir(path):
            if entry.is_dir(follow_symlinks=False):
                if entry.name == root_search:
                    print(entry.path)
                    yield entry
                else:
                    yield from scantree(entry.path)  # see below for Python 2.x

    def run_search(path):
        matches = []
        for entry in scantree(path):
            matches.append(entry)
        return matches

    folders_to_rm = run_search(root_path)
    print(folders_to_rm)

except ImportError:
    print('Error: need python v. >= 3.5')  # use scandir PyPI module on Python < 3.5
