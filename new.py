import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
import tkinter.messagebox as tkMessageBox
from PIL import Image, ImageTk
# from student import Student
# from train import Train
import os
from datetime import *
from datetime import datetime
import time
import numpy as np
import random
import cv2
import mysql.connector
from tkinter import messagebox
from time import strftime
from tkinter import ttk
from fpdf import FPDF
import xlsxwriter
import re
import smtplib
import random


class Face_Recognition_System:
    def __init__(self, root):

        # ======================================Main(root)====================================
        self.select = 0
        self.select2 = 0
        self.recognised_student_dep = str
        self.recognised_student_name = str
        recognised_student_roll = str
        self.var_department = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_student_id = StringVar()
        self.var_student_name = StringVar()
        self.var_div = StringVar()
        self.var_roll_no = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_book_name = StringVar()
        self.var_book_author = StringVar()
        self.var_semester_library = StringVar()
        self.var_department_library = StringVar()
        self.var_Bookid = StringVar()
        self.var_author = StringVar()
        self.search = StringVar()
        self.text_search = StringVar()
        self.email = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.regex = "^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        self.email = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.send_email = StringVar()
        self.student_textsearch=StringVar()
        self.student_search=StringVar()
        self.library_textsearch = StringVar()
        self.library_search = StringVar()

        self.root = root
        self.root.maxsize(1300, 750)
        self.root.minsize(1300, 750)
        self.root.title("Face Recognition System")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # =======================================variables====================================
        global select
        select = self.select
        global select2
        select = self.select2

    # ============================================== Main screens (Layouts)==================================================

    # def first_screen(self):
    #     self.screen1 = Frame(self.root, bg='white')
    #     self.screen1.pack()
    #     self.select = 1
    #     global select
    #     select = self.select
    #     label = Label(self.screen1, text='FACE RECOGINITION ATTENDENCE SYSTEM', bg="crimson", width='300', height=3,
    #                   font=('Copperplate Gothic Bold', 25, 'bold'))
    #     label.pack()
    #     space_label = Label(self.screen1, text="", bg='white')
    #     button = Button(self.screen1, text='LOGIN', activeforeground='white', bd=3, activebackground='black',
    #                     bg='crimson', command=self.register,
    #                     height='1', width='12', font=("Copperplate Gothic bold", 16, "bold"),
    #                     relief=SOLID)
    #     button.pack(pady=15)
    #     space_label = Label(self.screen1, text="", bg='white')
    #     space_label.pack(pady=800)

    # =================== REGISTER FRAME =========================================================
    def register(self):
        if self.select==6:
            self.image_panel1.destroy
        # self.image_panel1.destroy()
        self.select = 1
        global select
        select = self.select
        self.login_frame = ImageTk.PhotoImage \
            (file='images\\admin_setup_frame.png')
        self.image_panel = Label(self.root, image=self.login_frame)
        self.image_panel.pack(fill='both', expand='yes')

        self.txt = "Registeration System"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.image_panel, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=460, y=70, width=450)
        self.slider()
        self.heading_color()

        # ============================Email====================================
        self.email_label = Label(self.image_panel, text="Email ", bg="white", fg="#4f4e4d",
                                 font=("yu gothic ui", 13, "bold"))
        self.email_label.place(x=495, y=160)

        self.email_entry = Entry(self.image_panel, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                 textvariable=self.email, font=("yu gothic ui semibold", 12))
        self.email_entry.place(x=480, y=183, width=420, height=34)

        # ============================Username====================================
        self.username_label = Label(self.image_panel, text="Username ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=495, y=272)

        self.username_entry = Entry(self.image_panel, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    textvariable=self.username, font=("yu gothic ui semibold", 12))
        self.username_entry.place(x=480, y=297, width=420, height=41)

        # ============================Password====================================
        self.password_label = Label(self.image_panel, text="Password ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=495, y=400)

        self.password_entry = Entry(self.image_panel, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    show="*",
                                    textvariable=self.password, font=("yu gothic ui semibold", 12))
        self.password_entry.place(x=480, y=424, width=420, height=34)

        # ============================Submit button================================
        self.submit = ImageTk.PhotoImage \
            (file='images/submit.png')

        self.submit_button = Button(self.image_panel, image=self.submit,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.get_data_register)
        self.submit_button.place(x=515, y=530)

        # ============================Exit button================================
        self.exit_img = ImageTk.PhotoImage \
            (file='images\\exit1.png')
        self.exit_button = Button(self.image_panel, image=self.exit_img,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , command=self.Exit, borderwidth=0, background="white", cursor="hand2")
        self.exit_button.place(x=705, y=530)

        # ======================== Account Label =====================================
        self.account_label = Label(self.image_panel, text="Already have an account?", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.account_label.place(x=515, y=630)

        # =========================== Register Button ===============================================
        self.sign_up_button = Button(self.image_panel, text="Login Now", command=self.login, bg="white", fg="#DC143C",
                                     relief=FLAT,
                                     activebackground="white", borderwidth=0,
                                     font=("yu gothic ui", 13, "bold"), cursor="hand2")
        self.sign_up_button.place(x=723, y=628)

    # =================== LOGIN FRAME =========================================================
    def login(self):
        if self.select==1:
            self.image_panel.destroy()
        if self.select==7:
            self.otp_frame1.destroy()
        # if self.select==8:
        #     self.otp_password_frame1.destroy()
        if self.select ==9:
            self.password_frame1.destroy()
        if self.select == 11:
            self.bg_img.destroy()
            self.main_frame.destroy()
        self.select = 6
        global select
        select = self.select
        self.login_frame1 = ImageTk.PhotoImage \
            (file='images\\admin_setup_frame_login.png')
        self.image_panel1 = Label(self.root, image=self.login_frame1)
        self.image_panel1.place(x=-2, y=-2)


        self.txt = "Login System"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.image_panel1, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=500, y=90, width=450)
        self.slider()
        self.heading_color()

        # ============================Username====================================
        self.username_label = Label(self.image_panel1, text="Username or Email Address", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=538, y=215)

        self.username_entry = Entry(self.image_panel1, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    textvariable=self.username, font=("yu gothic ui semibold", 12))
        self.username_entry.place(x=536, y=250, width=405, height=38)

        # ============================Password====================================
        self.password_label = Label(self.image_panel1, text="Password", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=538, y=383)

        self.password_entry = Entry(self.image_panel1, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    textvariable=self.password, show='*', font=("yu gothic ui semibold", 12))
        self.password_entry.place(x=536, y=417, width=405, height=35)

        # ============================Submit button================================
        self.submit = ImageTk.PhotoImage \
            (file='images/submit.png')

        self.submit_button = Button(self.image_panel1, image=self.submit,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.get_data)
        self.submit_button.place(x=550, y=530)

        # ============================Exit button================================
        self.exit_img = ImageTk.PhotoImage \
            (file='images\\exit1.png')
        self.exit_button = Button(self.image_panel1, image=self.exit_img,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white",
                                  command=self.Exit
                                  , borderwidth=0, background="white", cursor="hand2")
        self.exit_button.place(x=750, y=530)

        # ======================== Forget Password ===========================================
        self.forget_password = Button(self.image_panel1, text="Forget Password?", bg="white", fg="#DC143C", relief=FLAT,
                                      activebackground="white", borderwidth=0, command=self.email_fpass,
                                      font=("yu gothic ui", 11, "bold"), cursor="hand2")
        self.forget_password.place(x=830, y=470)

        # ======================== Account Label =======================
        self.account_label = Label(self.image_panel1, text="Don't have an account?", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.account_label.place(x=565, y=630)

        # =========================== Register Button ===============================================
        self.sign_up_button = Button(self.image_panel1, text="Register Now", bg="white", fg="#DC143C", relief=FLAT,
                                     command=self.register, activebackground="white", borderwidth=0,
                                     font=("yu gothic ui", 13, "bold"), cursor="hand2")
        self.sign_up_button.place(x=755, y=628)

    def get_data(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All Fields Are Required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select email,password from register")
                data = my_cursor.fetchall()
                if (data != []):
                    name_list = [r for r in data]
                else:
                    name_list = []

                my_cursor.execute("select username,password from register")
                data = my_cursor.fetchall()
                if (data != []):
                    name_list1 = [r for r in data]
                else:
                    name_list1 = []

                if '@' in self.username.get():
                    if any((self.username.get() in i for i in name_list)):
                        if any((self.password.get() in i for i in name_list)):
                            my_cursor.execute("INSERT INTO login (id, email, username, password) VALUES (%s, %s, %s, %s) ",
                                              ("", self.username.get(), "NULL", self.password.get()))
                            messagebox.showinfo("Success", f"{self.username.get().upper()} Has Been Logined Successfully!",
                                                parent=self.root)
                            self.mainPage()
                        else:
                            messagebox.showerror("Error", "Unknown Password! Check Again.", parent=self.root)
                    else:
                        messagebox.showerror("Error", "Unknown Email! Check Again.", parent=self.root)
                elif name_list == []:
                    my_cursor.execute("INSERT INTO login (id, email, username, password) VALUES (%s, %s, %s, %s) ",
                                      ("", self.username.get(), "NULL", self.password.get()))
                    messagebox.showinfo("Success", f"{self.username.get().upper()} Has Been Logined Successfully!",
                                        parent=self.root)
                    self.mainPage()
                elif name_list1 == []:
                    my_cursor.execute("INSERT INTO login (id, username, email, password) VALUES (%s,%s,%s, %s)",
                                      ("", self.username.get(), "NULL", self.password.get()))
                    messagebox.showinfo("Success", f"{self.username.get().upper()} Has Been Logined Successfully!",
                                        parent=self.root)
                    self.mainPage()
                elif any((self.username.get() in i for i in name_list1)):
                    if any((self.password.get() in i for i in name_list1)):
                        my_cursor.execute("INSERT INTO login (id, username, email, password) VALUES (%s,%s,%s, %s)",
                                          ("", self.username.get(), "NULL", self.password.get()))
                        messagebox.showinfo("Success", f"{self.username.get().upper()} Has Been Logined Successfully!",
                                            parent=self.root)
                        self.mainPage()
                    else:
                        messagebox.showerror("Error", "Unknown Password! Check Again.", parent=self.root)
                else:
                    messagebox.showerror("Error", "Unknown Username! Check Again.", parent=self.root)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def get_data_register(self):
        self.regex = "^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.search(self.regex, self.email.get()):
            messagebox.showerror("Error", "Enter valid email!", parent=self.root)
        elif self.email.get() == "" or self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All Fields Are Required!", parent=self.root)
        elif len(self.password.get()) < 8:
            messagebox.showerror("Error", "Password must be 8 character long!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register")
                data = my_cursor.fetchall()
                if (data != []):
                    name_list = [r for r in data]
                else:
                    name_list = []

                if any((self.email.get() in i for i in name_list)):
                    messagebox.showerror("Error", "Email Already Exits! Try With Another Email")
                elif any((self.username.get() in i for i in name_list)):
                    messagebox.showerror("Error", "Username Already Exits! Try With Another Username")
                elif name_list == []:
                    my_cursor.execute("insert into register values (%s,%s,%s,%s)", ("", self.username.get(),
                                                                                    self.email.get(),
                                                                                    self.password.get()
                                                                                    ))
                    messagebox.showinfo("Success", f"{self.username.get()} Has Been Registered Successfully!",
                                        parent=self.root)
                else:
                    my_cursor.execute("insert into register values (%s,%s,%s,%s)", ("", self.username.get(),
                                                                                    self.email.get(),
                                                                                    self.password.get()
                                                                                    ))
                    messagebox.showinfo("Success", f"{self.username.get().upper()} Has Been Registered Successfully!",
                                        parent=self.root)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # ==================== ENTER EMAIL FOR OTP GENERATION =============================
    def email_fpass(self):
        self.image_panel1.destroy()
        self.select == 7
        self.otp_frame = ImageTk.PhotoImage \
            (file='images/otp_frame.png')
        self.otp_frame1 = Label(self.root, image=self.otp_frame)
        self.otp_frame1.place(x=-2, y=-2)

        self.txt = "OTP Generation"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.otp_frame1, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=480, y=90, width=450)
        self.slider()
        self.heading_color()

        # ============================Email====================================
        self.email_new_label = Label(self.otp_frame1, text="Email Address", bg="white", fg="#4f4e4d",
                                     font=("yu gothic ui", 13, "bold"))
        self.email_new_label.place(x=514, y=285)

        self.email_new1_entry = Entry(self.otp_frame1, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69", textvariable=self.send_email,
                                      font=("yu gothic ui semibold", 12))
        self.email_new1_entry.place(x=525, y=323, width=405, height=37)

        # check otp submit
        self.submit1 = ImageTk.PhotoImage \
            (file='images/submit.png')
        self.submit_button1 = Button(self.otp_frame1, image=self.submit1,
                                     font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                     , borderwidth=0, background="white", cursor="hand2", command=self.check_email)
        self.submit_button1.place(x=618, y=440)

        # ======================== Account Label =======================
        self.account_label1 = Label(self.otp_frame1, text="Already have an account?", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.account_label1.place(x=545, y=600)

        # ===========================Login Button ===============================================
        self.sign_up_button1 = Button(self.otp_frame1, text="Login Now", bg="white", fg="#DC143C", relief=FLAT,
                                     command=self.login,
                                     activebackground="white", borderwidth=0,
                                     font=("yu gothic ui", 13, "bold"), cursor="hand2")
        self.sign_up_button1.place(x=750, y=598)

    def send_otp(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # adding TLS security
        server.starttls()

        # login to account
        self.email = 'ashitagupta09@gmail.com'
        self.password = 'rvtoxxwgmnohumqv'
        server.login(self.email, self.password)

        # generate OTP using random.randint() function
        self.otp = ''.join([str(random.randint(0, 9)) for i in range(4)])
        self.msg = 'Hello, Your OTP is ' + str(self.otp)
        self.sender = 'ashitagupta09@gmail.com'  # write email id of sender
        self.receiver = self.send_email.get()  # write email of receiver

        # sending otp
        server.sendmail(self.sender, self.receiver, self.msg)
        server.quit()
        self.otp_fpass()

    def otp_fpass(self):
        self.otp_frame1.destroy()
        self.select==8
        self.otp_password_frame = ImageTk.PhotoImage \
            (file='images/otp_password.png')
        self.otp_password_frame1 = Label(self.root, image=self.otp_password_frame)
        self.otp_password_frame1.place(x=-2, y=-2)

        self.txt = "OTP Generation"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.otp_password_frame1, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=480, y=90, width=450)
        self.slider()
        self.heading_color()

        # ============================enter otp====================================
        self.email_new_label = Label(self.otp_password_frame1, text="Enter OTP", bg="white", fg="#4f4e4d",
                                     font=("yu gothic ui", 13, "bold"))
        self.email_new_label.place(x=510, y=270)

        self.email_new2_entry = Entry(self.otp_password_frame1, highlightthickness=0, relief=FLAT, bg="white",
                                      fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12))
        self.email_new2_entry.place(x=525, y=323, width=405, height=37)

        # send otp submit
        self.submit1 = ImageTk.PhotoImage \
            (file='images/submit.png')
        self.submit_button1 = Button(self.otp_password_frame1, image=self.submit1,
                                     font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                     , borderwidth=0, background="white", cursor="hand2", command=self.check_otp)
        self.submit_button1.place(x=618, y=440)

        # ======================== Account Label =======================
        self.account_label = Label(self.otp_password_frame1, text="Didn't receive the OTP?", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.account_label.place(x=545, y=600)

        # =========================== Resend OTP Button ===============================================
        self.sign_up_button = Button(self.otp_password_frame1, text="Resend OTP", bg="white", fg="#DC143C", relief=FLAT,
                                     command=self.resend_otp,
                                     activebackground="white", borderwidth=0,
                                     font=("yu gothic ui", 13, "bold"), cursor="hand2")
        self.sign_up_button.place(x=735, y=598)

    def resend_otp(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # adding TLS security
        server.starttls()

        # login to account
        self.email = 'ashitagupta09@gmail.com'
        self.password = 'rvtoxxwgmnohumqv'
        server.login(self.email, self.password)

        # generate OTP using random.randint() function
        self.otp = ''.join([str(random.randint(0, 9)) for i in range(4)])
        self.msg = 'Hello, Your OTP is ' + str(self.otp)
        self.sender = 'ashitagupta09@gmail.com'  # write email id of sender
        self.receiver = self.send_email.get()  # write email of receiver

        # sending otp
        server.sendmail(self.sender, self.receiver, self.msg)
        server.quit()
        self.otp_fpass()

    def check_otp(self):
        if self.email_new2_entry.get() == self.otp:
            messagebox.showinfo("Success", "Login Success", parent=self.root)
            self.otp = "done"
            self.newpassword()

        elif self.otp == "done":
            messagebox.showinfo("Success", "Already Login", parent=self.root)
        else:
            messagebox.showerror("Error", "Wrong OTP", parent=self.root)

    def check_email(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="",
                                       database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select email from register")
        data = my_cursor.fetchall()
        if (data != []):
            name_list = [r for r in data]
        else:
            name_list = []

        if any((self.send_email.get() in i for i in name_list)):
            self.send_otp()
            self.otp_fpass()
        else:
            messagebox.showerror("Error", "Enter Email Associated With Account!")

        conn.commit()
        conn.close()

    def newpassword(self):
        self.select = 9
        self.otp_password_frame1.destroy()
        self.password_frame = ImageTk.PhotoImage \
            (file='images/new_frame.png')
        self.password_frame1 = Label(self.root, image=self.password_frame)
        self.password_frame1.place(x=-2, y=-2)

        self.txt = "Set New Password"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.password_frame1, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=480, y=90, width=450)
        self.slider()
        self.heading_color()

        # ============================new password====================================
        self.password_new_label = Label(self.password_frame1, text="New Password", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        self.password_new_label.place(x=510, y=217)

        self.password_new1_entry = Entry(self.password_frame1, highlightthickness=0, relief=FLAT, bg="white",
                                         fg="#6b6a69",
                                         font=("yu gothic ui semibold", 12))
        self.password_new1_entry.place(x=515, y=248, width=405, height=37)

        # ============================confirm password====================================
        self.confirm_password_label = Label(self.password_frame1, text="Confirm Password", bg="white", fg="#4f4e4d",
                                            font=("yu gothic ui", 13, "bold"))
        self.confirm_password_label.place(x=510, y=332)

        self.confirm_password_entry = Entry(self.password_frame1, highlightthickness=0, relief=FLAT, bg="white",
                                            fg="#6b6a69",
                                            font=("yu gothic ui semibold", 12))
        self.confirm_password_entry.place(x=515, y=362, width=405, height=37)

        # New Password Submit
        self.submitotp = ImageTk.PhotoImage \
            (file='images/submit.png')
        self.submitotp_button = Button(self.password_frame1, image=self.submitotp,
                                       font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", command=self.confirmpassword
                                       , borderwidth=0, background="white", cursor="hand2")
        self.submitotp_button.place(x=618, y=460)

        # ======================== Account Label =======================
        self.account_label = Label(self.password_frame1, text="Already have an account?", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.account_label.place(x=545, y=600)

        # =========================== Login Now ===============================================
        self.sign_up_button = Button(self.password_frame1, text="Login Now", bg="white", fg="#DC143C", relief=FLAT, command=self.login,

                                     activebackground="white", borderwidth=0,
                                     font=("yu gothic ui", 13, "bold"), cursor="hand2")
        self.sign_up_button.place(x=752, y=598)

    def confirmpassword(self):
        if self.password_new1_entry.get() == "" or self.confirm_password_entry.get() == "":
            messagebox.showerror("Error", "All Fields Are Required!", parent=self.root)
        elif len(self.password_new1_entry.get()) < 8:
            messagebox.showerror("Error", "Password must be 8 character long!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="face_recognition")
                my_cursor = conn.cursor()

                if self.password_new1_entry.get() != self.confirm_password_entry.get():
                    messagebox.showerror("Error", "Incorrect Confirm Password")
                elif self.password_new1_entry.get() == self.confirm_password_entry.get():
                    my_cursor.execute(
                        "update register set password=%s where email=%s",
                        (
                         self.password_new1_entry.get(),
                         self.send_email.get()
                         ))
                    messagebox.showinfo("Success", f"New Password Has Been Registered Successfully!",
                                        parent=self.root)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)
    # def logout(self):
    #     if self.select==11:
    #         self.bg_img.destroy()
    #         self.main_frame.destroy()
    #         self.login()


    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # _______________________SCREEN LAYOUTS---------------------------------------------------------------------

    # __________________________SCREEN1 MAIN PAGE__________________________________________________________________________________________

    def mainPage(self):
        if self.select == 1:
            self.screen1.destroy()
        elif self.select == 2:
            self.bg_img_student.destroy()
        elif self.select == 3:
            self.bg_img_attendence.destroy()
            self.main_frame_attendence.destroy()
        elif self.select == 4:
            self.bg_img_library.destroy()
        elif self.select == 5:
            self.bg_img_view.destroy()
            self.main_frame_view.destroy()
        elif self.select==6:
            self.image_panel1.destroy()
        elif self.select == 10:
            self.bg_img_help.destroy()
        self.select = 11
        global select
        select = self.select

        # label = Label(self.screen3, text='FACE RECOGINITION ATTENDENCE SYSTEM', bg="firebrick", width='300', height=3,
        #               font=('Copperplate Gothic Bold', 25, 'bold'))

        # Background Image
        img3 = Image.open(r"images\frame.png")
        img3 = img3.resize((1300, 737), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.bg_img = Label(self.root, image=self.photoimg3)
        self.bg_img.place(x=0, y=0, width=1300, height=737)

        # Main Frame
        self.main_frame = Frame(self.root, bd=2, background="white")
        self.main_frame.place(x=40, y=37, width=1219, height=660)

        # =================================== Time =========================================
        self.clock_image = ImageTk.PhotoImage(file="images/time.png")
        self.date_time_image = Label(self.main_frame, image=self.clock_image, bg="white", activebackground="white")
        self.date_time_image.place(x=0, y=7)

        self.date_time = Label(self.root)
        self.date_time.place(x=75, y=40)
        self.time_running()

        # ========================== Heading =====================================
        self.txt = "Welcome to Face Recognition Attendance System"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.main_frame, text=self.txt, font=('yu gothic ui', 20, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=250, y=2, width=650)
        self.slider()
        self.heading_color()

        # ============================Current user================================
        self.current_user_image = ImageTk.PhotoImage(file="images/current_user.png")
        self.current_user_label = Label(self.main_frame, image=self.current_user_image, bg="white")
        self.current_user_label.place(x=920, y=3)

        self.current_user = Label(self.main_frame, bg="white", text=self.username.get(),
                                  font=("yu gothic ui", 10, "bold"), fg="#DC143C")
        self.current_user.place(x=950, y=5)
        # ============================Logout button===============================
        self.logout = ImageTk.PhotoImage(file="images\logout.png")
        self.logout_button = Button(self.main_frame, image=self.logout,command=self.login,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        self.logout_button.place(x=1130, y=3)

        # ============================ Line ================================
        line = Image.open(r"images\line.png")
        line = line.resize((1220, 10), Image.ANTIALIAS)
        self.line = ImageTk.PhotoImage(line)

        bg_img = Label(self.main_frame, image=self.line, bg="white")
        bg_img.place(x=0, y=50, width=1220, height=10)

        # ============================Home Frame====================================
        home_frame = Frame(self.main_frame)
        home_frame.place(x=0, y=70, height=117, width=115)

        # ============================Home button====================================
        self.home = ImageTk.PhotoImage(file='images/home.png')
        self.home_button = Button(home_frame, image=self.home,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.home_button.place(x=0, y=0)

        # ============================View Frame====================================
        view_frame = Frame(self.main_frame)
        view_frame.place(x=0, y=280, height=120, width=117)

        # ============================View button====================================
        self.view = ImageTk.PhotoImage(file='images/view.png')
        self.view_button = Button(view_frame, image=self.view, command=self.view_attendence,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.view_button.place(x=0, y=0)

        # ============================ Exit Frame====================================
        exit_frame = Frame(self.main_frame)
        exit_frame.place(x=0, y=500, height=120, width=125)

        # ============================ Exit button====================================
        self.exit = ImageTk.PhotoImage(file='images/exit.png')
        self.exit_button = Button(exit_frame, image=self.exit, command=self.Exit,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")

        self.exit_button.place(x=0, y=0)

        # =========================== Manage Frame ===========================================
        manage_frame = Image.open(r"images\manage frame.png")
        manage_frame = manage_frame.resize((1104, 597), Image.ANTIALIAS)
        self.manage_frame = ImageTk.PhotoImage(manage_frame)

        manage_frame = Label(self.main_frame, image=self.manage_frame, bg="white")
        manage_frame.place(x=120, y=58, width=1104, height=597)

        # =================== Student Details =======================
        self.student = ImageTk.PhotoImage(file='images/student-details.png')
        self.student_button = Button(manage_frame, image=self.student, command=self.student_details,
                                     font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                     , borderwidth=0, background="white", cursor="hand2")

        self.student_button.place(x=139, y=163, width=136, height=123)

        # =================== Face Recognition =======================
        self.face_recognition = ImageTk.PhotoImage(file='images/attendance.png')
        self.face_recognition_button = Button(manage_frame, image=self.face_recognition, command=self.Facerecognition,
                                              font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                              , borderwidth=0, background="white", cursor="hand2")

        self.face_recognition_button.place(x=473, y=163, width=136, height=123)

        # =================== Attendance =======================
        self.attendance = ImageTk.PhotoImage(file='images/courses.png')
        self.attendance_button = Button(manage_frame, image=self.attendance, command=self.library,
                                        font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                        , borderwidth=0, background="white", cursor="hand2")

        self.attendance_button.place(x=809, y=163, width=136, height=123)

        # =================== Train Data =======================
        self.train_data = ImageTk.PhotoImage(file='images/train_data.png')
        self.train_data_button = Button(manage_frame, image=self.train_data, command=self.train_classifier,
                                        font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                        , borderwidth=0, background="white", cursor="hand2")

        self.train_data_button.place(x=140, y=415, width=134, height=123)

        # =================== Photos =======================
        self.photos = ImageTk.PhotoImage(file='images/photos.png')
        self.photos_button = Button(manage_frame, image=self.photos, command=self.open_image,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")

        self.photos_button.place(x=475, y=412, width=134, height=126)

        # =================== Help Desk =======================
        self.help_desk = ImageTk.PhotoImage(file='images/help_desk.png')
        self.help_desk_button = Button(manage_frame, image=self.help_desk,command=self.help_desk_f,
                                       font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                       , borderwidth=0, background="white", cursor="hand2")

        self.help_desk_button.place(x=809, y=415, width=134, height=123)

    def time_running(self):
        """ displays the current date and time which is shown at top left corner of admin dashboard"""
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        concated_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=concated_text, font=("yu gothic ui", 13, "bold"), relief=FLAT, borderwidth=0,
                                 background="white", foreground="black")
        self.date_time.after(100, self.time_running)

    def slider(self):
        """creates slides for heading by taking the text,
		and that text are called after every 150 ms"""
        if self.count >= len(self.txt):
            self.count = -1
            self.text = ''
            self.heading.config(text=self.text)

        else:
            self.text = self.text + self.txt[self.count]
            self.heading.config(text=self.text)
        self.count += 1

        self.heading.after(150, self.slider)

    def heading_color(self):
        """
		configures heading label
		:return: every 50 ms returned new random color.

		"""
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    # def student_details(self):
    # 	self.new_window = Toplevel(self.root)
    # 	self.app = Student(self.new_window)

    def open_image(self):
        os.startfile("data")

    # def traindata(self):
    # 	self.new_window = Toplevel(self.root)
    # 	self.app1 = Train(self.new_window)
    #
    # def facerecognition(self):
    # 	self.new_window = Toplevel(self.root)
    # 	self.app2 = face_recognition(self.new_window)

    # 	self.new_window = Toplevel(self.root)
    # # 	self.app = Student(self.new_window)
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # __________________________________________________SCREEN2 STUDENT DETAILS_____________________________________________________
    def student_details(self):
        self.bg_img.destroy()
        self.main_frame.destroy()
        # Variables
        self.select = 2
        global select
        select = self.select
        # Variable for radio button
        self.var_radio_btn = StringVar()

        # Background Image
        img3 = Image.open(r"images\framenew.png")
        img3 = img3.resize((1300, 750), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.bg_img_student = Label(self.root, image=self.photoimg3)
        self.bg_img_student.place(x=0, y=0, width=1300, height=750)
        # Backarrow Image
        img = Image.open(r"images\Back-Arrow-Icon-PNG.png")
        img = img.resize((80, 73), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bgarrow_img1 = Button(self.bg_img_student, image=self.photoimg, command=self.mainPage, bg="white",
                              activebackground="white", border=0)
        bgarrow_img1.place(x=25, y=20, width=80, height=73)
        ##################    TITTLE      #################################
        self.txt = "Student Details"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.bg_img_student, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=460, y=20, width=450)
        self.slider()
        self.heading_color()

        # ========================left frame==================================

        # LeftLabel Frame
        self.Left_frame_student = LabelFrame(self.bg_img_student, bd=4, bg="white", relief=RIDGE,
                                             text="Student Details",
                                             font=("times new roman", 12, "bold"))
        self.Left_frame_student.place(x=20, y=100, width=625, height=570)

        # Current Course Information
        Current_course_frame = LabelFrame(self.Left_frame_student, bd=4, bg="white", relief=RIDGE,
                                          text="Current Course Information",
                                          font=("times new roman", 12, "bold"))
        Current_course_frame.place(x=5, y=15, width=608, height=150)

        def pick_book(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
            my_cursor = conn.cursor()
            sem = semester_combo.get()
            dep = department_combo.get()
            my_cursor.execute("SELECT book_name from book WHERE semester=%s AND department=%s", (sem, dep,))
            data = my_cursor.fetchall()
            my_list = [r for r in data]
            course_combo.config(value=my_list)
            conn.commit()
            conn.close()

        # 1 - Department Label
        department_label = Label(Current_course_frame, text="Department", font=('yu gothic ui semibold', 12, 'bold'),
                                 bg="white")
        department_label.grid(row=0, column=0, padx=10, sticky=W)

        # 1 - Department ComboBox
        department_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_department,
                                        font=('yu gothic ui semibold', 12, 'bold'), state="readonly", width=20)
        department_combo.option_add("*TCombobox*Listbox.selectBackground", "#DC143C")
        department_combo.option_add("*TCombobox*Listbox.foreground", "black")
        department_combo["values"] = (
            "Select Department", "Computer Science", "Electronics", "Civil", "Electrical", "AutoMobile")
        department_combo.current(0)
        department_combo.bind("<<ComboboxSelected>>", pick_book)
        department_combo.grid(row=0, column=1, padx=2, pady=20, sticky=W)

        # 2 - Course Label
        course_label = Label(Current_course_frame, text="Course", font=('yu gothic ui semibold', 12, 'bold'),
                             bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        # 2 - Course ComboBox
        course_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_course,
                                    font=('yu gothic ui semibold', 12, 'bold'), state="readonly", width=18,
                                    values=["Select Course"])
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=20, sticky=W)

        # 3 - Semester Label
        semester_label = Label(Current_course_frame, text="Semester", font=('yu gothic ui semibold', 12, 'bold'),
                               bg="white")
        semester_label.grid(row=1, column=0, padx=10, sticky=W)

        # 3 - Semester ComboBox
        semester_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_semester,
                                      font=('yu gothic ui semibold', 12, 'bold'), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6")
        semester_combo.current(0)
        semester_combo.bind("<<ComboboxSelected>>", pick_book)
        semester_combo.grid(row=1, column=1, padx=2, pady=20, sticky=W)

        # 4 - Year Label
        year_label = Label(Current_course_frame, text="Year", font=('yu gothic ui semibold', 12, 'bold'), bg="white")
        year_label.grid(row=1, column=2, padx=10, sticky=W)

        # 4 - Year ComboBox
        year_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_year,
                                  font=('yu gothic ui semibold', 12, 'bold'), state="readonly", width=18)
        year_combo["values"] = (
            "Select Year", "2021-2022", "2022-2023", "2023-2024", "2024-2025", "2025-2026", "2026-2027")
        year_combo.current(0)
        year_combo.grid(row=1, column=3, padx=2, pady=20, sticky=W)

        # Student Information
        class_Student_frame = LabelFrame(self.Left_frame_student, bd=4, bg="white", relief=RIDGE,
                                         text="Student Information",
                                         font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=5, y=190, width=608, height=300)

        # 1 - Student Id Label
        studentId_label = Label(class_Student_frame, text="Student ID:", font=('yu gothic ui semibold', 13, 'bold'),
                                bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # 1 - Student Id Entry

        studentId_entry = Entry(class_Student_frame, textvariable=self.var_student_id, width=15, highlightthickness=0,
                                bg="white", relief=FLAT,
                                font=("yu gothic ui semibold", 12))
        studentId_entry.grid(row=0, column=1, padx=6, pady=1, sticky=W)

        studentId_line = Canvas(class_Student_frame, width=140, height=1.3, bg="#393939", highlightthickness=0)
        studentId_line.place(x=140, y=25)

        # 2 - Student Name Label
        studentId_label = Label(class_Student_frame, text="Student Name:", font=('yu gothic ui semibold', 13, 'bold'),
                                bg="white")
        studentId_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # 2 - Student Name Entry
        student_Name_entry = Entry(class_Student_frame, textvariable=self.var_student_name, width=15,
                                   highlightthickness=0, bg="white", relief=FLAT,
                                   font=("yu gothic ui semibold", 12))
        student_Name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        studentName_line = Canvas(class_Student_frame, width=140, height=1.3, bg="#393939", highlightthickness=0)
        studentName_line.place(x=454, y=25)

        # 3 - Class Division Label
        class_division_label = Label(class_Student_frame, text="Class Division:",
                                     font=('yu gothic ui semibold', 13, 'bold'),
                                     bg="white")
        class_division_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        # 3 - Class Division Entry
        class_division_entry = Entry(class_Student_frame, textvariable=self.var_div, width=15, highlightthickness=0,
                                     bg="white", relief=FLAT,
                                     font=("yu gothic ui semibold", 12))
        class_division_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        class_division_line = Canvas(class_Student_frame, width=140, height=1.3, bg="#393939", highlightthickness=0)
        class_division_line.place(x=150, y=60)

        # 4 - Roll No. Label
        roll_no_label = Label(class_Student_frame, text="Roll No:", font=('yu gothic ui semibold', 13, 'bold'),
                              bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        # 4 - Roll No. Entry
        roll_no_entry = Entry(class_Student_frame, textvariable=self.var_roll_no, width=15, highlightthickness=0,
                              bg="white", relief=FLAT,
                              font=("yu gothic ui semibold", 12))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        roll_no_line = Canvas(class_Student_frame, width=140, height=1.3, bg="#393939", highlightthickness=0)
        roll_no_line.place(x=454, y=60)

        # 5 - Gender Label
        gender_label = Label(class_Student_frame, text="Gender:", font=('yu gothic ui semibold', 13, 'bold'),
                             bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        # 5 - Gender CombBox
        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender,
                                    font=("times new roman", 13, "bold"), state="readonly", width=13)
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # 6 - DOB Label
        dob_label = Label(class_Student_frame, text="DOB:", font=('yu gothic ui semibold', 13, 'bold'), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        # 6 - DOB Entry
        dob_entry = Entry(class_Student_frame, textvariable=self.var_dob, width=15, highlightthickness=0,
                          bg="white", relief=FLAT,
                          font=("yu gothic ui semibold", 12))
        dob_entry.insert(0, "mm/dd/yyyy")
        dob_entry.configure(state=DISABLED)
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        def on_click(event):
            dob_entry.configure(state=NORMAL)
            dob_entry.delete(0, END)

            # make the callback only work once
            dob_entry.unbind('<Button-1>', on_click_id)

        on_click_id = dob_entry.bind('<Button-1>', on_click)

        dob_entry_line = Canvas(class_Student_frame, width=140, height=1.3, bg="#393939", highlightthickness=0)
        dob_entry_line.place(x=454, y=95)

        # 7 - Email Label
        email_label = Label(class_Student_frame, text="Email:", font=('yu gothic ui semibold', 13, 'bold'),
                            bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        # 7 - Email Entry
        email_entry = Entry(class_Student_frame, textvariable=self.var_email, width=15, highlightthickness=0,
                            bg="white", relief=FLAT,
                            font=("yu gothic ui semibold", 12))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        email_entry_line = Canvas(class_Student_frame, width=140, height=1.3, bg="#393939", highlightthickness=0)
        email_entry_line.place(x=150, y=130)

        # 8 - Phone No. Label
        phone_no_label = Label(class_Student_frame, text="Phone No:", font=('yu gothic ui semibold', 13, 'bold'),
                               bg="white")
        phone_no_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        # 8 - Phone No. Entry
        phone_no_entry = Entry(class_Student_frame, textvariable=self.var_phone, width=15, highlightthickness=0,
                               bg="white", relief=FLAT,
                               font=("yu gothic ui semibold", 12))
        phone_no_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        phone_no_entry_line = Canvas(class_Student_frame, width=140, height=1.3, bg="#393939", highlightthickness=0)
        phone_no_entry_line.place(x=454, y=130)

        # 9 - Address Label
        address_label = Label(class_Student_frame, text="Address:", font=('yu gothic ui semibold', 13, 'bold'),
                              bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        # 9 - Address Entry
        address_entry = Entry(class_Student_frame, textvariable=self.var_address, width=15, highlightthickness=0,
                              bg="white", relief=FLAT,
                              font=("yu gothic ui semibold", 12))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        address_entry_line = Canvas(class_Student_frame, width=140, height=1.3, bg="#393939", highlightthickness=0)
        address_entry_line.place(x=150, y=165)

        # 10 - Teacher Name Label
        teacher_name_label = Label(class_Student_frame, text="Teacher Name:",
                                   font=('yu gothic ui semibold', 13, 'bold'),
                                   bg="white")
        teacher_name_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        # 10 - Teacher Name Entry
        teacher_name_entry = Entry(class_Student_frame, textvariable=self.var_teacher, width=15, highlightthickness=0,
                                   bg="white", relief=FLAT,
                                   font=("yu gothic ui semibold", 12))
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        email_entry_line = Canvas(class_Student_frame, width=140, height=1.3, bg="#393939", highlightthickness=0)
        email_entry_line.place(x=454, y=165)

        # Radio Buttons
        radiobtn1 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio_btn, text="Take Photo Sample",
                                    value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio_btn, text="No Photo Sample",
                                    value="No")
        radiobtn2.grid(row=6, column=1)

        # Buttons Frame for save, update, delete and update
        btn_frame = Frame(class_Student_frame, bd=2, relief=GROOVE)
        btn_frame.place(x=3, y=194, width=596, height=70)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=14,
                          font=("times new roman", 13, "bold"),
                          bg="crimson", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=14,
                            font=("times new roman", 13, "bold"), bg="crimson",
                            fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=14,
                            font=("times new roman", 13, "bold"), bg="crimson",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=14,
                           font=("times new roman", 13, "bold"), bg="crimson",
                           fg="white")
        reset_btn.grid(row=0, column=3)

        # Button Frame for take and update photo sample
        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=5, y=229, width=593, height=38)

        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", width=29, command=self.generate_dataset,
                                font=("times new roman", 13, "bold"),
                                bg="crimson", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=28, command=self.generate_dataset,
                                  font=("times new roman", 13, "bold"), bg="crimson", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # -------------------------------------------------Right  FRAME---------------------------------------------------------------------------------

        # Right LabelFrame
        self.Right_frame_student = LabelFrame(self.bg_img_student, bd=4, bg="white", relief=RIDGE,
                                              text="Student Details",
                                              font=("times new roman", 12, "bold"))
        self.Right_frame_student.place(x=640, y=100, width=625, height=570)

        # Image On Right Frame
        img_right = Image.open(r"images\current_course.jpg")
        img_right = img_right.resize((608, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.Right_frame_student, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=608, height=130)

        # Search LabelFrame
        Search_frame = LabelFrame(self.Right_frame_student, bd=4, bg="white", relief=RIDGE, text="Search System",
                                  font=("times new roman", 12, "bold"))
        Search_frame.place(x=2, y=135, width=612, height=74)

        # Search Label
        Search_label = Label(Search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="white")
        Search_label.grid(row=0, column=0, padx=3, pady=10, sticky=W)

        # Search Combobox
        Search_combo = ttk.Combobox(Search_frame, font=("times new roman", 13, "bold"),textvariable=self.student_search,state="readonly", width=13)
        Search_combo["values"] = ("Select", "department", "roll_no","student_name","semester")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=0, pady=10, sticky=W)

        Search_entry = ttk.Entry(Search_frame, width=15,textvariable=self.student_textsearch, font=("times new roman", 13, "bold"))
        Search_entry.grid(row=0, column=2, padx=6, pady=5, sticky=W)

        # Search Button
        Search_btn = Button(Search_frame, text="Search", width=9, font=("times new roman", 13, "bold"), bg="crimson",command=self.search_student,
                            fg="white")
        Search_btn.grid(row=0, column=3, padx=2)

        # Show All Button
        showAll_btn = Button(Search_frame, text="Show All", width=9, font=("times new roman", 13, "bold"), bg="crimson",command=self.fetch_data,
                             fg="white")
        showAll_btn.grid(row=0, column=4, padx=10)

        # Table Frame
        table_frame = Frame(self.Right_frame_student, bd=4, relief=RIDGE, bg="white")
        table_frame.place(x=4, y=218, width=610, height=280)

        # Scrollbar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Add some style
        style = ttk.Style()

        # Pick a theme
        style.theme_use("clam")

        # Configure our treeview colors
        style.configure("Treeview", background="white", rowheight=25, fieldbackground="white",
                        font=("times new roman", 10, "bold"))

        # Change selected color
        style.map("Treeview", background=[("selected", "#DC143C")])

        self.student_table = ttk.Treeview(table_frame, column=(
            "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address",
            "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # Text in center
        self.student_table.column("dep", anchor=CENTER)
        self.student_table.column("course", anchor=CENTER)
        self.student_table.column("year", anchor=CENTER)
        self.student_table.column("sem", anchor=CENTER)
        self.student_table.column("id", anchor=CENTER)
        self.student_table.column("name", anchor=CENTER)
        self.student_table.column("div", anchor=CENTER)
        self.student_table.column("roll", anchor=CENTER)
        self.student_table.column("gender", anchor=CENTER)
        self.student_table.column("dob", anchor=CENTER)
        self.student_table.column("email", anchor=CENTER)
        self.student_table.column("phone", anchor=CENTER)
        self.student_table.column("address", anchor=CENTER)
        self.student_table.column("teacher", anchor=CENTER)
        self.student_table.column("photo", anchor=CENTER)

        self.student_table.tag_configure("oddrow", background="white")
        self.student_table.tag_configure("evenrow", background="#f1ad98")

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="RollNo")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ------------------ add data in database ----------------------
    def add_data(self):
        if self.var_department.get() == "Select Department" or self.var_student_name.get() == "" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_div.get() == "" or self.var_roll_no.get() == "" or self.var_dob.get() == "" or self.var_gender.get() == "Select Gender" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "" :
            messagebox.showerror("Error", "All Fields Are Required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_student_id.get(),
                    self.var_student_name.get(),
                    self.var_div.get(),
                    self.var_roll_no.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio_btn.get(), "",
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # ----------------------------------- fetch data from database into table --------------------------------------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student where status=''")
        data = my_cursor.fetchall()
        count = 0

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                if count % 2 == 0:
                    self.student_table.insert("", END, values=i, tags="evenrow")
                else:
                    self.student_table.insert("", END, values=i, tags="oddrow")
                count += 1
            conn.commit()
        conn.close()

    #     --------------------------- get cursor -----------------------------
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_department.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_student_id.set(data[4]),
        self.var_student_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll_no.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio_btn.set(data[14])

    # ------------------------- update function ---------------------------
    def update_data(self):
        if self.var_department.get() == "Select Department" or self.var_student_name.get() == "" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_div.get() == "" or self.var_roll_no.get() == "" or self.var_dob.get() == "" or self.var_gender.get() == "Select Gender" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "" or self.var_radio_btn == "":

            messagebox.showerror("Error", "All Fields Are Required!", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do You Want To Update This Student Details!", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set department=%s, course=%s, year=%s, semester=%s, student_name=%s, division=%s, roll_no=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo_sample=%s where student_id=%s",
                        (
                            self.var_department.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_student_name.get(),
                            self.var_div.get(),
                            self.var_roll_no.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio_btn.get(),
                            self.var_student_id.get(),
                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student Details Updated Successfully!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ------------------------------- Delete Data ------------------------------------------------------------------

    def delete_data(self):
        if self.var_student_id == "":
            messagebox.showerror("Error", "Student Id is Required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Success", "Do You Want To Delete This Data!", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set status='deleted' where student_id=%s",
                                      (self.var_student_id.get(),))

                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details Deleted Successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    #     --------------------------------------- Reset Data ----------------------------------------------
    def reset_data(self):
        self.var_department.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_student_name.set(""),
        self.var_div.set(""),
        self.var_roll_no.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio_btn.set(""),
        self.var_student_id.set("")

    #    ---------------------------------------- Generate data set or take photo sample ----------------------------------------------
    def generate_dataset(self):
        if self.var_department.get() == "Select Department" or self.var_student_name.get() == "" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_div.get() == "" or self.var_roll_no.get() == "" or self.var_dob.get() == "" or self.var_gender.get() == "Select Gender" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "" or self.var_radio_btn == "":
            messagebox.showerror("Error", "All Fields Are Required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = self.var_student_id.get()
                id = int(id)
                # for i in myresult:
                #     id += 1
                my_cursor.execute(
                    "update student set department=%s, course=%s, year=%s, semester=%s, student_name=%s, division=%s, roll_no=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo_sample=%s where student_id=%s",
                    (self.var_department.get(),
                     self.var_course.get(),
                     self.var_year.get(),
                     self.var_semester.get(),
                     self.var_student_name.get(),
                     self.var_div.get(),
                     self.var_roll_no.get(),
                     self.var_gender.get(),
                     self.var_dob.get(),
                     self.var_email.get(),
                     self.var_phone.get(),
                     self.var_address.get(),
                     self.var_teacher.get(),
                     self.var_radio_btn.get(),
                     self.var_student_id.get() == id
                     ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #     ------------ Load predefined data of face frontal from opencv for object detection--------------------
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    images = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    # Detect faces of different sizes
                    faces = face_classifier.detectMultiScale(images, 1.3, 5)
                    #                                       scaling factor=1.3 (how much the image size is reduced at each image scale)
                    #                                       minimum neighbor=5 (affect the quality of the detected faces)
                    # Generate Rectangle
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                capture = cv2.VideoCapture(1)
                capture.set(3, 1280)
                capture.set(4, 720)
                img_id = 0
                while True:
                    ret, my_frame = capture.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id == 100):
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def search_student(self):
        print("hlo", self.search.get(), self.text_search.get())
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student where " + str(self.student_search.get()) + " LIKE '%" + str(
            self.student_textsearch.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in rows:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ==================================================ATTENDENCEE===============================================================

    def Facerecognition(self):
        if self.select2 == 1:
            self.bg_img.destroy()
        self.bg_img.destroy()
        self.main_frame.destroy()
        self.select = 3

        global select
        select = self.select
        # Background Image
        img3 = Image.open(r"images\detectionframe.png")
        img3 = img3.resize((1300, 737), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.bg_img_attendence = Label(self.root, image=self.photoimg3)
        self.bg_img_attendence.place(x=0, y=0, width=1300, height=737)

        # Main Frame
        self.main_frame_attendence = Frame(self.root, bd=2, background="white")
        self.main_frame_attendence.place(x=207, y=39, width=885, height=660)

        # =================================== Time =========================================
        self.clock_image = ImageTk.PhotoImage(file="images/time.png")
        self.date_time_image = Label(self.main_frame_attendence, image=self.clock_image, background="white",
                                     activebackground="white")
        self.date_time_image.place(x=0, y=7)

        self.date_time = Label(self.root)
        self.date_time.place(x=240, y=40)
        self.time_running()

        # ========================== Heading =====================================
        self.txt = "Attendance System"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.main_frame_attendence, text=self.txt, font=('yu gothic ui', 20, "bold"), bg="white",
                             fg='black', bd=5,
                             relief=FLAT)
        self.heading.place(x=140, y=2, width=600)
        self.slider()
        self.heading_color()

        # ============================Current user================================
        self.current_user_image = ImageTk.PhotoImage(file="images/current_user.png")
        self.current_user_label = Label(self.main_frame_attendence, image=self.current_user_image, bg="white")
        self.current_user_label.place(x=630, y=3)

        self.current_user = Label(self.main_frame_attendence, bg="white", text=self.username.get(),
                                  font=("yu gothic ui", 10, "bold"), fg="#DC143C")
        self.current_user.place(x=660, y=7)

        # ============================ Line ================================
        line = Image.open(r"images\line.png")
        line = line.resize((1220, 10), Image.ANTIALIAS)
        self.line = ImageTk.PhotoImage(line)

        bg_img = Label(self.main_frame_attendence, image=self.line, bg="white")
        bg_img.place(x=7, y=50, width=867, height=10)

        # ============================Home Frame====================================
        home_frame = Frame(self.main_frame_attendence)
        home_frame.place(x=0, y=70, height=117, width=115)

        # ============================Home button====================================
        self.home = ImageTk.PhotoImage(file='images/home.png')
        self.home_button = Button(home_frame, image=self.home, command=self.mainPage,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.home_button.place(x=0, y=0)

        # ============================View Frame====================================
        view_frame = Frame(self.main_frame_attendence)
        view_frame.place(x=0, y=280, height=120, width=117)

        # ============================View button====================================
        self.view = ImageTk.PhotoImage(file='images/view.png')
        self.view_button = Button(view_frame, image=self.view, command=self.view_attendence,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.view_button.place(x=0, y=0)

        # ============================ Exit Frame====================================
        exit_frame = Frame(self.main_frame_attendence)
        exit_frame.place(x=0, y=500, height=120, width=125)

        # ============================ Exit button====================================
        self.exit = ImageTk.PhotoImage(file='images/exit.png')
        self.exit_button = Button(exit_frame, image=self.exit, command=self.Exit, font=("yu gothic ui", 13, "bold"),
                                  relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")

        self.exit_button.place(x=0, y=0)

        # =========================== Manage Frame ===========================================
        manage_frame = Image.open(r"images\backround_attendance.png")
        manage_frame = manage_frame.resize((700, 520), Image.ANTIALIAS)
        self.manage_frame = ImageTk.PhotoImage(manage_frame)

        manage_frame = Label(self.main_frame_attendence, image=self.manage_frame, bg="white")
        manage_frame.place(x=150, y=90, width=700, height=530)

        # =================== Check In =======================
        self.check_in = ImageTk.PhotoImage(file='images/check_in.png')
        self.check_in_button = Button(manage_frame, image=self.check_in, command=self.face_recog,
                                      font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                      , borderwidth=0, background="white", cursor="hand2", state=NORMAL)

        self.check_in_button.place(x=116, y=186, width=136, height=123)

        # =================== Check Out =======================
        self.check_out = ImageTk.PhotoImage(file='images/check_out.png')
        self.check_out_button = Button(manage_frame, image=self.check_out,
                                       font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white",
                                       command=self.face_recog_check_out
                                       , borderwidth=0, background="white", cursor="hand2")

        self.check_out_button.place(x=450, y=186, width=136, height=123)

    # ============================ Attendance for login =======================================
    def mark_attendance(self, recognised_student_roll, recognised_student_name, recognised_student_dep):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        query = ("SELECT status  from attendence  WHERE name='%s' ORDER BY login_datetime  DESC LIMIT 1")
        my_cursor.execute(query % (recognised_student_name))
        recognised_student_status = my_cursor.fetchone()
        if (recognised_student_status != None):
            recognised_student_status_new = recognised_student_status[0]
        else:
            recognised_student_status_new = None

        conn.commit()
        conn.close()
        connection = mysql.connector.connect(host="localhost", username="root", password="",
                                             database="face_recognition")
        my_cursor = connection.cursor()

        my_cursor.execute("SELECT roll_no  from attendence")
        data = my_cursor.fetchall()
        name_list = [r for r in data]
        connection.commit()
        connection.close()

        if any((recognised_student_roll in i for i in name_list)):
            if ((recognised_student_status_new == "checkout")):
                connect = mysql.connector.connect(host="localhost", username="root", password="",
                                                  database="face_recognition")
                my_cursor = connect.cursor()

                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                query = "INSERT INTO attendence (id, name,roll_no,department,login_datetime,status)VALUES (%s,%s,%s,%s,%s,%s)"
                my_cursor.execute(query, (
                    "",
                    recognised_student_name,
                    recognised_student_roll,
                    recognised_student_dep,
                    timestamp, "checkin"
                ))
                connect.commit()
                connect.close()
        elif any(recognised_student_roll not in i for i in name_list):
            connect = mysql.connector.connect(host="localhost", username="root", password="",
                                              database="face_recognition")
            my_cursor = connect.cursor()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            query = "INSERT INTO attendence (id, name,roll_no,department,login_datetime,status)VALUES (%s,%s,%s,%s,%s,%s)"
            my_cursor.execute(query, (
                "",
                recognised_student_name,
                recognised_student_roll,
                recognised_student_dep,
                timestamp, "checkin"
            ))
            connect.commit()
            connect.close()
        elif (name_list == []):
            connect = mysql.connector.connect(host="localhost", username="root", password="",
                                              database="face_recognition")
            my_cursor = connect.cursor()

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            query = "INSERT INTO attendence (id, name,roll_no,department,login_datetime,status)VALUES (%s,%s,%s,%s,%s,%s)"
            my_cursor.execute(query, (
                "",
                recognised_student_name,
                recognised_student_roll,
                recognised_student_dep,
                timestamp, "checkin"
            ))
            connect.commit()
            connect.close()
        else:
            print("cant checkin")

    # ================================= Attendance for checkout ================================
    def mark_attendance_check_out(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        query = ("SELECT status  from attendence  WHERE name='%s' ORDER BY login_datetime  DESC LIMIT 1")
        my_cursor.execute(query % (self.recognised_student_name))
        recognised_student_status = my_cursor.fetchone()
        if (recognised_student_status != None):
            self.recognised_student_status_new = recognised_student_status[0]
        else:
            self.recognised_student_status_new = None

        conn.commit()
        conn.close()
        connection = mysql.connector.connect(host="localhost", username="root", password="",
                                             database="face_recognition")
        my_cursor = connection.cursor()

        my_cursor.execute("SELECT roll_no  from attendence")
        data = my_cursor.fetchall()
        name_list = [r for r in data]
        connection.commit()
        connection.close()

        if self.var_semester.get() == "Select Semester" or self.var_course.get() == "Select Book" or self.var_author.get() == "Select Author":
            messagebox.showerror("Error", "All Fields Are Required!", parent=self.root)
        elif any((self.recognised_student_roll in i for i in name_list)):
            if self.recognised_student_status_new == "checkin":
                connect = mysql.connector.connect(host="localhost", username="root", password="",
                                                  database="face_recognition")
                my_cursor = connect.cursor()
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                query = "INSERT INTO attendence (id, name,roll_no,department,login_datetime,status,semester,book,author)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                my_cursor.execute(query, (
                    "",
                    self.recognised_student_name,
                    self.recognised_student_roll,
                    self.recognised_student_dep,
                    timestamp, "checkout", self.var_semester.get(), self.var_course.get(), self.var_author.get()
                ))
                messagebox.showinfo("Success", f"Your Information is Added Successfully!",
                                    parent=self.root)
                connect.commit()
                connect.close()
        else:
            print("cant checkout")

    # ==============================face recognition============================
    def face_recog(self):
        self.counter = 0

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("select student_name from student where student_id=" + str(id))
                recognised_student_name = my_cursor.fetchone()
                recognised_student_name = "+".join(recognised_student_name)

                my_cursor.execute("select roll_no from student where student_id=" + str(id))
                recognised_student_roll = my_cursor.fetchone()
                recognised_student_roll = "+".join(recognised_student_roll)

                my_cursor.execute("select department from student where student_id=" + str(id))
                recognised_student_dep = my_cursor.fetchone()
                recognised_student_dep = "+".join(recognised_student_dep)

                if confidence > 77:
                    cv2.putText(img, f"Roll:{recognised_student_roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{recognised_student_name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{recognised_student_dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 255, 255), 3)
                    self.counter += 1
                    if self.counter == 1:
                        self.mark_attendance(recognised_student_roll, recognised_student_name, recognised_student_dep)
                    else:
                        pass
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "FACE", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(1)

        while TRUE:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("welcome to face recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

    # 	=========== face recognition checkout ========================
    def face_recog_check_out(self):
        self.counter = 0

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for [x, y, w, h] in features:
                # np=np.array(img, 'uint8')
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("select student_name from student where student_id=" + str(id))
                recognised_student_name = my_cursor.fetchone()
                self.recognised_student_name = "+".join(recognised_student_name)

                my_cursor.execute("select roll_no from student where student_id=" + str(id))
                recognised_student_roll = my_cursor.fetchone()
                self.recognised_student_roll = "+".join(recognised_student_roll)

                my_cursor.execute("select department from student where student_id=" + str(id))
                recognised_student_dep = my_cursor.fetchone()
                self.recognised_student_dep = "+".join(recognised_student_dep)

                if confidence > 77:
                    cv2.putText(img, f"Roll:{self.recognised_student_roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{self.recognised_student_name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{self.recognised_student_dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX,
                                0.8,
                                (255, 255, 255), 3)
                    self.counter += 1
                # if self.counter == 1:
                #     self.mark_attendance_check_out(recognised_student_roll, recognised_student_name,
                #                                    recognised_student_dep)
                # else:
                #     pass
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "FACE", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(1)

        while TRUE:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("welcome to face recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        self.checoutpaage_two(self.recognised_student_dep, self.recognised_student_name, self.recognised_student_roll)

    def checoutpaage_two(self, recognised_student_dep, recognised_student_name, recognised_student_roll):
        self.select2 = 1
        global select2
        select2 = self.select2
        # Background Image
        img3 = Image.open(r"images\book_frame.png")
        img3 = img3.resize((1300, 737), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.bg_img = Label(self.root, image=self.photoimg3)
        self.bg_img.place(x=0, y=0, width=1300, height=737)

        # Backarrow Image
        img = Image.open(r"images\Back-Arrow-Icon-PNG.png")
        img = img.resize((80, 73), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        barrow_img1 = Button(self.bg_img, image=self.photoimg, command=self.Facerecognition, bg="white",
                             activebackground="white", border=0)
        barrow_img1.place(x=270, y=40, width=80, height=73)

        def pick_book(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
            my_cursor = conn.cursor()
            sem = semester_combo.get()
            dep = department_combo.get()
            my_cursor.execute("SELECT book_name from book WHERE semester=%s AND department=%s", (sem, dep,))
            data = my_cursor.fetchall()
            my_list = [r for r in data]
            course_combo.config(value=my_list)
            conn.commit()
            conn.close()

        def pick_author(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
            my_cursor = conn.cursor()
            book = course_combo.get()
            my_cursor.execute("SELECT author from book WHERE book_name=%s", (book,))
            data1 = my_cursor.fetchall()
            my_list1 = [r for r in data1]
            author_combo.config(value=my_list1)
            print(my_list1)
            conn.commit()
            conn.close()

        # Department ComboBox
        department_combo = ttk.Combobox(self.bg_img,
                                        font=('yu gothic ui semibold', 12, 'bold'), state="readonly", width=20)
        department_combo.option_add("*TCombobox*Listbox.selectBackground", "#DC143C")
        department_combo.option_add("*TCombobox*Listbox.foreground", "black")
        department_combo["values"] = ([recognised_student_dep])
        department_combo.current(0)
        department_combo.bind("<<ComboboxSelected>>", pick_book)
        department_combo.place(x=480, y=432)

        # Book ComboBox
        course_combo = ttk.Combobox(self.bg_img, textvariable=self.var_course,
                                    font=('yu gothic ui semibold', 12, 'bold'), state="readonly", width=18,
                                    values=["Select Book"])
        course_combo.bind("<<ComboboxSelected>>", pick_author)
        course_combo.current(0)
        course_combo.place(x=480, y=505)

        # Semester ComboBox
        semester_combo = ttk.Combobox(self.bg_img, textvariable=self.var_semester,
                                      font=('yu gothic ui semibold', 12, 'bold'), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6")
        semester_combo.current(0)
        semester_combo.bind("<<ComboboxSelected>>", pick_book)
        semester_combo.place(x=480, y=355)

        # Author ComboBox
        author_combo = ttk.Combobox(self.bg_img, textvariable=self.var_author,
                                    font=('yu gothic ui semibold', 12, 'bold'), state="readonly", width=18,
                                    values=["Select Author"])
        author_combo.current(0)
        author_combo.place(x=480, y=590)

        # Name Entry
        self.name_entry = Entry(self.bg_img, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12, 'bold'))
        self.name_entry.insert(0, recognised_student_name)
        self.name_entry.configure(state='readonly', readonlybackground="white")
        self.name_entry.place(x=480, y=186, width=555, height=38)

        # Roll No. Entry
        self.roll_entry = Entry(self.bg_img, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12, 'bold'))
        self.roll_entry.insert(0, recognised_student_roll)
        self.roll_entry.configure(state='readonly', readonlybackground="white")
        self.roll_entry.place(x=480, y=265, width=555, height=38)

        # ============================Submit Frame====================================
        view_frame = Frame(self.bg_img)
        view_frame.place(x=850, y=600, height=60, width=127)

        # ============================Submit button====================================
        self.view = ImageTk.PhotoImage(file='images/submit1.png')
        self.view_button = Button(view_frame, image=self.view,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white",
                                  command=self.mark_attendance_check_out
                                  , borderwidth=0, background="white", cursor="hand2")
        self.view_button.place(x=0, y=0)

    # --------------------------------------------------pdf---------------------------------------------------------------------------

    def printpdfattendence(self, spacing=1):
        pdf = FPDF()
        pdf.add_page(HORIZONTAL)
        # if self.select == 1:
        printed_data_PDF = [
            ["S No.", "Student_Name", "Rollno", "Department", "Login_time", "Status", "Semester", "Issued_book",
             "Author"
             ]]
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "SELECT `id`,`name`,`roll_no`,`department`,`login_datetime`,`status`,`semester`,`book`,`author` FROM attendence ")
        fetch = my_cursor.fetchall()
        for data in fetch:
            condata = list(data)
            printed_data_PDF.append(condata)
        pdf.set_font("Arial", style="B", size=15)
        pdf.cell(w=110)
        pdf.cell(60, 10, "..!! Attendence Report !!..", border=1, ln=0, align="C")
        pdf.ln(20)
        pdf.set_font("Arial", size=10)
        col_width = pdf.w / 7.9
        row_height = pdf.font_size + 1
        for row in printed_data_PDF:
            for item in row:
                pdf.cell(col_width, row_height * spacing, txt=str(item), border=1)
            pdf.ln(row_height * spacing)
        pdf.set_y(-31)
        pdf.set_font("Arial", style="I", size=8)
        pageNum = "Page no. %s" % pdf.page_no()
        pdf.cell(0, 10, pageNum, align="C")
        pdf.output('Attendence Report .pdf')
        os.startfile(".\Attendence Report .pdf", "open")

    def printxl(self, spacing=1):
        printed_data_XL = []
        row = 0
        column = 0

        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM attendence ")
        headings = ["S No.", "Student_Name", "Rollno", "Department", "Login_time", "Status", "Semester", "Issued_book",
                    "Author"]
        wb = xlsxwriter.Workbook("Attendence Report.xlsx")
        ws = wb.add_worksheet()
        fetch = my_cursor.fetchall()
        for data in fetch:
            condata = list(data)
            printed_data_XL.append(condata)
        for i in headings:
            ws.write(row, column, i)
            column += 1
        row = 1
        column = 0
        my_cursor.execute(
            "SELECT `id`,`name`,`roll_no`,`department`,`login_datetime`,`status`,`semester`,`book`,`author` FROM attendence ")
        for Lid, Lname, Lroll_no, Ldepartment, Llogin_datetime, Lstatus, Lsemester, Lbook, Lauthor in printed_data_XL:
            ws.write(row, column, Lid)
            ws.write(row, column + 1, Lname)
            ws.write(row, column + 2, Lroll_no)
            ws.write(row, column + 3, Lroll_no)
            ws.write(row, column + 4, Ldepartment)
            ws.write(row, column + 5, Llogin_datetime)
            ws.write(row, column + 6, Lstatus)
            ws.write(row, column + 7, Lsemester)
            ws.write(row, column + 8, Lbook)
            ws.write(row, column + 9, Lauthor)
            row += 1
        wb.close()
        os.startfile(".\Attendence Report.xlsx", "open")

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------LIBRARY--------------------------------------------------------------

    def library(self):
        self.bg_img.destroy()
        self.main_frame.destroy()
        # Variables
        self.select = 4
        global select
        select = self.select

        # Variable for radio button
        self.var_radio_btn = StringVar()

        # Background Image
        img3 = Image.open(r"images\framenew.png")
        img3 = img3.resize((1300, 750), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.bg_img_library = Label(self.root, image=self.photoimg3)
        self.bg_img_library.place(x=0, y=0, width=1300, height=750)
        # Backarrow Image
        img = Image.open(r"images\Back-Arrow-Icon-PNG.png")
        img = img.resize((80, 73), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bgarrow_img1 = Button(self.bg_img_library, image=self.photoimg, command=self.mainPage, bg="white",
                              activebackground="white", border=0)
        bgarrow_img1.place(x=25, y=20, width=80, height=73)
        ##################    TITTLE      #################################
        self.txt = "LIBRARY"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.bg_img_library, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=460, y=20, width=450)
        self.slider()
        self.heading_color()

        # ========================left frame==================================

        # LeftLabel Frame
        self.Left_frame = LabelFrame(self.bg_img_library, bd=4, bg="white", relief=RIDGE, text="Library Details",
                                     font=("times new roman", 12, "bold"))
        self.Left_frame.place(x=20, y=100, width=625, height=570)
        # Image On LEFT Frame
        img_right = Image.open(r"images\library.jpg")
        img_right = img_right.resize((608, 170), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.Left_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=608, height=170)

        # Library Information
        class_library_frame = LabelFrame(self.Left_frame, bd=4, bg="white", relief=RIDGE, text="Library Information",
                                         font=("times new roman", 12, "bold"))
        class_library_frame.place(x=5, y=200, width=608, height=300)
        heading = Label(class_library_frame, text="INSERT", font=('yu gothic ui', 20, "bold", "underline"), bg="white",
                        fg='black',
                        bd=5,
                        relief=FLAT)
        heading.place(x=240, y=0, width=150)

        # 1 - Department Label
        department_label = Label(class_library_frame, text="Department", font=('yu gothic ui semibold', 12, 'bold'),
                                 bg="white")
        department_label.place(x=10, y=70)

        # 1 - Department ComboBox
        department_combo = ttk.Combobox(class_library_frame, textvariable=self.var_department_library,
                                        font=('yu gothic ui semibold', 12, 'bold'), state="readonly", width=17)
        department_combo.option_add("*TCombobox*Listbox.selectBackground", "#DC143C")
        department_combo.option_add("*TCombobox*Listbox.foreground", "black")
        department_combo["values"] = (
            "Select Department", "Computer Science", "Electronics", "Civil", "Electrical", "AutoMobile")
        department_combo.current(0)
        department_combo.place(x=120, y=70)

        # # # 3 - Semester Label
        semester_label = Label(class_library_frame, text="Semester", font=('yu gothic ui semibold', 12, 'bold'),
                               bg="white")
        semester_label.place(x=10, y=150)

        # # 3 - Semester ComboBox
        semester_combo = ttk.Combobox(class_library_frame, textvariable=self.var_semester_library,
                                      font=('yu gothic ui semibold', 12, 'bold'), state="readonly", width=17)
        semester_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6")
        semester_combo.current(0)
        semester_combo.place(x=120, y=150)
        # #
        # # # 1 -  book name  Label
        bookname_label = Label(class_library_frame, text="Book Name:", font=('yu gothic ui semibold', 13, 'bold'),
                               bg="white")
        bookname_label.place(x=320, y=70)
        #
        # # # 3 - bookname Entry
        # #
        bookname_entry = Entry(class_library_frame, textvariable=self.var_book_name, width=15, highlightthickness=0,
                               bg="white", relief=FLAT,
                               font=("yu gothic ui semibold", 12))
        bookname_entry.place(x=420, y=70)
        #
        bookname_line = Canvas(class_library_frame, width=140, height=1.3, bg="#393939", highlightthickness=0)
        bookname_line.place(x=420, y=92)
        # # #
        # # # # 2 - AUTHOR Name Label
        book_author_label = Label(class_library_frame, text="Book Author:", font=('yu gothic ui semibold', 13, 'bold'),
                                  bg="white")
        book_author_label.place(x=320, y=150)
        # #
        # # # 2 -AUTHOR Name Entry
        book_author_entry = Entry(class_library_frame, textvariable=self.var_book_author, width=15,
                                  highlightthickness=0, bg="white", relief=FLAT,
                                  font=("yu gothic ui semibold", 12))
        book_author_entry.place(x=430, y=150)
        #
        book_author_line = Canvas(class_library_frame, width=140, height=1.3, bg="#393939", highlightthickness=0)
        book_author_line.place(x=430, y=170)
        # #

        # Buttons Frame for save, update, delete and update
        btn_frame = Frame(class_library_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=1, y=240, width=596, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data1, width=14,
                          font=("times new roman", 13, "bold"),
                          bg="crimson", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data1, width=14,
                            font=("times new roman", 13, "bold"), bg="crimson",
                            fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data1, width=14,
                            font=("times new roman", 13, "bold"), bg="crimson",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data1, width=14,
                           font=("times new roman", 13, "bold"), bg="crimson",
                           fg="white")
        reset_btn.grid(row=0, column=3)

        # -------------------------------------------------Right  FRAME---------------------------------------------------------------------------------

        # Right LabelFrame
        self.Right_frame = LabelFrame(self.bg_img_library, bd=4, bg="white", relief=RIDGE, text="Student Details",
                                      font=("times new roman", 12, "bold"))
        self.Right_frame.place(x=640, y=100, width=625, height=570)

        # Search LabelFrame
        Search_frame = LabelFrame(self.Right_frame, bd=4, bg="white", relief=RIDGE, text="Search System",
                                  font=("times new roman", 12, "bold"))
        Search_frame.place(x=2, y=5, width=612, height=74)

        # Search Label
        Search_label = Label(Search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="white")
        Search_label.grid(row=0, column=0, padx=3, pady=10, sticky=W)

        # Search Combobox
        Search_combo = ttk.Combobox(Search_frame, font=("times new roman", 13, "bold"),textvariable=self.library_search,state="readonly", width=13)
        Search_combo["values"] = ("Select", "author", "book_name","semester","department")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=0, pady=10, sticky=W)

        Search_entry = ttk.Entry(Search_frame, width=15,textvariable=self.library_textsearch,font=("times new roman", 13, "bold"))
        Search_entry.grid(row=0, column=2, padx=6, pady=5, sticky=W)

        # Search Button
        Search_btn = Button(Search_frame, text="Search", width=9,command=self.search_library, font=("times new roman", 13, "bold"), bg="crimson",
                            fg="white")
        Search_btn.grid(row=0, column=3, padx=2)

        # Show All Button
        showAll_btn = Button(Search_frame, text="Show All",command=self.fetch_data1,width=9, font=("times new roman", 13, "bold"), bg="crimson",
                             fg="white")
        showAll_btn.grid(row=0, column=4, padx=10)

        # Table Frame
        table_frame = Frame(self.Right_frame, bd=4, relief=RIDGE, bg="white")
        table_frame.place(x=4, y=90, width=610, height=450)

        # Scrollbar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.book_table = ttk.Treeview(table_frame, column=(
            "id", "sem", "dep", "name",
            "author"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.book_table.xview)
        scroll_y.config(command=self.book_table.yview)

        self.book_table.heading("dep", text="Department")
        self.book_table.heading("sem", text="Semester")
        self.book_table.heading("id", text="BookId")
        self.book_table.heading("name", text="BookName")
        self.book_table.heading("author", text="BookAuthor")
        self.book_table["show"] = "headings"

        self.book_table.pack(fill=BOTH, expand=1)
        self.book_table.bind("<ButtonRelease>", self.get_cursor1)
        self.fetch_data1()

    # ------------------ add data in database ----------------------

    def add_data1(self):
        if self.var_department_library.get() == "Select Department" or self.var_semester_library.get() == "Select Semester" or self.var_book_name.get() == "" or self.var_book_author.get() == "":
            messagebox.showerror("Error", "All Fields Are Required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into book values(%s,%s,%s,%s,%s)", (
                    "",
                    self.var_semester_library.get(),
                    self.var_department_library.get(),
                    self.var_book_name.get(),
                    self.var_book_author.get()
                ))

                conn.commit()
                self.fetch_data1()
                conn.close()
                messagebox.showinfo("Success", "Library Details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # ----------------------------------- fetch data from database into table --------------------------------------
    def fetch_data1(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from book")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.book_table.delete(*self.book_table.get_children())
            for i in data:
                self.book_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    #     --------------------------- get cursor -----------------------------
    def get_cursor1(self, event=""):
        cursor_focus = self.book_table.focus()
        content = self.book_table.item(cursor_focus)
        data = content["values"]

        self.var_Bookid.set(data[0]),
        self.var_semester_library.set(data[1]),
        self.var_department_library.set(data[2]),
        self.var_book_name.set(data[3]),
        self.var_book_author.set(data[4])

    # ------------------------- update function ---------------------------
    def update_data1(self):
        if self.var_department_library.get() == "Select Department" or self.var_semester_library.get() == "Select Semester" or self.var_book_name.get() == "" or self.var_book_author.get() == "":
            messagebox.showerror("Error", "All Fields Are Required!", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do You Want To Update This Student Details!", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update book set semester=%s,department=%s,book_name=%s, author=%s where id=%s",
                        (
                            self.var_semester_library.get(),
                            self.var_department_library.get(),
                            self.var_book_name.get(),
                            self.var_book_author.get(),
                            self.var_Bookid.get()
                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Library Details Updated Successfully!", parent=self.root)
                conn.commit()
                self.fetch_data1()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ------------------------------- Delete Data ------------------------------------------------------------------

    def delete_data1(self):
        if self.var_student_id == "":
            messagebox.showerror("Error", "Book Id is Required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Success", "Do You Want To Delete This Data!", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("delete from book where id=%s", (self.var_Bookid.get(),))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data1()
                conn.close()
                messagebox.showinfo("Success", "Library Details Deleted Successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    #     --------------------------------------- Reset Data ----------------------------------------------
    def reset_data1(self):
        self.var_department_library.set("Select Department"),
        self.var_semester_library.set("Select Semester"),
        self.var_book_name.set(""),
        self.var_book_author.set("")

    def search_library(self):
        print("hlo", self.search.get(), self.text_search.get())
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from book where " + str(self.library_search.get()) + " LIKE '%" + str(
            self.library_textsearch.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.book_table.delete(*self.book_table.get_children())
            for i in rows:
                self.book_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    # def search(self):

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------TRAIN DATA-----------------------------------------------------------------

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # ------------------------- Train the classifier and save------------------------
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset is Completed!")

    def view_attendence(self):
        if self.select == 0:
            self.bg_img.destroy()
            self.main_frame.destroy()
        elif self.select == 3:
            self.bg_img_attendence.destroy()
            self.main_frame_attendence.destroy()
        self.select = 5
        global select
        select = self.select
        # Background Image
        img3 = Image.open(r"images\frame.png")
        img3 = img3.resize((1300, 737), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.bg_img_view = Label(self.root, image=self.photoimg3)
        self.bg_img_view.place(x=0, y=0, width=1300, height=737)

        # Main Frame
        self.main_frame_view = Frame(self.root, bd=2, background="white")
        self.main_frame_view.place(x=40, y=37, width=1219, height=660)

        # =================================== Time =========================================
        self.clock_image = ImageTk.PhotoImage(file="images/time.png")
        self.date_time_image = Label(self.main_frame_view, image=self.clock_image, bg="white", activebackground="white")
        self.date_time_image.place(x=0, y=7)

        self.date_time = Label(self.root)
        self.date_time.place(x=75, y=40)
        self.time_running()

        # ========================== Heading =====================================
        self.txt = "Attendance Report"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.main_frame_view, text=self.txt, font=('yu gothic ui', 20, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=250, y=2, width=650)
        self.slider()
        self.heading_color()

        # ============================Current user================================
        self.current_user_image = ImageTk.PhotoImage(file="images/current_user.png")
        self.current_user_label = Label(self.main_frame_view, image=self.current_user_image, bg="white")
        self.current_user_label.place(x=920, y=3, width=50, height=40)
        self.current_user = Label(self.main_frame_view, bg="white", text=self.username.get(),
                                  font=("yu gothic ui", 10, "bold"), fg="#DC143C")
        self.current_user.place(x=970, y=5)

        # self.current_user = Label(  self.main_frame_view, bg="white",
        #                           font=("yu gothic ui", 10, "bold"), fg="green")
        # self.current_user.place(x=1000, y=48)


        # ============================ Line ================================
        line = Image.open(r"images\line.png")
        line = line.resize((1220, 10), Image.ANTIALIAS)
        self.line = ImageTk.PhotoImage(line)

        bg_img = Label(self.main_frame_view, image=self.line, bg="white")
        bg_img.place(x=0, y=50, width=1220, height=10)

        # ============================Home Frame====================================
        home_frame = Frame(self.main_frame_view)
        home_frame.place(x=0, y=170, height=117, width=115)

        # ============================Home button====================================
        self.home = ImageTk.PhotoImage(file='images/home.png')
        self.home_button = Button(home_frame, image=self.home, command=self.mainPage,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.home_button.place(x=0, y=0)

        # ============================ Exit Frame====================================
        exit_frame = Frame(self.main_frame_view)
        exit_frame.place(x=0, y=400, height=120, width=125)

        # ============================ Exit button====================================
        self.exit = ImageTk.PhotoImage(file='images/exit.png')
        self.exit_button = Button(exit_frame, image=self.exit, command=self.Exit,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")

        self.exit_button.place(x=0, y=0)

        # Table Frame
        table_frame = Frame(self.root, relief=RIDGE, bg="white")
        table_frame.place(x=164, y=167, width=1097, height=460)

        # Scrollbar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Add some style
        style = ttk.Style()

        # Pick a theme
        style.theme_use("clam")

        # Configure our treeview colors
        style.configure("Treeview", background="white", rowheight=25, fieldbackground="white",
                        font=("times new roman", 10, "bold"))

        # Change selected color
        style.map("Treeview", background=[("selected", "#DC143C")])

        self.attendance_table = ttk.Treeview(table_frame, column=(
            "id", "name", "roll_no", "department", "login_datetime", "status", "semester", "book", "author"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # Text in center
        self.attendance_table.column("id", anchor=CENTER)
        self.attendance_table.column("name", anchor=CENTER)
        self.attendance_table.column("roll_no", anchor=CENTER)
        self.attendance_table.column("department", anchor=CENTER)
        self.attendance_table.column("semester", anchor=CENTER)
        self.attendance_table.column("book", anchor=CENTER)
        self.attendance_table.column("author", anchor=CENTER)
        self.attendance_table.column("login_datetime", anchor=CENTER)
        self.attendance_table.column("status", anchor=CENTER)

        self.attendance_table.tag_configure("oddrow", background="white")
        self.attendance_table.tag_configure("evenrow", background="#f1ad98")

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("id", text="Id")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("roll_no", text="Roll No")
        self.attendance_table.heading("department", text="Department")
        self.attendance_table.heading("login_datetime", text="Login Time")
        self.attendance_table.heading("status", text="Status")
        self.attendance_table.heading("semester", text="Semester")
        self.attendance_table.heading("book", text="Book")
        self.attendance_table.heading("author", text="Author")
        self.attendance_table["show"] = "headings"

        self.attendance_table.pack(fill=BOTH, expand=1)
        self.fetch_data2()

        # ============================PDF Frame====================================
        pdf_frame = Frame(self.main_frame_view)
        pdf_frame.place(x=460, y=590, height=55, width=126)

        # ============================PDF button====================================
        self.pdf = ImageTk.PhotoImage(file='images/pdf.png')
        self.pdf_button = Button(pdf_frame, image=self.pdf, command=self.printpdfattendence,
                                 font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                 , borderwidth=0, background="white", cursor="hand2")
        self.pdf_button.place(x=0, y=0)

        # ============================Excel Frame====================================
        excel_frame = Frame(self.main_frame_view)
        excel_frame.place(x=700, y=590, height=55, width=126)

        # ============================Excel button====================================
        self.excel = ImageTk.PhotoImage(file='images/excel.png')
        self.excel_button = Button(excel_frame, image=self.excel, command=self.printxl,
                                   font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                   , borderwidth=0, background="white", cursor="hand2")
        self.excel_button.place(x=0, y=0)

        # Search Label

        Search_label = Label(self.main_frame_view, text="Search By:", font=("yu gothic ui", 15, "bold"), bg="white")
        Search_label.place(x=430, y=79, width=199, height=24)

        # Search Combobox
        search_combo = ttk.Combobox(self.main_frame_view,
                                    font=('yu gothic ui semibold', 13, 'bold'), textvariable=self.search,
                                    state="readonly", width=20)
        search_combo.option_add("*TCombobox*Listbox.selectBackground", "#DC143C")
        search_combo.option_add("*TCombobox*Listbox.foreground", "black")
        search_combo["values"] = ("Select", "roll_no", "name")
        search_combo.current(0)
        search_combo.place(x=590, y=77, width=150, height=30)

        Search_entry = ttk.Entry(self.main_frame_view, width=15, textvariable=self.text_search,
                                 font=("yu gothic ui", 13, "bold"))
        Search_entry.place(x=770, y=77, width=150, height=30)

        # Search Button
        Search_btn = Button(self.main_frame_view, text="Search", width=9, command=self.search2,
                            font=("yu gothic ui", 13, "bold"), bg="#DC143C",
                            fg="white")
        Search_btn.place(x=950, y=70, width=110, height=40)

        # Show All Button
        showAll_btn = Button(self.main_frame_view, text="Show All", width=9, command=self.fetch_data2,
                             font=("yu gothic ui", 13, "bold"), bg="#DC143C",
                             fg="white")
        showAll_btn.place(x=1080, y=70, width=110, height=40)

    # ----------------------------------- fetch data from database into table --------------------------------------
    def fetch_data2(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from attendence")
        data = my_cursor.fetchall()
        count = 0
        if len(data) != 0:
            self.attendance_table.delete(*self.attendance_table.get_children())
            for i in data:
                if count % 2 == 0:
                    self.attendance_table.insert("", END, values=i, tags="evenrow")
                else:
                    self.attendance_table.insert("", END, values=i, tags="oddrow")
                count += 1
            conn.commit()
        conn.close()

    def search2(self):
        print("hlo", self.search.get(), self.text_search.get())
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from attendence where " + str(self.search.get()) + " LIKE '%" + str(
            self.text_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.attendance_table.delete(*self.attendance_table.get_children())
            for i in rows:
                self.attendance_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def help_desk_f(self):
        self.bg_img.destroy()
        self.main_frame.destroy()
        self.select = 10
        global select
        select = self.select

        # Background Image
        img3 = Image.open(r"images\help_desk_info.png")
        img3 = img3.resize((1300, 737), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.bg_img_help = Label(self.root, image=self.photoimg3)
        self.bg_img_help.place(x=0, y=0, width=1300, height=737)
        # Backarrow Image
        img = Image.open(r"images\Back-Arrow-Icon-PNG.png")
        img = img.resize((80, 73), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        bgarrow_img1 = Button(self.bg_img_help, image=self.photoimg, command=self.mainPage, bg="white",
                              activebackground="white", border=0)
        bgarrow_img1.place(x=35, y=35, width=50, height=43)

    def Exit(self):
        result = tkMessageBox.askquestion('Face Recoginition Attendence System', 'Are you sure you want to exit?',
                                          icon="warning")
        if result == 'yes':
            root.destroy()
            exit()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    obj.login()
    root.mainloop()
