from AddBook import *
from DeleteBook import *
from quantity_update import *
def authentication():
    root = Tk()
    root.title("MANAGER ACCOUNT")
    root.minsize(width=500, height=500)
    root.geometry("700x600")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="brown4")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel = Label(headingFrame1, text="MANAGER ACCOUNT", bg='black', fg='white',
                         font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBook)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete)
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn3= Button(root, text="Update Quantity", bg='black', fg='white', command=set_update)
    btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)



    root.mainloop()

def check_password():
    password="qwerty"
    pas=bookInfo1.get()
    if password==pas:
        root.destroy()
        authentication()
    else:
        messagebox.showinfo("Wrong Password")


def authenticate():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root , bookInfo9

    root = Tk()
    root.title("Password")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Password Require", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Enter Password
    lb2 = Label(labelFrame, text="ENTER PASSWORD : ", bg='black', fg='white')
    lb2.place(relx=0.3, rely=0.4)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=check_password)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()