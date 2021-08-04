from tkinter import *
import pymysql
from tkinter import messagebox
from ViewBook import *
from list_y_author import *
from list_by_category import *
from manager_login import *

mypas="mypass123"
mydatabase="db"
con=pymysql.connect(host='localhost',user='root',password=mypas,database=mydatabase)
cur=con.cursor()
root=Tk()
root.title("Inventory")
root.minsize(width=500,height=500)
root.geometry("700x600")
same = True
n=0.5
backgroundimage=Image.open("3876048.jpg")
[imageSizeWidth, imageSizeHeight]=backgroundimage.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)
backgroundimage = backgroundimage.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img= ImageTk.PhotoImage(backgroundimage)
Canvas1=Canvas(root)
Canvas1.create_image(300,300,image=img)
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="INVENTORY MANAGEMENT \n SYSTEM", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)



btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View)
btn3.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="List By Author", bg='black', fg='white', command=get_author)
btn4.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="List By Category", bg='black', fg='white', command=get_category)
btn5.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn6= Button(root, text="Manager Login", bg='black', fg='white', command=authenticate)
btn6.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)
root.mainloop()

root.mainloop()
