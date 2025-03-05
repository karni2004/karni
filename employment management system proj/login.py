from customtkinter import *
from tkinter import messagebox
from PIL import Image
from customtkinter import CTkImage, CTkLabel, CTkEntry, CTkButton






def login():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror("Error","All fields are required")
    elif usernameEntry.get()=="lotty" and passwordEntry.get()=="1234":
        messagebox.showinfo("Success","Login is successful")
        root.destroy()
        import ems
    else:
       messagebox.showerror("Error","Wrong Credentials")

root=CTk()
root.geometry('930x478')
root.resizable(False,False)
root.title("login page")
root.iconbitmap(r'emp.ico')
image = CTkImage(Image.open("lot.jpg"),size=(930,478))
imageLabel = CTkLabel(root,image=image,text="")
imageLabel.place(x=0,y=0)
headingLabel=CTkLabel(root,text='Employee Management System',bg_color="#FAFAFA",font=('Goody Old Style',20,'bold'),text_color='darkblue')
headingLabel.place(x=0,y=0)
usernameEntry = CTkEntry(root,placeholder_text="Enter Your Username",width=180)
usernameEntry.place(x=30,y=60)
passwordEntry=CTkEntry(root, placeholder_text="Enter Your Password",width=180,show='*')
passwordEntry.place(x=30,y=100)
loginButton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=45,y=150)
root.mainloop()