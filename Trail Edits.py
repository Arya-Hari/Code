from tkinter import * 
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import pickle
import io
import mysql.connector
from tkinter import scrolledtext
from tkinter import ttk

def services():
    def viewspecial():
        SPage = Toplevel(MPage)
        SPage.geometry('1000x1000')

        main_frame=Frame(SPage)
        main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
        second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")

        global image5
        background4=Canvas(second_frame,width=6000,height=6000)
        image5=ImageTk.PhotoImage(Image.open("istockphoto-1154943426-612x612.jpg"))
        background4.create_image(0,0,anchor='nw',image=image5)
        background4.pack(expand=True,fill=BOTH)

        WELCOME = Label(second_frame,text='''WELCOME TO SPECIAL APPOINTMENTS PAGE
Here, choose amongst the best doctors who'll tackle any problem! You can count on 
them to heal you from the roots. Counter any problem in the best way possible
What are you waiting for? GO EXPLORE! ''',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        WELCOME.place(x=150,y=7)

        VIJAY_GANESHA=Label(second_frame,text=''' DR. VIJAY GANESHAN - INSTITUTION OF MENTAL HEALTH
 QUALIFICATIONS - B.A in Psychology, M.A in Counselling Psychology and Social Psychology,
 PhD in Counselling Psychology

  SPECIALISATION - ANXIETY
 
 Dr Vijay Ganesha has over 40 years of experience in helping patients deal with anxiety-related issues. He also authored the best-selling book named
 "Declutter Your Mind". He frequently conducts workshops in both India and abroad on anxiety and how to deal with it.''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        VIJAY_GANESHA.place(x=15,y=150)
        VG_BOOK=Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        VG_BOOK.place(x=700,y=170)    

        RADHIKA_RAMANATHAN=Label(second_frame,text='''RADHIKA RAMANATHAN - CAREFORYOU
  QUALIFICATIONS - B.A. in Psychology, M.A in Developmental Psychology and Social Psychology,
  PhD in Social Psychology

  SPECIALISATION - DEPRESSION

  Dr. Radhika Ramanathan is not a new name in the books. She is the host of the popular TV show "The Happy Lab", where she helps people overcome
  depression by showing the power of happiness. She has helped over 2500 people both on and off the show. ''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid' )
        RADHIKA_RAMANATHAN.place(x=15,y=360)
        RR_BOOK=Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        RR_BOOK.place(x=700,y=380)

    
        

    def viewgeneral():
        GDPage=Toplevel(MPage)
        GDPage.geometry('1000x1000')
        

        main_frame=Frame(GDPage)
        main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
        second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")

        global image4
        background3=Canvas(second_frame,width=6000,height=6000)
        image4=ImageTk.PhotoImage(Image.open("istockphoto-1154943426-612x612.jpg"))
        background3.create_image(0,0,anchor='nw',image=image4)
        background3.pack(expand=True,fill=BOTH)
        WELCOME = Label(second_frame,text='''WELCOME TO GENERAL APPOINTMENTS PAGE
Here, choose amongst the best doctors who'll listen to anything and everything you
have to say! Counter any problem and heal in the best way possible
What are you waiting for? GO EXPLORE! ''',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        WELCOME.place(x=150,y=7)
    

        JOHN_VARGHESE = Label(second_frame,text=''' JOHN VARGHESE - OAK GROVE THERAPY CENTRE
 QUALIFICATIONS - B.A in Psychology,M.A in Councelling Psychology

 John Varghese has over 22 years of experience dealing with patients struggling with problems over various fields of Psychology such as Anxiety,
 Depression, Post-Trauma and Addiction. He is currently pursuing his career in Oak Grove Therapy Centre and is also associated with top notch
 hospitals in India such as NIMHANS and KIMS. In the course of his career, John Varghese has aided over 90000 patients to tackle all their difficulties
 and strengthen themselves both mentally as well as physically.''',justify=LEFT,font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        JOHN_VARGHESE.place(x=15,y=150)
        JV_BOOK = Button (second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        JV_BOOK.place(x=700,y=170)

        USHA_MANDA=Label(second_frame,text = ''' DR. USHA MANDA - THERAPISTIC
 QUALIFICATIONS - B.A in Psychology, M.A in Organizational Psychology and in Councelling Psychology, 
 Ph.D in Councelling Psychology 

 Dr. Usha Manda has over 30 years of experience in the field of general Psychology. She is presently waged Therapistic() but is affiliated with several
 reputed health care centers in India such as NIMHANS, Apollo and Fortis. Dr. Usha Manda has helped more than 120000 people overcome obstacles
 related to mental health, stress, well-being and has also provided councelling to over 30000 patients.''',justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        USHA_MANDA.place(x=15,y=330)
        UM_BOOK = Button (second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        UM_BOOK.place(x=700,y=350)



    CPage=Toplevel(MPage)
    CPage.geometry('1000x600')

    global image3
    background2=Canvas(CPage,width=6000,height=600)
    image3=ImageTk.PhotoImage(Image.open("istockphoto-1154943426-612x612.jpg"))
    background2.create_image(0,0,anchor='nw',image=image3)
    background2.pack(expand=True,fill=BOTH)


    WELCOME = Label(CPage,text='''WELCOME TO MINDCOLOGY
Recovery is an Evolution, Not a Miracle - That's Our Motto
At Mindcology, we want to help you in your evolutionary journey to a better self...
We want you to be in your best space and provide you with a range of options to choose from!!
GO AHEAD AND TAKE THAT FIRST STEP!!!''',font=('Bahnschrift Condensed',18),bg='white',fg='black')
    WELCOME.place(x=120,y=7)

    FORMAL=Label(CPage,text='''Having issues you want to get
a professional opinion upon? Just want a general talk or
a specialized recovery? We've got you covered. Just click 
the button down below to take you to your place of choice!!''',font=('Bahnschrift Condensed',18),bg='white',fg='black')
    FORMAL.place(x=10,y=170)

    GENERAL=Button(CPage,text='I JUST NEED A GENERAL TALK',font=('Bahnschrift Condensed',14),fg='black',bg='white',command=viewgeneral)
    GENERAL.place(x=40,y=320)

    SPECIALIST=Button(CPage,text='I NEED A SPECIALIST',font=('Bahnschrift Condensed',14),fg='black',bg='white',command=viewspecial)
    SPECIALIST.place(x=250,y=320)

    INFORMAL=Label(CPage,text='''Feel a need to connect with others
just like you? We can help you with that too. Find 
information  on workshops and discussions right here. Click
the button below and find out when and where exactly!!!''',font=('Bahnschrift Condensed',18),bg='white',fg='black')
    INFORMAL.place(x=500,y=170)

    WORKSHOPS=Button(CPage,text='SHOW ME THE WORKSHOPS',font=('Bahnschrift Condensed',14),bg='white',fg='black')
    WORKSHOPS.place(x=650,y=320)


    
def loginclicked():
    def clicked_l():
        usid_l=0
        psid_l=0
        connection = mysql.connector.connect(
                                         database='mindcology',
                                         user='root',
                                         password='12ammu34')

        sql_selectQuery = "select * from REGISTRATION"
        cursor = connection.cursor()
        cursor.execute(sql_selectQuery)
        records = cursor.fetchall()
        logu=0
        logp=0
        for row in records:
            if row[3] == USERNAME1_entry.get():
                logu+=1
                if row[4]==PASSWORD1_entry.get():
                    SLogin = Label(LPage,text='LOGIN  SUCCESSFUL!!!',font=('Bahnschrift Condensed',20),bg='white',fg='blue')
                    SLogin.place(x=200,y=250)
                    Click = Button(LPage,text='Click to Continue',font=('Bahnschrift Condensed',20),bg='white',fg='blue',command=services)
                    Click.place(x=215,y=300)
            if row[4]==PASSWORD1_entry.get():
                logp+=1
        if logu==0:
            messagebox.showinfo('Error','Username Incorrect')
        if logp==0:
            messagebox.showinfo('Error','Password Incorrect')
    
    
    global image1
    LPage=Toplevel(MPage)
    background1=Canvas(LPage,width=600,height=517)
    image1=ImageTk.PhotoImage(Image.open("lib.jpg"))
    background1.create_image(0,0,anchor='nw',image=image1)
    background1.pack(expand=True,fill=BOTH)
    LPage.geometry('600x400')
    
    Login_Form=Label(LPage,text='LOGIN  TO CONTINUE',font=('Bahnschrift Condensed',18),bg='white',fg='black')
    Login_Form.place(x=220, y=50)
    
    USERNAME1=Label(LPage,text='Username',font=('Bahnschrift Condensed',15),bg='white',fg='black')
    USERNAME1.place(x=175, y=100)
    USERNAME1_entry=Entry(LPage)
    USERNAME1_entry.place(x=265, y=105)
    USERNAME1_entry.bind('<Return>',clicked_l)
    
    PASSWORD1=Label(LPage,text='Password',font=('Bahnschrift Condensed',15),bg='white',fg='black')
    PASSWORD1.place(x=175, y=150)
    PASSWORD1_entry=Entry(LPage)
    PASSWORD1_entry.place(x=265,y=155)
    PASSWORD1_entry.bind('<Return>',clicked_l)

    SUBMITL=Button(LPage,text='SUBMIT',font=('Bahnschrift Condensed',15),bg='white',fg='black',command=clicked_l)
    SUBMITL.place(x=265, y=200)



def registerclicked():
    def clicked():
        usid=0
        psid=0
        connection = mysql.connector.connect(
                                         database='mindcology',
                                         user='root',
                                         password='12ammu34')

        sql_select_Query = "select * from REGISTRATION"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            if row[3] == USERNAME_entry.get():
                messagebox.showinfo('Error','Username Already in Use')
                usid+=1
            if row[4]==PASSWORD_entry.get():
                messagebox.showinfo('Error','Password Already in Use')
                psid+=1
        if usid==0:
            if psid==0:
                entry1= FNAME_entry.get()
                entry2=LNAME_entry.get()
                entry3=EMAIL_entry.get()
                entry4=USERNAME_entry.get()
                entry5=PASSWORD_entry.get()
                conn=mysql.connector.connect(user='root', password='12ammu34',database='mindcology')
                mycursor=conn.cursor()
                sql=('''INSERT INTO REGISTRATION (FIRST_NAME,LAST_NAME,EMAIL,USERNAME,PASSWORD)
            VALUES(%s,%s,%s,%s,%s)''')
                val = (entry1,entry2,entry3,entry4,entry5)
                mycursor.execute(sql,val)
                conn.commit()
                FNAME.destroy()
                FNAME_entry.destroy()
                LNAME.destroy()
                LNAME_entry.destroy()
                EMAIL.destroy()
                EMAIL_entry.destroy()
                USERNAME.destroy()
                USERNAME_entry.destroy()
                PASSWORD.destroy()
                PASSWORD_entry.destroy()
                SUBMITR.destroy()
                Registration_Form.destroy()
                SLogin1= Label(RPage,text='REGISTRATION SUCCESSFUL!!!',font=('Bahnschrift Condensed',20),bg='white',fg='blue')
                SLogin1.place(x=170,y=100)
                Click1 = Button(RPage,text='Click to Continue',font=('Bahnschrift Condensed',20),bg='white',fg='blue',command=services)
                Click1.place(x=215,y=150)
                
    global image1
    RPage=Toplevel(MPage)
    background1=Canvas(RPage,width=600,height=517)
    image1=ImageTk.PhotoImage(Image.open("lib.jpg"))
    background1.create_image(0,0,anchor='nw',image=image1)
    background1.pack(expand=True,fill=BOTH)
    RPage.geometry('600x517')

    Registration_Form=Label(RPage,text='REGISTRATION FORM',font=('Bahnschrift Condensed',18),bg='white',fg='black')
    Registration_Form.place(x=215, y=50)

    FNAME=Label(RPage,text='First Name',font=('Bahnschrift Condensed',15),bg='white',fg='black')
    FNAME.place(x=175, y=100)
    FNAME_entry=Entry(RPage)
    FNAME_entry.place(x=265,y=105)
    FNAME_entry.bind('<Return>',clicked)

    
    LNAME=Label(RPage,text='Last Name',font=('Bahnschrift Condensed',15),bg='white',fg='black')
    LNAME.place(x=175,y=150)
    LNAME_entry=Entry(RPage)
    LNAME_entry.place(x=265,y=155)
    LNAME_entry.bind('<Return>',clicked)
    
    EMAIL=Label(RPage,text='Email ID',font=('Bahnschrift Condensed',15),bg='white',fg='black')
    EMAIL.place(x=180, y=200)
    EMAIL_entry=Entry(RPage)
    EMAIL_entry.place(x=265,y=205)
    EMAIL_entry.bind('<Return>',clicked)
    
    USERNAME=Label(RPage,text='Username',font=('Bahnschrift Condensed',15),bg='white',fg='black')
    USERNAME.place(x=175, y=250)
    USERNAME_entry=Entry(RPage)
    USERNAME_entry.place(x=265, y=255)
    USERNAME_entry.bind('<Return>',clicked)
    
    PASSWORD=Label(RPage,text='Password',font=('Bahnschrift Condensed',15),bg='white',fg='black')
    PASSWORD.place(x=175, y=300)
    PASSWORD_entry=Entry(RPage)
    PASSWORD_entry.place(x=265,y=305)
    PASSWORD_entry.bind('<Return>',clicked)


    SUBMITR=Button(RPage,text='SUBMIT',font=('Bahnschrift Condensed',15),bg='white',fg='black',command=clicked)
    SUBMITR.place(x=265, y=350)

MPage=tk.Tk()

background=Canvas(MPage,width=600,height=517)
image=ImageTk.PhotoImage(Image.open("lib.jpg"))
image3=ImageTk.PhotoImage(Image.open("istockphoto-1154943426-612x612.jpg"))
background.create_image(0,0,anchor='nw',image=image)
background.pack(expand=True,fill=BOTH)

MPage.title('Mindcology')
MPage.geometry('600x517')

intro=Label(MPage, text='''MINDCOLOGY
Recovery is an Evolution, Not a Miracle''', font=('Bahnschrift Condensed',20),bg='white',fg='black')
intro.place(x=135,y=100)

Q1=Label(MPage, text = 'Login or register now to continue',font=('Bahnschrift Condensed',15),bg='white',fg='black')
Q1.place(x=195, y=260)

login=Button(MPage, text='Login', font=('Bahnschrift Condensed',15),bg='white',fg='black',command=loginclicked)
login.place(x=230,y=300)
register=Button(MPage, text='Register Now!', font=('Bahnschrift Condensed',15),bg='white',fg='black',command=registerclicked)
register.place(x=280,y=300)
    
motto=Label(MPage, text='''Anxiety | Depression | Post-Trauma | Addiction
RECOVERY IS AN EVOLUTION, NOT A MIRACLE''', font=('Bahnschrift Condensed', 15),bg='white', fg='black')
motto.place(x=150,y=400)


MPage.mainloop()
