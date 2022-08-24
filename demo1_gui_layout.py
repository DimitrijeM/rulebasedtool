import tkinter as tk


class HelloWorld(tk.Frame):
    def __init__(self, parent):
        super(HelloWorld, self).__init__(parent)

        self.label = tk.Label(self, text="Hello, World!")
        self.label.pack(padx=40, pady=40)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rule-based tool demo")

    window_width = 600
    window_height = 400
    # root.geometry('600x400+50+50')  # widhtxheight+-x+-y

    # center the window on the screen
    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # prevent the window from resizing
    root.resizable(600, 400)
    root.iconbitmap('./assets/pythontutorial-1-150x150.ico')

    main = HelloWorld(root)
    main.pack(fill="both", expand=True)

    root.mainloop()
