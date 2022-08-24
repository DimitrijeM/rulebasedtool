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


def return_pressed(event):
    print('Return key pressed.')


def log(event):
    print(event)


def print_text(text):
    print(text.get())


if __name__ == "__main__":


    root = tk.Tk()

    btn = ttk.Button(root, text='Save')
    btn.bind('<Return>', return_pressed)
    btn.bind('<Return>', log, add='+')

    text = tk.StringVar()
    textbox = ttk.Entry(root, textvariable=text)

    btn.focus()
    btn.pack(expand=True)

    root.mainloop()