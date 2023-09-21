from tkinter import *
import tkinter.messagebox
import sys


def confirm_paths(directories):
    def final_confirm(bool_list, window):
        if len(directories) == 0:
            tkinter.messagebox.showinfo(title="No directories selected", message="No directories to remove")
            window.destroy()
            sys.exit()

        for index in range(0, len(directories)):
            directories[index].update(
                {"to_remove": str(not bool_list[index].get())}
            )
        if tkinter.messagebox.askyesno(title="Warning!",
                                       message="Deleted folders can't be retrieved. Are you sure?",
                                       icon="warning"):
            window.destroy()
        else:
            window.destroy()
            tkinter.messagebox.showinfo(title="No removal", message=f"No directories removed!")
            sys.exit()

    window = Tk()
    window.title("Confirm paths before deleting folders")

    label_header = Label(window, text="Confirm deletions")
    label_header.pack()

    temp_arr = []
    for path_dict in directories:
        temp_arr.append(x := BooleanVar())

        ch_box = Checkbutton(
            window,
            text=path_dict['path_obj'].path,
            variable=x,
            onvalue=0,
            offvalue=1
        )
        ch_box.pack(anchor='w')

    button_confirm = Button(window, text="Confirm", command=lambda: final_confirm(temp_arr, window))
    button_confirm.pack()

    window.after(1, lambda: window.focus_force())
    window.mainloop()
    return directories
