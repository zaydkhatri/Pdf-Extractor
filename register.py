from tkinter import *
from tkinter import ttk, messagebox #for combo box
from PIL import Image, ImageTk
import pymysql
import re

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1000x667+180+20")
        
        # -- icon -- 
        self.icon = ImageTk.PhotoImage(file="images/icon.png")
        self.root.iconphoto(False,self.icon)

        # -- Bg Image -- 
        self.bg = ImageTk.PhotoImage(file="images/bg.jpg")
        bg = Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1)

        # -- Left Image -- 
        self.left = ImageTk.PhotoImage(file="images/logo.jpg")
        left = Label(self.root, image=self.left).place(x=80,y=100,width=295,height=500)

        # -- Frame for Registration
        frame1 = Frame(self.root,bg="white")
        frame1.place(x=370,y=100,width=550,height=500) 

        # ----------------- Row 0 
        title = Label(frame1,text="Register Here",font=("Times new roman",30,"bold"),bg="white").place(x=160,y=10)

        # ----------------- Row 1
        # -- First Name Entry -- 
        f_name = Label(frame1,text="First Name",font=("Times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=70)
        self.fname_entry = Entry(frame1,font=("Times new roman",15),bg="lightgray")
        self.fname_entry.place(x=50,y=100,width=200)  

        # -- Last name Entry --
        l_name = Label(frame1,text="Last Name",font=("Times new roman",15,"bold"),bg="white",fg="gray").place(x=300,y=70)
        self.lname_entry = Entry(frame1,font=("Times new roman",15),bg="lightgray")
        self.lname_entry.place(x=300,y=100,width=200)

        # ----------------- Row 2
        # -- First Name Entry -- 
        contact_no = Label(frame1,text="Contact No.",font=("Times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=140)
        self.contact_no_entry = Entry(frame1,font=("Times new roman",15),bg="lightgray")
        self.contact_no_entry.place(x=50,y=170,width=200)

        # -- Last name Entry --
        email = Label(frame1,text="Email",font=("Times new roman",15,"bold"),bg="white",fg="gray").place(x=300,y=140)
        self.email_entry = Entry(frame1,font=("Times new roman",15),bg="lightgray")
        self.email_entry.place(x=300,y=170,width=200)

        # ----------------- Row 3
        # -- Question Combo Box -- 
        question = Label(frame1,text="Security Question",font=("Times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=210)
        self.question_cmb = ttk.Combobox(frame1,font=("Times new roman",13),state="readonly",justify="center")
        self.question_cmb['values'] = ('Select','Your Pet Name','Best Colour','Your Best Friend Name',
        'What was the house number and street name you lived in as a child?',
        'What were the last four digits of your childhood telephone number?','What primary school did you attend?',
        'In what town or city was your first full time job?','In what town or city did you meet your spouse or partner?',
        'In what town or city did you meet your spouse or partner?',"What are the last five digits of your driver's license number?",
        'In what town or city did your parents meet?','What time of the day were you born?',
        'What time of the day was your first child born?')
        self.question_cmb.place(x=50,y=240,width=200)
        self.question_cmb.current(0)

        # -- Answer Entry --
        answer = Label(frame1,text="Answer",font=("Times new roman",15,"bold"),bg="white",fg="gray").place(x=300,y=210)
        self.answer_cmb = Entry(frame1,font=("Times new roman",15),bg="lightgray")
        self.answer_cmb.place(x=300,y=240,width=200)

        # ----------------- Row 4
        # -- Password Entry -- 
        password = Label(frame1,text="Password",font=("Times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=280)
        self.password_entry = Entry(frame1,show="*",font=("Times new roman",15),bg="lightgray")
        self.password_entry.place(x=50,y=310,width=200)

        # -- Confirm Password Entry --
        confirm_pass = Label(frame1,text="Confirm Password",font=("Times new roman",15,"bold"),bg="white",fg="gray").place(x=300,y=280)
        self.confirm_pass_entry = Entry(frame1,show="*",font=("Times new roman",15),bg="lightgray")
        self.confirm_pass_entry.place(x=300,y=310,width=200)
       
        # ----------------- Row 5
        self.var_check = IntVar()
        self.check = Checkbutton(frame1,text="Terms and Conditions",variable=self.var_check,onvalue=1,offvalue=0,font=("Times new roman",10),bg="white",fg="black")
        self.check.place(x=50,y=350)

        # ----------------- Row 6
        self.register_btn = ImageTk.PhotoImage(file="images/register.png")
        register_btn = Button(frame1,image=self.register_btn,border=0,command=self.registered_data,cursor="hand2").place(x=180,y=400,width=200,height=70)

        # ----------------- Sign-in
        sign_in = Button(self.root,text="Sign In",command=self.login_win,cursor="hand2",font=("Times new roman",13,"bold"),bd=4).place(x=165,y=520, width=120,height=50)

        self.regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    def check_email(self):
        if re.search(self.regex,self.email_entry.get()):
            return True
        else:
            return False

    def login_win(self):
        self.root.destroy()
        import login

    def default_data(self):
        self.fname_entry.delete(0,END)
        self.lname_entry.delete(0,END)
        self.contact_no_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.question_cmb.current(0)
        self.answer_cmb.delete(0,END)
        self.password_entry.delete(0,END)
        self.confirm_pass_entry.delete(0,END)
        self.var_check.set(0)
    
    def registered_data(self):
        if self.fname_entry.get()=="" or self.email_entry.get()=="" or self.question_cmb.get()=="Select" or self.answer_cmb=="" or self.password_entry=="" or self.confirm_pass_entry=="" or self.contact_no_entry=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.password_entry.get() != self.confirm_pass_entry.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.check_email() == False:
            messagebox.showerror("Error","Invalid Email Address",parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please check Our Terms and Conditions",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="register",port=3306)
                cur = con.cursor()
                cur.execute("select * from clients where Email=%s",self.email_entry.get())
                row = cur.fetchone()
                
                if row != None:
                    messagebox.showerror("Error","Email id Already Been Used Enter Another Email id",parent=self.root)
                else:
                    cur.execute("insert into clients (F_Name,L_Name,Contact,Email,Question,Answer,Password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (
                                    self.fname_entry.get(), 
                                    self.lname_entry.get(),
                                    self.contact_no_entry.get(),
                                    self.email_entry.get(),
                                    self.question_cmb.get(),
                                    self.answer_cmb.get(),
                                    self.password_entry.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registered Successfully",parent=self.root)
                    self.default_data()

            except Exception as e:
                messagebox.showerror("Error",f"Error Occur: {str(e)}",parent=self.root)


                # self.fname_entry.get(),
                # self.lname_entry.get(),
                # self.contact_no_entry,
                # self.email_entry.get(),
                # self.question_cmb.get(),
                # self.answer_cmb.get(),
                # self.password_entry.get(),
                # self.confirm_pass_entry.get())


root = Tk()
obj = Register(root)
root.mainloop()
