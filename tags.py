import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=606
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_727=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_727["font"] = ft
        GLabel_727["fg"] = "#01aaed"
        GLabel_727["justify"] = "center"
        GLabel_727["text"] = "Додавання користувачів"
        GLabel_727.place(x=0,y=0,width=244,height=46)

        GLineEdit_525=tk.Entry(root)
        GLineEdit_525["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_525["font"] = ft
        GLineEdit_525["fg"] = "#333333"
        GLineEdit_525["justify"] = "center"
        GLineEdit_525["text"] = "login"
        GLineEdit_525.place(x=90,y=40,width=153,height=30)

        GLabel_100=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_100["font"] = ft
        GLabel_100["fg"] = "#333333"
        GLabel_100["justify"] = "center"
        GLabel_100["text"] = "Логін"
        GLabel_100.place(x=10,y=40,width=70,height=25)

        GLabel_705=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["justify"] = "center"
        GLabel_705["text"] = "Пароль"
        GLabel_705.place(x=20,y=90,width=70,height=25)

        GLineEdit_596=tk.Entry(root)
        GLineEdit_596["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_596["font"] = ft
        GLineEdit_596["fg"] = "#333333"
        GLineEdit_596["justify"] = "center"
        GLineEdit_596["text"] = "password"
        GLineEdit_596.place(x=90,y=90,width=152,height=30)

        GButton_800=tk.Button(root)
        GButton_800["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_800["font"] = ft
        GButton_800["fg"] = "#000000"
        GButton_800["justify"] = "center"
        GButton_800["text"] = "Додати"
        GButton_800.place(x=90,y=140,width=79,height=30)
        GButton_800["command"] = self.GButton_800_command

        GLabel_481=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_481["font"] = ft
        GLabel_481["fg"] = "#333333"
        GLabel_481["justify"] = "center"
        GLabel_481["text"] = "Введіть к-сть ботів"
        GLabel_481.place(x=260,y=70,width=152,height=30)

        GLineEdit_928=tk.Entry(root)
        GLineEdit_928["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_928["font"] = ft
        GLineEdit_928["fg"] = "#333333"
        GLineEdit_928["justify"] = "center"
        GLineEdit_928["text"] = "Entry"
        GLineEdit_928.place(x=270,y=100,width=307,height=31)

        GLabel_670=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_670["font"] = ft
        GLabel_670["fg"] = "#333333"
        GLabel_670["justify"] = "center"
        GLabel_670["text"] = "Введіть посилання на пост"
        GLabel_670.place(x=270,y=130,width=208,height=30)

        GLineEdit_226=tk.Entry(root)
        GLineEdit_226["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_226["font"] = ft
        GLineEdit_226["fg"] = "#333333"
        GLineEdit_226["justify"] = "center"
        GLineEdit_226["text"] = "Entry"
        GLineEdit_226.place(x=270,y=160,width=308,height=32)

        GButton_457=tk.Button(root)
        GButton_457["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_457["font"] = ft
        GButton_457["fg"] = "#000000"
        GButton_457["justify"] = "center"
        GButton_457["text"] = "Button"
        GButton_457.place(x=400,y=210,width=70,height=25)
        GButton_457["command"] = self.GButton_457_command

        GLabel_692=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_692["font"] = ft
        GLabel_692["fg"] = "#333333"
        GLabel_692["justify"] = "center"
        GLabel_692["text"] = "Тематика"
        GLabel_692.place(x=270,y=10,width=70,height=25)

        GLineEdit_643=tk.Entry(root)
        GLineEdit_643["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_643["font"] = ft
        GLineEdit_643["fg"] = "#333333"
        GLineEdit_643["justify"] = "center"
        GLineEdit_643["text"] = "Entry"
        GLineEdit_643.place(x=270,y=40,width=308,height=30)

        GLabel_902=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_902["font"] = ft
        GLabel_902["fg"] = "#333333"
        GLabel_902["justify"] = "center"
        GLabel_902["text"] = ""
        GLabel_902.place(x=10,y=340,width=70,height=25)

        GRadio_500=tk.Radiobutton(root)
        GRadio_500["cursor"] = "spider"
        ft = tkFont.Font(family='Times',size=10)
        GRadio_500["font"] = ft
        GRadio_500["fg"] = "#333333"
        GRadio_500["justify"] = "center"
        GRadio_500["text"] = "Випадковий аккаунт"
        GRadio_500.place(x=0,y=300,width=157,height=30)
        GRadio_500["command"] = self.GRadio_500_command

        GRadio_69=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_69["font"] = ft
        GRadio_69["fg"] = "#333333"
        GRadio_69["justify"] = "center"
        GRadio_69["text"] = "По логіну"
        GRadio_69.place(x=0,y=330,width=98,height=34)
        GRadio_69["command"] = self.GRadio_69_command

        GLineEdit_266=tk.Entry(root)
        GLineEdit_266["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_266["font"] = ft
        GLineEdit_266["fg"] = "#333333"
        GLineEdit_266["justify"] = "center"
        GLineEdit_266["text"] = "Entry"
        GLineEdit_266.place(x=20,y=360,width=141,height=32)

        GButton_762=tk.Button(root)
        GButton_762["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_762["font"] = ft
        GButton_762["fg"] = "#000000"
        GButton_762["justify"] = "center"
        GButton_762["text"] = "Створити"
        GButton_762.place(x=90,y=560,width=70,height=25)
        GButton_762["command"] = self.GButton_762_command

        GLabel_71=tk.Label(root)
        GLabel_71["bg"] = "#fad400"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_71["font"] = ft
        GLabel_71["fg"] = "#01aaed"
        GLabel_71["justify"] = "center"
        GLabel_71["text"] = "Створити пост"
        GLabel_71.place(x=0,y=270,width=172,height=30)

        GLabel_478=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_478["font"] = ft
        GLabel_478["fg"] = "#333333"
        GLabel_478["justify"] = "center"
        GLabel_478["text"] = "Введіть посилання на картинку"
        GLabel_478.place(x=0,y=390,width=249,height=51)

        GLineEdit_451=tk.Entry(root)
        GLineEdit_451["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_451["font"] = ft
        GLineEdit_451["fg"] = "#333333"
        GLineEdit_451["justify"] = "center"
        GLineEdit_451["text"] = "Entry"
        GLineEdit_451.place(x=20,y=440,width=205,height=30)

        GLabel_508=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_508["font"] = ft
        GLabel_508["fg"] = "#333333"
        GLabel_508["justify"] = "center"
        GLabel_508["text"] = "Введіть тематику для тексту"
        GLabel_508.place(x=0,y=470,width=220,height=33)

        GLineEdit_924=tk.Entry(root)
        GLineEdit_924["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_924["font"] = ft
        GLineEdit_924["fg"] = "#333333"
        GLineEdit_924["justify"] = "center"
        GLineEdit_924["text"] = "Entry"
        GLineEdit_924.place(x=20,y=510,width=204,height=30)

    def GButton_800_command(self):
        print("command")


    def GButton_457_command(self):
        print("command")


    def GRadio_500_command(self):
        print("command")


    def GRadio_69_command(self):
        print("command")


    def GButton_762_command(self):
        print("command")


