import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


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


def log(event):
    print(event)


def print_text(text):
    print(text.get())


def login_clicked():
    """ callback when the login button clicked
    """
    msg = f'You entered email: {email.get()} and password: {password.get()}'
    showinfo(
        title='Information',
        message=msg
    )


if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("300x150")
    root.resizable(False, False)
    root.title('Sign In')

    email = tk.StringVar()
    password = tk.StringVar()

    signin = ttk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=True)

    # email
    email_label = ttk.Label(signin, text="Email Address:")
    email_label.pack(fill='x', expand=True)

    email_entry = ttk.Entry(signin, textvariable=email)
    email_entry.pack(fill='x', expand=True)
    email_entry.focus()

    # password
    password_label = ttk.Label(signin, text="Password:")
    password_label.pack(fill='x', expand=True)

    password_entry = ttk.Entry(signin, textvariable=password, show="*")
    password_entry.pack(fill='x', expand=True)

    # login button
    login_button = ttk.Button(signin, text="Login", command=login_clicked)
    login_button.pack(fill='x', expand=True, pady=10)

    root.mainloop()