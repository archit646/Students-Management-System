from tkinter import * 
from tkinter import ttk
from datetime import datetime
import tkinter.messagebox as m
import pymysql as sql
from tkcalendar import DateEntry
try:
  con=sql.connect(host='localhost',user='root',password='root',database='project')
  cursor=con.cursor()
except Exception as e:
  m.showerror("Database Error",f"{e}")

def Add(event):
  try:
    roll=e_roll.get()
    name=e_name.get()
    email=e_email.get()
    gender=e_gender.get()
    contact=e_contact.get()
    dob=e_dob.get().strip()
    address=e_address.get("1.0", END).strip()
    if(roll=="" or name=="" or email=="" or gender=="" or contact=="" or dob=="" or address==""):
      m.showerror("Error","Fill All Details")
  
    else:
     cursor.execute("insert into students(Roll_no,Name,Email,Gender,Contact,Dob,Address) values (%s,%s,%s,%s,%s,%s,%s)",(roll,name,email,gender,contact,dob,address))
     con.commit()
     m.showinfo("Done","Student Added Successfully")
  except:
    m.showerror("Error","Roll No. Or Email is Duplicate")
def Update(event):
  try:
    roll=e_roll.get()
    name=e_name.get()
    email=e_email.get()
    gender=e_gender.get()
    contact=e_contact.get()
    dob=e_dob.get().strip()
    address=e_address.get("1.0", END).strip()
    selected_row=students_data.focus()
    row_data=students_data.item(selected_row,"values")
    print(row_data)
    if(roll=="" or name=="" or email=="" or gender=="" or contact=="" or dob=="" or address==""):
      m.showerror("Error","Fill All Details")
    else:
      cursor.execute("update students set Roll_no=%s,Name=%s,Email=%s,Gender=%s,Contact=%s,Dob=%s,Address=%s where Roll_no=%s",(roll,name,email,gender,contact,dob,address,row_data[0]))
      con.commit()
      m.showinfo("Done","Update Successfully")
  except Exception as e:
    print(e)
    # m.showerror("Error","Roll No. Or Email is Duplicate")

def Clear(event):
    e_roll.delete(0,"end")
    e_roll.insert(0,"")
    e_name.delete(0,"end")
    e_name.insert(0,"")
    e_email.delete(0,"end")
    e_email.insert(0,"")
    e_gender.delete(0,"end")
    e_gender.insert(0,"")
    e_contact.delete(0,"end")
    e_contact.insert(0,"")
    e_dob.delete(0,"end")
    e_dob.insert(0,"")
    e_address.delete("1.0","end")
    e_address.insert("1.0","")



def show(event):
  rows=cursor.execute("select * from students")
  data=cursor.fetchall()
  if data:
     for item in students_data.get_children():
        students_data.delete(item)
     for i,row in enumerate(data):
        students_data.insert('','end',values=row)
  else:
    m.showwarning("Warning","No Record Found")

def selected_row(event):
  selected_row=students_data.focus()
  if selected_row: 
    row_data=students_data.item(selected_row,"values")
    e_roll.delete(0,"end")
    e_roll.insert(0,row_data[0])
    e_name.delete(0,"end")
    e_name.insert(0,row_data[1])
    e_email.delete(0,"end")
    e_email.insert(0,row_data[2])
    e_gender.delete(0,"end")
    e_gender.insert(0,row_data[3])
    e_contact.delete(0,"end")
    e_contact.insert(0,row_data[4])
    e_dob.delete(0,"end")
    e_dob.insert(0,row_data[5])
    e_address.delete("1.0","end")
    e_address.insert("1.0",row_data[6])

def del_row(event):
  selected_row=students_data.focus()
  if selected_row: 
    row_data=students_data.item(selected_row,"values")
    students_data.delete(selected_row)
    cursor.execute("delete from students where Roll_no=%s",(row_data[0],))
    con.commit()
  else:
    m.showerror("Error","Please Select Row")
def Search(event):
  search=e_search.get()
  search1=e_search1.get()
  if search=="Roll No.":
    cursor.execute(f"select * from students where Roll_no={search1}")
    data=cursor.fetchall()
    if data:
      for item in students_data.get_children():
        students_data.delete(item)
      for i,row in enumerate(data):
        students_data.insert('','end',values=row)
    else:
      m.showerror("Error","No Record Found")

  elif search=="Name":
    cursor.execute(f"select * from students where Name like '{search1}%'")
    data=cursor.fetchall()
    if data:
      for item in students_data.get_children():
        students_data.delete(item)
      for i,row in enumerate(data):
        students_data.insert('','end',values=row)
    else:
        m.showerror("Error","No Record Found")
  else:
    cursor.execute(f"select * from students where Contact like '{search1}%'")
    data=cursor.fetchall()
    if data:
      for item in students_data.get_children():
        students_data.delete(item)
      for i,row in enumerate(data):
        students_data.insert('','end',values=row)
    else:
        m.showerror("Error","No Record Found")


mainWindow=Tk()
mainWindow.state("zoomed")
mainWindow.title("Students Management System")
mainWindow.configure(bg="white")
mainWindow.minsize(500,500)
head=Label(mainWindow,text="Students Management System",bg="blue",fg="yellow",font="Vardana 25 bold",bd=5,relief="groove")
head.place(relx=0,rely=0,relwidth=1,relheight=0.08)
left_frame=Frame(mainWindow,bg="red")
left_frame.place(relx=0.004,rely=0.09,relwidth=0.3,relheight=0.90,)
right_frame=Frame(mainWindow,bg="green")
right_frame.place(relx=0.31,rely=0.09,relwidth=0.687,relheight=0.90)
left_label=Label(left_frame,text="Manage Students",font="Vardana 23 bold",fg="white",bg="red")
left_label.place(relx=0.225,rely=0.03)

