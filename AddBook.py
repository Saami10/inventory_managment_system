from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegister():
    bid=bookInfo1.get()
    category=bookInfo2.get()
    author=bookInfo3.get()
    name=bookInfo4.get()
    description=bookInfo5.get()
    price=bookInfo6.get()
    quantity=bookInfo7.get()

    insertBooks = "insert into " + bookTable + " values "\
                "('" + bid + "','" + category + "','" + author + "','" + name +"','" + description + "','"+price+"','"+ quantity +"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(bid)
    print(name)
    print(author)
    print(description)
    root.destroy()


def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, bookInfo5, bookInfo6, bookInfo7, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=700, height=700)
    root.geometry("600x500")

    mypass = "mypass123"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books"  # Book Table

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.04, rely=0.05, relheight=0.05)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.2, rely=0.05, relwidth=0.52, relheight=0.05)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.04, rely=0.15, relheight=0.05)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.2, rely=0.15, relwidth=0.52, relheight=0.05)

    # Book Author
    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.04, rely=0.25, relheight=0.05)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.2, rely=0.25, relwidth=0.52, relheight=0.05)

    # Book Status
    lb4 = Label(labelFrame, text="Description : ", bg='black', fg='white')
    lb4.place(relx=0.04, rely=0.35, relheight=0.05)

    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.2, rely=0.35, relwidth=0.52, relheight=0.05)

    # Book Category

    lb5= Label(labelFrame, text='Category : ', bg='black', fg='white')
    lb5.place(relx=0.04, rely=0.45, relheight=0.05)

    bookInfo2= Entry(labelFrame)
    bookInfo2.place(relx=0.2, rely=0.45, relwidth=0.52, relheight=0.05)

    #Book Price
    lb6=Label(labelFrame, text='Price : ', bg='black', fg='white')
    lb6.place(relx=0.04, rely=0.55, relheight=0.05)

    bookInfo6= Entry(labelFrame)
    bookInfo6.place(relx=0.2, rely=0.55, relwidth=0.52, relheight=0.05)

    #Book Quantity
    lb7=Label(labelFrame, text='Quantity : ', bg='black', fg='white')
    lb7.place(relx=0.04, rely=0.65, relheight=0.05)

    bookInfo7=Entry(labelFrame)
    bookInfo7.place(relx=0.2, rely=0.65, relwidth=0.52, relheight =0.05)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.08, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.08, relheight=0.08)

    root.mainloop()