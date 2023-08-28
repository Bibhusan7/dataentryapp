import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="",db="std_details")
if mydb:
    print("connected")
else:
    print("not connected")

mycursor = mydb.cursor()
from customtkinter import *
set_appearance_mode('light')
set_default_color_theme('green')

root = CTk()
root.geometry("500x300")
root.title('Student App')

Ttl = CTkLabel(root, text="Data Entry", font=("Lucida Console", 20))
Ttl.pack(padx=20,pady=10)

AskLabel = CTkLabel(root, text="Add: Adds new detail\nView: Shows details\nSearch: Finds details of specific person\nUpdate: Update a data\nDelete: Delete a data\nExit: Exits",
                 font=("Lucida Console", 15))
AskLabel.pack(padx=10, pady=7)

def adding():
    new = CTkToplevel()
    new.geometry("600x500")
    new.title("Add data")
    new.attributes('-topmost', True)
    def values(event=None):
        det = [name.get().capitalize(), age.get(), address.get(), mark.get(), section.get()]
        mycursor.execute(f"insert into students(name,age,address,mark,section)values('{det[0]}',{det[1]},'{det[2]}',{det[3]},'{det[4]}')")
        mydb.commit()
        new.destroy()


    ttl1 = CTkLabel(new, text="Add New Data", font=('Lucida Console', 18))
    ttl1.pack(padx=20, pady=20)

    CTkLabel(new, text="Name", font=('Lucida Console', 15)).pack()
    name = CTkEntry(new, placeholder_text='eg: Ram', placeholder_text_color='gray')
    name.pack(padx=10, pady=10)

    CTkLabel(new, text="Age", font=('Lucida Console', 15)).pack()
    age = CTkEntry(new, placeholder_text='eg: 17', placeholder_text_color='gray')
    age.pack(padx=10, pady=10)

    CTkLabel(new, text="Address", font=('Lucida Console', 15)).pack()
    address = CTkEntry(new, placeholder_text='eg: Kathmandu', placeholder_text_color='gray')
    address.pack(padx=10, pady=10)

    CTkLabel(new, text="Mark", font=('Lucida Console', 15)).pack()
    mark = CTkEntry(new,placeholder_text='eg: 57', placeholder_text_color='gray')
    mark.pack(padx=10, pady=10)

    CTkLabel(new, text="Section", font=('Lucida Console', 15)).pack()
    section = CTkEntry(new,placeholder_text='eg: a', placeholder_text_color='gray')
    section.pack(padx=10, pady=10)

    sub_btn = CTkButton(new, text="Submit",width=140, font=("Lucida Console", 15), command=values)
    sub_btn.pack()
    new.bind('<Return>', values)
def viewing():
    new = CTkToplevel()
    new.geometry("400x300")
    new.title("View data")
    new.attributes('-topmost', True)

    ttl1 = CTkLabel(new, text="View Data", font=('Lucida Console', 18))
    ttl1.pack(padx=10, pady=20)

    mycursor.execute("select * from students")
    det = mycursor.fetchall()

    for i in det:
         CTkLabel(new, text=f"{i}", font=("Lucida Console", 15)).pack()
def searching():
    new = CTkToplevel()
    new.geometry("400x300")
    new.title("Search Data")
    new.attributes('-topmost', True)

    ttl1 = CTkLabel(new, text="Find Data", font=('Lucida Console', 18))
    ttl1.pack(padx=20, pady=20)

    def getdata(event=None):
        src = to_search.get().capitalize()
        print(src)
        mycursor.execute(f"select * from students where name='{src}'")
        det = mycursor.fetchall()
        for i in det:
                if src in i:
                    dt = CTkLabel(new, text=f"{i}", font=("Lucida Console", 15))
                    dt.pack()

    CTkLabel(new, text="Search Name", font=('Lucida Console',15,'bold')).pack()
    to_search = CTkEntry(new)
    to_search.pack()

    btn= CTkButton(new, text="Submit",width=140, font=("Lucida Console", 15), command=getdata)
    btn.pack(pady=5)
    new.bind('<Return>', getdata)
def delete():
    new = CTkToplevel()
    new.geometry("400x300")
    new.title("Delete Data")
    new.attributes('-topmost', True)



    ttl1 = CTkLabel(new, text="Delete Data", font=('Lucida Console', 18))
    ttl1.pack(padx=20, pady=20)

    def getdat(event=None):
        dell = to_del.get().capitalize()
        if dell == "All":
            mycursor.execute("TRUNCATE TABLE students")
        else:
            mycursor.execute(f"delete from students where name='{dell}'")


    CTkLabel(new, text="Delete Name", font=('Lucida Console', 15, 'bold')).pack()
    to_del = CTkEntry(new)
    to_del.pack()

    btn = CTkButton(new, text="Submit",width=140, font=("Lucida Console", 15), command=getdat)
    btn.pack(pady=5)
    new.bind('<Return>', getdat)
def update():
    new = CTkToplevel()
    new.geometry("400x300")
    new.title("Update Data")
    new.attributes('-topmost', True)

    ttl1 = CTkLabel(new, text="Update Data", font=('Lucida Console', 18))
    ttl1.pack(padx=20, pady=20)

    def getupdate(event=None):
        up_name = to_up.get().capitalize()
        new_name = cng.get().capitalize()
        mycursor.execute(f"update students set name='{new_name}' where name='{up_name}'")

    CTkLabel(new, text="Update Data of user", font=('Lucida Console', 15, 'bold')).pack()
    to_up = CTkEntry(new)
    to_up.pack()

    CTkLabel(new, text="New Name of user", font=('Lucida Console', 15, 'bold')).pack()
    cng = CTkEntry(new)
    cng.pack()

    btn = CTkButton(new, text="Submit",width=140, font=("Lucida Console", 15), command=getupdate)
    btn.pack(pady=5)
    new.bind('<Return>', getupdate)
def val(event=None):
    user = ask.get()
    user = user.lower()
    if user== 'add':
        adding()
    elif user == 'view':
        viewing()

    elif user == 'search':
        searching()
    elif user == 'delete':
        delete()
    elif user == 'update':
        update()
    elif user == 'exit':
        exit()
    else:
        pass

ask = CTkEntry(root)
ask.pack(padx=10,pady=12)

askBtn = CTkButton(root, text="Submit",width=140, font=("Lucida Console", 15),command=val)
askBtn.pack()

root.bind('<Return>', val)
print(get_appearance_mode())

root.mainloop()