roll_no=Label(left_frame,text="Roll No.",bg="red",font="Vardana 15 bold",fg="white")
roll_no.place(relx=0.1,rely=0.13)

name=Label(left_frame,text="Name",bg="red",font="Vardana 15 bold",fg="white")
name.place(relx=0.1,rely=0.23)

email=Label(left_frame,text="Email",bg="red",font="Vardana 15 bold",fg="white")
email.place(relx=0.1,rely=0.33)

gender=Label(left_frame,text="Gender",bg="red",font="Vardana 15 bold",fg="white")
gender.place(relx=0.1,rely=0.43)

contact=Label(left_frame,text="Contact",bg="red",font="Vardana 15 bold",fg="white")
contact.place(relx=0.1,rely=0.53)

dob=Label(left_frame,text="D.o.b",bg="red",font="Vardana 15 bold",fg="white")
dob.place(relx=0.1,rely=0.63)

address=Label(left_frame,text="Address",bg="red",font="Vardana 15 bold",fg="white")
address.place(relx=0.1,rely=0.73)

e_roll=Entry(left_frame)
e_roll.place(relx=0.4,rely=0.13,relwidth=0.48,relheight=0.04)

e_name=Entry(left_frame)
e_name.place(relx=0.4,rely=0.23,relwidth=0.48,relheight=0.04)

e_email=Entry(left_frame)
e_email.place(relx=0.4,rely=0.33,relwidth=0.48,relheight=0.04)

e_gender=ttk.Combobox(left_frame,values=["Male","Female","Other"])
e_gender.set("Select")
e_gender.place(relx=0.4,rely=0.43,relwidth=0.48,relheight=0.04)

e_contact=Entry(left_frame)
e_contact.place(relx=0.4,rely=0.53,relwidth=0.48,relheight=0.04)

# e_dob=Entry(left_frame)
e_dob=DateEntry(left_frame,date_pattern='yyyy/mm/dd')
e_dob.place(relx=0.4,rely=0.63,relwidth=0.48,relheight=0.04)

e_address=Text(left_frame)
e_address.place(relx=0.4,rely=0.7,relwidth=0.48,relheight=0.09)

btn_frame=Frame(left_frame,bd=3,bg="green")
btn_frame.place(relx=0.02,rely=0.83,relheight=0.1,relwidth=0.96)

add_btn=Button(btn_frame,text="Add",font="Vardana 10 bold")
add_btn.place(relx=0.05,rely=0.28,relwidth=0.15)
add_btn.bind("<Button-1>",Add)

update_btn=Button(btn_frame,text="Update",font="Vardana 10 bold")
update_btn.place(relx=0.3,rely=0.28,relwidth=0.15)
update_btn.bind("<Button-1>",Update)

delete_btn=Button(btn_frame,text="Delete",font="Vardana 10 bold")
delete_btn.place(relx=0.55,rely=0.28,relwidth=0.15)
delete_btn.bind("<Button-1>",del_row)

clear_btn=Button(btn_frame,text="Clear",font="Vardana 10 bold")
clear_btn.place(relx=0.8,rely=0.28,relwidth=0.15)
clear_btn.bind("<Button-1>",Clear)

search=Label(right_frame,text="Search By:",font="Vardana 17 bold",bg="green",fg="white")
search.place(relx=0.02,rely=0.04)

e_search=ttk.Combobox(right_frame,values=["Roll No.","Name","Contact"])
e_search.set("Select")
e_search.place(relx=0.18,rely=0.046,relwidth=0.15,relheight=0.04)

e_search1=Entry(right_frame)
e_search1.place(relx=0.38,rely=0.046,relwidth=0.15,relheight=0.04)

search_btn=Button(right_frame,text="Search",font="Vardana 10 bold")
search_btn.place(relx=0.58,rely=0.047,relwidth=0.1)
search_btn.bind("<Button-1>",Search)

show_btn=Button(right_frame,text="Show All",font="Vardana 10 bold",bg="black",fg="white",bd=2)
show_btn.place(relx=0.78,rely=0.047,relwidth=0.15)
show_btn.bind("<Button-1>",show)

data_frame=Frame(right_frame)
data_frame.place(relx=0.01,rely=0.13,relwidth=0.98,relheight=0.852)

students_data=ttk.Treeview(data_frame,columns=("Roll No.","Name","Email","Gender","Contact","Date-of-Birth","Address"),show="headings")
students_data.column("Roll No.",width=40,anchor="center")
students_data.column("Name",width=120,anchor="center")
students_data.column("Email",width=120,anchor="center")
students_data.column("Gender",width=80,anchor="center")
students_data.column("Contact",width=120,anchor="center")
students_data.column("Date-of-Birth",width=90,anchor="center")
students_data.column("Address",width=170,anchor="center")
students_data.heading("Roll No.",text="Roll No.")
students_data.heading("Name",text="Name")
students_data.heading("Email",text="Email")
students_data.heading("Gender",text="Gender")
students_data.heading("Contact",text="Contact")
students_data.heading("Date-of-Birth",text="Date-of-Birth")
students_data.heading("Address",text="Address")
students_data.place(relx=0.01,rely=0.015,relheight=0.97,relwidth=0.98)
style=ttk.Style()
style.configure("Treeview",font=("Vardana",10,"bold"),rowheight=40)
style.configure("Treeview.Heading",font=("Vardana",12,"bold"),background="red")

scroll_y = ttk.Scrollbar(data_frame, orient="vertical", command=students_data.yview)
students_data.configure(yscrollcommand=scroll_y.set)
scroll_y.pack(side="right", fill="y")  


students_data.bind("<<TreeviewSelect>>",selected_row)
mainWindow.mainloop()