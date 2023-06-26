# -*- coding: utf-8 -*-
from instagrapi import Client
import tkinter as tk

from shell import cli
from tags import App




def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    cli()
    main()
