from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database
from customtkinter import CTkImage, CTkFrame, CTkLabel, CTkEntry, CTkComboBox

###function

def delete_all():
   result=messagebox.askyesno('Confirm','Do You really want to delete all the records?')
   if result:
       database.deleteall_records()
   else:
       pass

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')

def search_empolyee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Enter value to search')
    elif searchBox.get()=='Search By':
        messagebox.showerror('Error','Please Select an Option')
    else:
        searched_data=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for empolyee in searched_data:
            tree.insert('', END, values=empolyee)



def delete_empolyee():
    selection_item=tree.selection()
    if not selection_item:
        messagebox.showerror("Error", "selected data to delete")
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror("Error", "Data is deleted")

def update_empolyee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","selected data to update")
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Data is Updated")

def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])


def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    roleBox.set('Web Developer')
    genderBox.set('Male')
    salaryEntry.delete(0,END)




def treeview_data():
    empolyees=database.fetch_empolyees()
    tree.delete(*tree.get_children())
    for empolyee in empolyees:
        tree.insert('',END,values=empolyee)


def add_employee():
    
    if idEntry.get()=='' or phoneEntry.get()==''or nameEntry.get()=='' or salaryEntry.get()=='':
      messagebox.showerror('Error','All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id already exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror("Error", "Invalid ID Format,Use 'EMP' followed by a number(e.g., 'EMP1').")
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is added')

#GUI Port

window=CTk()
window.geometry("1139x720")
window.resizable(False,False)
window.title("Employee Management System")



window.configure(fg_color="#161C30")
window.iconbitmap(r'emp.ico')

photo = CTkImage(Image.open("cas.jpeg"), size=(1139, 200))
photoLabel=CTkLabel(window,image=photo,text="")
photoLabel.pack()




leftFrame=CTkFrame(window,fg_color="#161C30")
leftFrame.place(x=7,y=240)
idLabel=CTkLabel(leftFrame,text="Id",font=("arial",18,"bold"),text_color="white")
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky=W)
idEntry=CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
idEntry.grid(row=0,column=1)
nameLabel=CTkLabel(leftFrame,text="Name",font=("arial",18,"bold"),text_color="white")
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky=W)
nameEntry=CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
nameEntry.grid(row=1,column=1)
phoneLabel=CTkLabel(leftFrame,text="Phone",font=("arial",15,"bold"),text_color="white")
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky=W)
phoneEntry=CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
phoneEntry.grid(row=2,column=1)
roleLabel=CTkLabel(leftFrame,text="Role",font=("arial",15,"bold"),text_color="white")
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky=W)
role_options=['Web Developer','Cloud Architect','Technical Writer','Network Engineer','Devops Engineer','Data Scientist','Business Analyst','IT Consultant','UX/UI Designer']
roleBox=CTkComboBox(leftFrame,values=role_options,width=180,font=("arial",18,"bold"),state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])
genderLabel=CTkLabel(leftFrame,text="Gender",font=("arial",15,"bold"),text_color="white")
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky=W)
gender_options=['Male','Female','Others']
genderBox=CTkComboBox(leftFrame,values=gender_options,width=180,font=("arial",15,"bold"),state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set('Male')
salaryLabel=CTkLabel(leftFrame,text="Salary",font=("arial",15,"bold"),text_color="white")
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky=W)
salaryEntry=CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
salaryEntry.grid(row=5,column=1)

rightFrame=CTkFrame(window)
rightFrame.place(x=320,y=205)
search_options=['Id','Name','Phone','Role','Gender','Salary']
searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')
searchEntry=CTkEntry(rightFrame,width=180)
searchEntry.grid(row=0,column=1)
searchButton=CTkButton(rightFrame,text='search',width=150,command=search_empolyee)
searchButton.grid(row=0,column=2)
show_allButton=CTkButton(rightFrame, text='show all', width=150,command=show_all)
show_allButton.grid(row=0, column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)
tree['column']=('Id','Name','Phone','Role','Gender','Salary')
tree.pack(side=RIGHT)
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')

tree.column('Id',width=100)
tree.column('Name',width=130)
tree.column('Phone',width=150)
tree.column('Role',width=200)
tree.column('Gender',width=100)
tree.column('Salary',width=110)

style = ttk.Style()

style.configure('Treeview.Heading',font=("arial",18,"bold"))
style.configure('Treeview',font=("arial",15,"bold"),rowheight=30,background='#161C30',foreground='white')
ver=ttk.Scrollbar(rightFrame,orient=VERTICAL,command='tree.yview')
tree.config(yscrollcommand=ver.set)
ver.grid()


buttonFrame=CTkButton(window,fg_color="#161C30",text="")
buttonFrame.place(x=170,y=670)
newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda:clear(True))
newButton.grid(row=0,column=0,pady=5)
addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)
updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_empolyee)
updateButton.grid(row=0,column=2,pady=5,padx=5)
deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_empolyee)
deleteButton.grid(row=0,column=3,pady=5,padx=5)
delete_allButton=CTkButton(buttonFrame,text='Delete All',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
delete_allButton.grid(row=0,column=4,pady=5,padx=5)

treeview_data()

window.bind('<ButtonRelease>',selection)

window.mainloop()
