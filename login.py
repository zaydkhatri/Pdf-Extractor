from tkinter import *
from tkinter import ttk, messagebox 
from PIL import Image,ImageTk
import pymysql


class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1000x667+180+20")

        # -- icon -- 
        self.icon = ImageTk.PhotoImage(file="images/icon.png")
        self.root.iconphoto(False,self.icon)
        
        # --Bg Image-- 
        self.bg = ImageTk.PhotoImage(file="images/bg.jpg")
        bg = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1)

        # --logo Image--
        self.logo = ImageTk.PhotoImage(file="images/logo.jpg")
        logo = Label(self.root,image=self.logo).place(x=80,y=100,width=295,height=500)

        # --Frame--
        frame = Frame(self.root,bg="white")
        frame.place(x=370,y=100,width=540,height=500)

        # --Login Title--
        title = Label(frame,text="Login Here",font=("Times new roman",30,"bold"),bg="white",fg="black").place(x=180,y=10)

        # -- User Image --
        self.user_img = ImageTk.PhotoImage(file="images/user.png")
        user = Label(frame,image=self.user_img,bg="white").place(x=245,y=60,width=70,height=70)
        line = Label(frame,bg="gray",fg="gray").place(x=50,y=145,width=450,height=1)

        #---------- row 1
        # -- Emai id --
        email= Label(frame,text="Email Address",font=("Times new roman",20,"bold"),bg="white",fg="gray").place(x=190,y=150)
        self.email_entry = Entry(frame,font=("Times new roman",15),bg="lightgray")
        self.email_entry.place(x=138,y=200,width=280) 
        
        #---------- row 2
        # -- Password --
        password= Label(frame,text="Password",font=("Times new roman",20,"bold"),bg="white",fg="gray").place(x=220,y=240)
        self.password_entry = Entry(frame,show="*",font=("Times new roman",15),bg="lightgray")
        self.password_entry.place(x=138,y=290,width=280) 

        #---------- row 3
        # -- Login Button -- 
        self.login_btn = ImageTk.PhotoImage(file="images/login1.png")
        login_btn = Button(frame,image=self.login_btn,command=self.login,bd=0,bg="white",cursor="hand2").place(x=185,y=315,width=200,height=70)

        #---------- row 4
        # -- line for or --
        line = Label(frame,bg="gray",fg="gray").place(x=50,y=380,width=450,height=1)
        or_txt = Label(frame,text="or",font=("Times new roman",13,"bold"),bg="white",fg="gray").place(x=275,y=368)       

        #---------- row 5
        # -- Forgot password --
        for_pass = Button(frame,text="Forget Password?",command=self.forget_pass_win,cursor="hand2",bd=0,font=("Times new roman",12,"bold"),bg="white",fg="blue").place(x=223,y=390)

        #---------- row 6
        # -- Don't have an account
        acc = Label(frame,text="Do not have an account click on Register",font=("Times new roman",10,"bold"),fg="green").place(x=175,y=420)

        # -- Register Here --
        reg_txt = Button(frame,text="Register Here",command=self.redirect_register,cursor="hand2",bd=4,font=("Times new roman",13,"bold")).place(x=190,y=450,width=200)

        
    # All Functions for Button
    def reset_forget_win(self):
        self.question_cmb.current(0)
        self.answer_entry.delete(0,END)
        self.password_entry.delete(0,END)
        
    def reset_login(self):
        self.email_entry.delete(0,END)
        self.password_entry(0,END)


    def forget_pass(self):
        if self.question_cmb.get() == "Select" or self.new_password_entry.get() == "" or self.answer_entry.get() == "":
            messagebox.showerror("Error","All Feilds are requires",parent=self.root2)
        else:
            try:
                con = pymysql.connect(host="127.0.0.1",user="root",password="root123",database="register",port=3308)
                cur = con.cursor()
                cur.execute("select * from clients where Email=%s and Question=%s and Answer=%s",(self.email_entry.get(),self.question_cmb.get(),self.answer_entry.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Entires",parent=self.root2)
                else:
                    cur.execute("update clients set Password=%s where Email=%s",(self.new_password_entry.get(),self.email_entry.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password been Reset, Please Login",parent=self.root2)
                    self.reset_forget_win()
                    self.root2.destroy()
            
            except Exception as e:
                messagebox.showerror("Error",f"This is the Error {str(e)}",parent=self.root2)

    def forget_pass_win(self):
        if self.email_entry.get() == "":
            messagebox.showerror("Error","Please Enter Valid Email Address to Reset password",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="127.0.0.1",user="root",password="root123",database="register",port=3308)
                cur = con.cursor()
                cur.execute("select * from clients where Email=%s",self.email_entry.get())
                row = cur.fetchone()
                
                if row == None:
                    messagebox.showerror("Error","Invalid Email Id",parent=self.root)
                else:
                    messagebox.showinfo("Sucess","Email id Found",parent=self.root)
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+345+160") 
                    self.root2.focus_force()
                    self.root2.grab_set()
                    
                    # -- Frame --
                    frame = Frame(self.root2,bg="white")
                    frame.place(relwidth=1,relheight=1)
                    # --------- row 1
                    # -- Title --
                    title = Label(frame,text="Forget Password",font=("Times new roman",30,"bold"),bg="white",fg="black").place(relwidth=1)
                    line = Label(frame,bg="gray",fg="gray").place(x=30,y=70,width=300,height=1)

                    # ---------- row 2
                    # -- Question -- 
                    question = Label(frame,text="Select Verification Question",font=("Times new roman",16,"bold"),bg="white",fg="gray").place(x=30,y=80)
                    self.question_cmb = ttk.Combobox(frame,font=("Times new roman",13),state="readonly",justify="center")
                    self.question_cmb['values'] = ('Select','Your Pet Name','Best Colour','Your Best Friend Name','What was the house number and street name you lived in as a child?',
                    'What were the last four digits of your childhood telephone number?','What primary school did you attend?',
                    'In what town or city was your first full time job?','In what town or city did you meet your spouse or partner?',
                    'In what town or city did you meet your spouse or partner?',"What are the last five digits of your driver's license number?",
                    'In what town or city did your parents meet?','What time of the day were you born?',
                    'What time of the day was your first child born?')
                    self.question_cmb.place(x=30,y=120,width=300)
                    self.question_cmb.current(0)

                    # ---------- row 3
                    # -- Answer -- 
                    answer = Label(frame,text="Enter Verification Answer",font=("Times new roman",16,"bold"),bg="white",fg="gray").place(x=30,y=160)
                    self.answer_entry = Entry(frame,font=("Times new roman",15),bg="lightgray")
                    self.answer_entry.place(x=30,y=200,width=300)


                    # --------- row 4
                    # -- New Password -- 
                    password = Label(frame,text="New Password",font=("Times new roman",16,"bold"),bg="white",fg="gray").place(x=30,y=240)
                    self.new_password_entry = Entry(frame,show="*",font=("Times new roman",15),bg="lightgray")
                    self.new_password_entry.place(x=30,y=280,width=300)
                    line = Label(frame,bg="gray",fg="gray").place(x=30,y=330,width=300,height=1)

                    # ---------- row 5
                    # -- reset --
                    reset = Button(frame,text="Reset",cursor="hand2",command=self.forget_pass,bd=4,font=("Times new roman",13,"bold")).place(x=150,y=340)        

            except Exception as e:
                messagebox.showerror("Error",f"This is the error {str(e)}",parent=self.root)  


    def redirect_main(self):
        self.root.destroy()
        import app

    def redirect_register(self):
        self.root.destroy()
        import register

    def login(self):
        if self.email_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="register",port=3308)
                cur = con.cursor()
                cur.execute("select * from clients where Email=%s and Password=%s",(self.email_entry.get(),self.password_entry.get()))
                row = cur.fetchone()
                
                if row == None:
                    messagebox.showerror("Error","Invalid Email Id and Password",parent=self.root)
                else:
                    cur.execute("select F_Name,L_Name from clients where Email=%s and Password=%s",(self.email_entry.get(),self.password_entry.get()))
                    row = cur.fetchone()
                    messagebox.showinfo("Success",f"Welcome {str(row)}",parent=self.root)
                    self.redirect_main()
                con.close()

            except Exception as e:
                messagebox.showerror("Error",f"This is the error {e}",parent=self.root)    

root = Tk()
main = Login(root)
root.mainloop()
