try:
    from os import scandir
    import sys
    from tkinter import *
    from tkinter import filedialog
    import tkinter.messagebox
    import shutil
except ImportError:
    print('Error: need python v. >= 3.5')  # use scandir PyPI module on Python < 3.5
    sys.exit()


def scan_tree(path):
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            if entry.name == root_search:
                yield entry
            else:
                yield from scan_tree(entry.path)  # see below for Python 2.x


def run_search(path):
    matches = []
    for entry in scan_tree(path):
        matches.append({'path_obj': entry})
    return matches


def final_confirm(temp_arr, window):
    for index in range(0, len(folders_to_rm)):
        folders_to_rm[index].update(
            {"to_remove": str(not temp_arr[index].get())}
        )
    if tkinter.messagebox.askyesno(
        title="Warning!",
        message="Deleted folders can't be retrieved. Are you sure?",
        icon="warning"
    ):
        window.destroy()
    else:
        window.destroy()
        sys.exit()


def confirm_paths():
    window = Tk()
    temp_arr = []

    # window.geometry("420x420")
    window.title("Confirm paths before deleting folders")
    window.iconphoto(
        True,
        PhotoImage(file='warning.png')
    )
    label_header = Label(window, text="Confirm deletions")
    button_confirm = Button(window, text="Confirm", command=lambda: final_confirm(temp_arr, window))

    label_header.pack()

    for path_dict in folders_to_rm:
        temp_arr.append(x := BooleanVar())

        ch_box = Checkbutton(
            window,
            text=path_dict['path_obj'].path,
            variable=x,
            onvalue=0,
            offvalue=1
        )
        ch_box.pack(anchor='w')

    button_confirm.pack()
    window.mainloop()


def rm_folders():
    try:
        for path_dict in folders_to_rm:
            if path_dict['to_remove'] == 'True':
                shutil.rmtree(path_dict['path_obj'].path)
        tkinter.messagebox.showinfo(
            title="Successfully removed",
            message="Modules successfully deleted."
        )
    except PermissionError:
        tkinter.messagebox.showerror(
            title="Insufficient permission",
            message="Lacking permission to remove folder(s)."
        )


root_path = filedialog.askdirectory(
    initialdir='..\\',
    title="Select a root directory for search"
) or '..\\'
root_search = sys.argv[1] if len(sys.argv) > 1 else 'node_modules'

folders_to_rm = run_search(root_path)
if len(folders_to_rm) == 0:
    tkinter.messagebox.showinfo(
        title="No matches",
        message=f"No {root_search} folders was found in tree."
    )
    sys.exit()
confirm_paths()
rm_folders()
