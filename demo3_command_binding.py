import tkinter as tk
from tkinter import ttk

def button_clicked():
    print('Button clicked')


def add_new_label(root, label_text):
    ttk.Label(root, text=label_text).pack()


def setup_window_look(root_window):
    root_window.title("Rule-based tool demo")
    window_width = 600
    window_height = 400

    screen_width = root_window.winfo_screenwidth()
    screen_height = root_window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
    root_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


if __name__ == "__main__":

    root = tk.Tk()
    ttk.Label(root, text='Create Document').pack()

    setup_window_look(root)

    # ttk.Button(root, text='Add Field', command=button_clicked).pack()
    ttk.Button(root,
               text='Add Field',
               command=lambda: add_new_label(root, 'Generic Field'))\
        .pack()

    ttk.Button(root, text='Add Number Attribute', command=lambda: add_new_label(root, 'Number')).pack()
    ttk.Button(root, text='Add String Attribute', command=lambda: add_new_label(root, 'String')).pack()
    ttk.Button(root, text='Add Categorical Attribute', command=lambda: add_new_label(root, 'Categories')).pack()

    root.mainloop()