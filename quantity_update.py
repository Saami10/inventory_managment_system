from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "mypass123"
mydatabase="db"

con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books" #Book Table

def updation():
    value=bookInfo1.get()
    bid=bookInfo2.get()
    update=" update " + bookTable + " set quantity="+ value +" where bid="+ bid
    print(update)
    try:
        cur.execute(update)
        con.commit()
        messagebox.showinfo("Success, Quantity Updated")
    except:
        messagebox.showerror("Failed, Not updated")



def set_update():
    global bookInfo1, Canvas1, con, cur, bookTable, root, bookInfo2

    root = Tk()
    root.title("UPDATE")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="UPDATE QUANTITY", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Set quantity to be updated
    lb2 = Label(labelFrame, text="Set Quantity : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    #Set The book id whose qunatity is to be updated
    lb3 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.6)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.6, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="UPDATE", bg='#d1ccc0', fg='black', command=updation)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()