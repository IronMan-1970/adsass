import tkinter as tk
from tags import App


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    app.userPasswordEntry.get