import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        # setting title
        root.title("Інста ГУР бот")
        # setting window size
        width = 606
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        userAddLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        userAddLabel["font"] = ft
        userAddLabel["fg"] = "#01aaed"
        userAddLabel["justify"] = "center"
        userAddLabel["text"] = "Додавання користувачів"
        userAddLabel.place(x=0,y=0,width=244,height=46)

        userLoginEntry=tk.Entry(root)
        userLoginEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        userLoginEntry["font"] = ft
        userLoginEntry["fg"] = "#333333"
        userLoginEntry["justify"] = "center"
        userLoginEntry["text"] = "login"
        userLoginEntry.place(x=90,y=40,width=153,height=30)
        def get_login_entry_text(self):
            login = userLoginEntry.get()
            return login

        userLoginLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        userLoginLabel["font"] = ft
        userLoginLabel["fg"] = "#333333"
        userLoginLabel["justify"] = "center"
        userLoginLabel["text"] = "Логін"
        userLoginLabel.place(x=10,y=40,width=70,height=25)

        userPasswordLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        userPasswordLabel["font"] = ft
        userPasswordLabel["fg"] = "#333333"
        userPasswordLabel["justify"] = "center"
        userPasswordLabel["text"] = "Пароль"
        userPasswordLabel.place(x=20,y=90,width=70,height=25)

        userPasswordEntry=tk.Entry(root)
        userPasswordEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        userPasswordEntry["font"] = ft
        userPasswordEntry["fg"] = "#333333"
        userPasswordEntry["justify"] = "center"
        userPasswordEntry["text"] = "password"
        userPasswordEntry.place(x=90,y=90,width=152,height=30)
        def get_password_entry_text(self):
            password = userPasswordEntry.get()
            return password

        userAddButton = tk.Button(root)
        userAddButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        userAddButton["font"] = ft
        userAddButton["fg"] = "#000000"
        userAddButton["justify"] = "center"
        userAddButton["text"] = "Додати"
        userAddButton.place(x=150, y=140, width=94, height=28)


        userAddButton["command"] = self.userAddButton_command

        addBotCountLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        addBotCountLabel["font"] = ft
        addBotCountLabel["fg"] = "#333333"
        addBotCountLabel["justify"] = "center"
        addBotCountLabel["text"] = "Введіть к-сть ботів"
        addBotCountLabel.place(x=260,y=70,width=152,height=30)

        addBotCountEntry=tk.Entry(root)
        addBotCountEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        addBotCountEntry["font"] = ft
        addBotCountEntry["fg"] = "#333333"
        addBotCountEntry["justify"] = "center"
        addBotCountEntry["text"] = "Entry"
        addBotCountEntry.place(x=270,y=100,width=307,height=31)

        def get_bot_count_entry_text(self):
            botCount = addBotCountEntry.get()
            return botCount

        postLinkLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        postLinkLabel["font"] = ft
        postLinkLabel["fg"] = "#333333"
        postLinkLabel["justify"] = "center"
        postLinkLabel["text"] = "Введіть посилання на пост"
        postLinkLabel.place(x=270,y=130,width=208,height=30)

        postLinkEntry=tk.Entry(root)
        postLinkEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        postLinkEntry["font"] = ft
        postLinkEntry["fg"] = "#333333"
        postLinkEntry["justify"] = "center"
        postLinkEntry["text"] = "Entry"
        postLinkEntry.place(x=270,y=160,width=308,height=32)
        def get_postLink_entry_text(self):
            postLink = postLinkEntry.get()
            return postLink


        commentPostButton=tk.Button(root)
        commentPostButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        commentPostButton["font"] = ft
        commentPostButton["fg"] = "#000000"
        commentPostButton["justify"] = "center"
        commentPostButton["text"] = "Button"
        commentPostButton.place(x=400,y=210,width=70,height=25)
        commentPostButton["command"] = self.commentPostButton_command

        subjectLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        subjectLabel["font"] = ft
        subjectLabel["fg"] = "#333333"
        subjectLabel["justify"] = "center"
        subjectLabel["text"] = "Тематика"
        subjectLabel.place(x=270,y=10,width=70,height=25)

        subjectEntry=tk.Entry(root)
        subjectEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        subjectEntry["font"] = ft
        subjectEntry["fg"] = "#333333"
        subjectEntry["justify"] = "center"
        subjectEntry["text"] = "Entry"
        subjectEntry.place(x=270,y=40,width=308,height=30)
        def get_subject_entry_text(self):
            subject = subjectEntry.get()
            return subject

        randomAccountRadioButton=tk.Radiobutton(root)
        randomAccountRadioButton["cursor"] = "spider"
        ft = tkFont.Font(family='Times',size=10)
        randomAccountRadioButton["font"] = ft
        randomAccountRadioButton["fg"] = "#333333"
        randomAccountRadioButton["justify"] = "center"
        randomAccountRadioButton["text"] = "Випадковий аккаунт"
        randomAccountRadioButton.place(x=0,y=300,width=157,height=30)
        randomAccountRadioButton["command"] = self.randomAccountRadioButton_command

        byUsernameAccountRadioButton=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        byUsernameAccountRadioButton["font"] = ft
        byUsernameAccountRadioButton["fg"] = "#333333"
        byUsernameAccountRadioButton["justify"] = "center"
        byUsernameAccountRadioButton["text"] = "По логіну"
        byUsernameAccountRadioButton.place(x=0,y=330,width=98,height=34)
        byUsernameAccountRadioButton["command"] = self.byUsernameAccountRadioButton_command

        usernameAccountEntry=tk.Entry(root)
        usernameAccountEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        usernameAccountEntry["font"] = ft
        usernameAccountEntry["fg"] = "#333333"
        usernameAccountEntry["justify"] = "center"
        usernameAccountEntry["text"] = "Entry"
        usernameAccountEntry.place(x=20,y=360,width=141,height=32)
        def get_usernameAccount_entry_text(self):
            usernameAccount = usernameAccountEntry.get()
            return usernameAccount

        createButton=tk.Button(root)
        createButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        createButton["font"] = ft
        createButton["fg"] = "#000000"
        createButton["justify"] = "center"
        createButton["text"] = "Створити"
        createButton.place(x=90,y=560,width=70,height=25)
        createButton["command"] = self.createButton_command

        createPostLabel=tk.Label(root)
        createPostLabel["bg"] = "#fad400"
        ft = tkFont.Font(family='Times',size=18)
        createPostLabel["font"] = ft
        createPostLabel["fg"] = "#01aaed"
        createPostLabel["justify"] = "center"
        createPostLabel["text"] = "Створити пост"
        createPostLabel.place(x=0,y=270,width=172,height=30)

        imageLinkLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        imageLinkLabel["font"] = ft
        imageLinkLabel["fg"] = "#333333"
        imageLinkLabel["justify"] = "center"
        imageLinkLabel["text"] = "Введіть посилання на картинку"
        imageLinkLabel.place(x=0,y=390,width=249,height=51)

        imageLinkEntry=tk.Entry(root)
        imageLinkEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        imageLinkEntry["font"] = ft
        imageLinkEntry["fg"] = "#333333"
        imageLinkEntry["justify"] = "center"
        imageLinkEntry["text"] = "Entry"
        imageLinkEntry.place(x=20,y=440,width=205,height=30)
        def get_imageLink_entry_text(self):
            imageLink = imageLinkEntry.get()
            return imageLink

        subjectPostLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        subjectPostLabel["font"] = ft
        subjectPostLabel["fg"] = "#333333"
        subjectPostLabel["justify"] = "center"
        subjectPostLabel["text"] = "Введіть тематику для тексту"
        subjectPostLabel.place(x=0,y=470,width=220,height=33)

        subjectPostEntry=tk.Entry(root)
        subjectPostEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        subjectPostEntry["font"] = ft
        subjectPostEntry["fg"] = "#333333"
        subjectPostEntry["justify"] = "center"
        subjectPostEntry["text"] = "Entry"
        subjectPostEntry.place(x=20,y=510,width=204,height=30)
        def get_subjectPost_entry_text(self):
            subjectPost = subjectPostEntry.get()
            return subjectPost

    def userAddButton_command(self, app):
        file = open("users.txt", "w")
        file.write(app.get_usernameAccount_entry_text+"/"+app.get_password_entry_text+"\n")
        file.close()
    def createButton_command(self):
        pass
    def commentPostButton_command(self):
        pass
    def randomAccountRadioButton_command(self):
        pass
    def byUsernameAccountRadioButton_command(self):
        pass