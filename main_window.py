"""The module is used for the GUI of the Help Compiler"""

from tkinter import filedialog
import tkinter as tk

def build_folder():

    """ The function returns a selected folder."""

    folder = filedialog.askdirectory(

        title="Select a Build folder",
        initialdir="C:/"

    )

    if folder:
        var.set(folder)


def UserFileInput(status,name):
    optionFrame = Frame(root)
    optionLabel = Label(optionFrame)
    optionLabel["text"] = name
    optionLabel.pack(side=LEFT)
    text = status
    var = StringVar(root)
    var.set(text)
    w = Entry(optionFrame, textvariable= var)
    w.pack(side = LEFT)
    optionFrame.pack()
    return w, var

def Print_entry():
    print(var.get())


if __name__ == '__main__':

    root = tk.Tk()

    root.iconbitmap("D:\\py\\helpCompile\\misc_pa_logo.ico")
    root.title("Help Compiler (GUI version)")
    root.minsize(800, 250)
    root.geometry("800x200")

    import_button_build = tk.Button(root, text="Browse", command=build_folder)
    import_button_build.grid(row=2, column=2, padx=65, pady=15)

    getBut = Button(root, text='print entry text', command = Print_entry)
    getBut.pack(side = BOTTOM)

    w, var = UserFileInput("", "Directory")

    root.mainloop()
