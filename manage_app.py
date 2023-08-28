import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="",db="std_details")
if mydb:
    print("connected")
else:
    print("not connected")

mycursor = mydb.cursor()

from tkinter import *

root = Tk()
root.geometry("400x300")
root.title('Student App')

Ttl = Label(root, text="Data Entry", font=("Arial", 18))
Ttl.pack(padx=20,pady=20)

AskLabel = Label(root, text="Add: Adds new detail\nView: Shows details\nSearch: Finds details of specific person\nUpdate: Update a data\nDelete: Delete a data\nExit: Exits",
                 font=("Arial", 13, 'italic'))
AskLabel.pack()

def adding():
    new = Toplevel()
    new.geometry("550x450")
    new.title("Add data")

    def values(event=None):
        det = [name.get().capitalize(), age.get(), address.get(), mark.get(), section.get()]
        mycursor.execute(f"insert into students(name,age,address,mark,section)values('{det[0]}',{det[1]},'{det[2]}',{det[3]},'{det[4]}')")
        mydb.commit()
        new.destroy()


    ttl1 = Label(new, text="Add New Data", font=('Arial', 18))
    ttl1.pack(padx=20, pady=20)

    Label(new, text="Name").pack()
    name = Entry(new)
    name.pack(padx=10, pady=10)

    Label(new, text="Age").pack()
    age = Entry(new)
    age.pack(padx=10, pady=10)

    Label(new, text="Address").pack()
    address = Entry(new)
    address.pack(padx=10, pady=10)

    Label(new, text="Mark").pack()
    mark = Entry(new)
    mark.pack(padx=10, pady=10)

    Label(new, text="Section").pack()
    section = Entry(new)
    section.pack(padx=10, pady=10)

    sub_btn = Button(new, text="Submit", width=10, font=("Arial", 10, 'bold'), command=values)
    sub_btn.pack(pady=2)
    new.bind('<Return>', values)

def viewing():
    new = Toplevel()
    new.geometry("400x300")
    new.title("View data")

    ttl1 = Label(new, text="View Data", font=('Arial', 18))
    ttl1.pack(padx=20, pady=20)

    mycursor.execute("select * from students")
    det = mycursor.fetchall()

    for i in det:
         Label(new, text=f"{i}", font=("Arial", 15)).pack()
def searching():
    new = Toplevel()
    new.geometry("400x300")
    new.title("Search Data")

    ttl1 = Label(new, text="Find Data", font=('Arial', 18))
    ttl1.pack(padx=20, pady=20)

    def getdata(event=None):
        src = to_search.get().capitalize()
        print(src)
        mycursor.execute(f"select * from students where name='{src}'")
        det = mycursor.fetchall()
        for i in det:
                if src in i:
                    dt = Label(new, text=f"{i}", font=("Arial", 15))
                    dt.pack()

    Label(new, text="Search Name", font=('Arial',15,'bold')).pack()
    to_search = Entry(new)
    to_search.pack()

    btn= Button(new, text="Submit", command=getdata)
    btn.pack()
    new.bind('<Return>', getdata)
def delete():
    new = Toplevel()
    new.geometry("400x300")
    new.title("Delete Data")



    ttl1 = Label(new, text="Delete Data", font=('Arial', 18))
    ttl1.pack(padx=20, pady=20)

    def getdat(event=None):
        dell = to_del.get().capitalize()
        if dell == "All":
            mycursor.execute("TRUNCATE TABLE students")
        else:
            mycursor.execute(f"delete from students where name='{dell}'")


    Label(new, text="Delete Name", font=('Arial', 15, 'bold')).pack()
    to_del = Entry(new)
    to_del.pack()

    btn = Button(new, text="Submit", command=getdat)
    btn.pack()
    new.bind('<Return>', getdat)
def update():
    new = Toplevel()
    new.geometry("400x300")
    new.title("Update Data")

    ttl1 = Label(new, text="Update Data", font=('Arial', 18))
    ttl1.pack(padx=20, pady=20)

    def getupdate(event=None):
        up_name = to_up.get().capitalize()
        new_name = cng.get().capitalize()
        mycursor.execute(f"update students set name='{new_name}' where name='{up_name}'")

    Label(new, text="Update Data of user", font=('Arial', 15, 'bold')).pack()
    to_up = Entry(new)
    to_up.pack()

    Label(new, text="New Name of user", font=('Arial', 15, 'bold')).pack()
    cng = Entry(new)
    cng.pack()

    btn = Button(new, text="Submit", command=getupdate)
    btn.pack()
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

ask = Entry(root)
ask.pack(padx=10,pady=10)

askBtn = Button(root, text="Submit",width=10, font=("Arial", 10, 'bold'),command=val)
askBtn.pack(pady=2)

root.bind('<Return>', val)

root.mainloop()