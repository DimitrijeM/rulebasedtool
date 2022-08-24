import tkinter as tk
from tkinter import ttk


if __name__ == "__main__":

    root = tk.Tk()
    # keyword argument
    # ttk.Label(root, text='Hi, there').pack()

    # dictionary index
    # label = ttk.Label(root)
    # label['text'] = 'Hi, there'
    # label.pack()

    # config()
    label = ttk.Label(root)
    label.config(text='Hi, there')
    label.pack()

    root.mainloop()