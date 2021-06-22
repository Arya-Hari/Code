
from tkinter import * 
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import Separator, Style


def specialcalc():
        SCPage= Toplevel(MPage)
        SCPage.geometry('1015x1000')
        main_frame=Frame(SCPage)
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

        global image7
        background6=Canvas(second_frame,width=1100,height=1500)
        image7=ImageTk.PhotoImage(Image.open("220d4aa99d158cfff3ad66bdd1f3357b.jpg"))
        background6.create_image(0,0,anchor='nw',image=image7)
        background6.pack(expand=True,fill=BOTH)

        n=StringVar()
        h=StringVar()
        h.set("1 hour")
        g=StringVar()
        a=StringVar()
        o=StringVar()
        message = Label(second_frame, text="""Almost Done!
Confirm Your Appointment Before Proceeding""", font=("Bahnschrift Condensed",20),fg="black",bg="white")
        message.place(x=320,y=15)

        FIRST_NAME = Label(second_frame, text="Enter First Name:", font=("Bahnschrift Condensed",18),bg="white")
        FIRST_NAME.place(x=45,y=140)
        FIRST_NAME_ENTRY = Entry(second_frame, width=30)
        FIRST_NAME_ENTRY.place(x=245,y=150)
        LAST_NAME = Label(second_frame, text="Enter Last Name:", font=("Bahnschrift Condensed",18),bg="white")
        LAST_NAME.place(x=45,y=190)
        LAST_NAME_ENTRY = Entry(second_frame, width=30)
        LAST_NAME_ENTRY.place(x=245,y=200)

        PHONE_NUMBER_1=Label(second_frame, text="Enter Phone Number 1:", font=("Bahnschrift Condensed",18),bg="white")
        PHONE_NUMBER_1.place(x=45,y=240)
        PHONE_NUMBER_1_ENTRY=Entry(second_frame, width=30)
        PHONE_NUMBER_1_ENTRY.place(x=245,y=250)
        PHONE_NUMBER_2 = Label(second_frame, text="Enter Phone Number 2:", font=("Bahnschrift Condensed",18),bg="white")
        PHONE_NUMBER_2.place(x=45,y=290)
        PHONE_NUMBER_2_ENTRY = Entry(second_frame, width=30)
        PHONE_NUMBER_2_ENTRY.place(x=245,y=300)

        EMAIL=Label(second_frame, text="Enter E-Mail Address:", font=("Bahnschrift Condensed",18),bg="white")
        EMAIL.place(x=45,y=340)
        EMAIL_ENTRY = Entry(second_frame, width=30)
        EMAIL_ENTRY.place(x=245,y=350)

        GENDER = Label(second_frame, text="Select Gender", font=("Bahnschrift Condensed",18),bg="white")
        GENDER.place(x=45,y=405)
        MALE = Radiobutton(second_frame, text="Male",font=("Bahnschrift Condensed",14), variable=g, value=1,tristatevalue=0,bg="white")
        MALE.place(x=45,y=445)
        FEMALE = Radiobutton(second_frame, text="Female",font=("Bahnschrift Condensed",14), variable=g, value=2,tristatevalue=0,bg="white")
        FEMALE.place(x=150,y=445)
        
        AGE = Label(second_frame, text="Select Age Group", font=("Bahnschrift Condensed", 18),bg="white")
        AGE.place(x=45,y=505)
        AGE1 = Radiobutton(second_frame, text="10-16", font=("Bahnschrift Condensed",14) ,bg="white",variable=a,value=1,tristatevalue=0)
        AGE1.place(x=45,y=555)
        AGE2 = Radiobutton(second_frame, text="18-25", font=("Bahnschrift Condensed",14),bg="white", variable=a,value=2,tristatevalue=0)
        AGE2.place(x=145,y=555)
        AGE3 = Radiobutton(second_frame, text="26-34", font=("Bahnschrift Condensed",14),bg="white", variable=a,value=3,tristatevalue=0)
        AGE3.place(x=245,y=555)
        AGE4 = Radiobutton(second_frame, text="35-44", font=("Bahnschrift Condensed",14),bg="white", variable=a,value=4,tristatevalue=0)
        AGE4.place(x=345,y=555)
        AGE5 = Radiobutton(second_frame, text="45+", font=("Bahnschrift Condensed",14),bg="white", variable=a,value=5,tristatevalue=0)
        AGE5.place(x=445,y=555)

        DAYS = Label(second_frame, text="Select Preferred Days of the Week", font=("Bahnschrift Condensed",18),bg="white")
        DAYS.place(x=620,y=555)
        MON = Checkbutton(second_frame, text="Monday",font=("Bahnschrift Condensed",14),bg="white")
        MON.place(x=580,y=595)
        TUES = Checkbutton(second_frame, text="Tuesday",font=("Bahnschrift Condensed",14),bg="white")
        TUES.place(x=665,y=595)
        WED = Checkbutton(second_frame, text="Wednesday",font=("Bahnschrift Condensed",14),bg="white")
        WED.place(x=755,y=595)
        THURS = Checkbutton(second_frame, text="Thursday",font=("Bahnschrift Condensed",14),bg="white")
        THURS.place(x=865,y=595)
        FRI = Checkbutton(second_frame, text="Friday",font=("Bahnschrift Condensed",14),bg="white")
        FRI.place(x=620,y=640)
        SAT = Checkbutton(second_frame, text="Saturday",font=("Bahnschrift Condensed",14),bg="white")
        SAT.place(x=710,y=640)
        SUN = Checkbutton(second_frame, text="Sunday",font=("Bahnschrift Condensed",14),bg="white")
        SUN.place(x=810,y=640)
        
        NUMBER_OF_HOURS=Label(second_frame, text="Select Number of Hours per Day", font=("Bahnschrift Condensed",18),bg="white")
        NUMBER_OF_HOURS.place(x=45,y=605)
        HOURS = OptionMenu(second_frame, h, "30 mins","1 hour", "1 hr 30 mins", "2 hours")
        HOURS.place(x=85,y=645)
        
        DOCTORS = Label(second_frame, text="Confirm Your Doctor", font=("Bahnschrift Condensed",18),bg="white")
        DOCTORS.place(x=620,y=140)
        AB = Radiobutton(second_frame, text="Dr. Ananya Bahri (Depression Therapist)",font=("Bahnschrift Condensed",14),bg="white", variable=n, value=1,tristatevalue=0)
        AB.place(x=620,y=180)
        DM = Radiobutton(second_frame, text="Dr. Diya More (Anxiety Therapist)",font=("Bahnschrift Condensed",14),bg="white", variable=n, value=2,tristatevalue=0)
        DM.place(x=620,y=225)
        TM = Radiobutton(second_frame, text="Dr. Tarun Matthew (Post Trauma Therapist)",font=("Bahnschrift Condensed",14),bg="white", variable=n, value=3,tristatevalue=0)
        TM.place(x=620,y=265)
        KL = Radiobutton(second_frame, text="Dr. Karim Lok (Addiction Therapist)",font=("Bahnschrift Condensed",14),bg="white", variable=n, value=4,tristatevalue=0)
        KL.place(x=620,y=305)
        RR = Radiobutton(second_frame, text="Dr. Radhika Ramanathan (Depression Therapist)",font=("Bahnschrift Condensed",14),bg="white", variable=n, value=5,tristatevalue=0)
        RR.place(x=620,y=345)
        KL = Radiobutton(second_frame, text="Dr. Vijay Ganesha (Anxiety Therapist)",font=("Bahnschrift Condensed",14),bg="white", variable=n, value=6,tristatevalue=0)
        KL.place(x=620,y=385)

        OPTION = Label(second_frame, text="Select Online or Offline", font=("Bahnschrift Condensed",18),bg="white")
        OPTION.place(x=620,y=435)
        ON = Radiobutton(second_frame, text="Online", font=("Bahnschrift Condensed",14),bg="white",variable=o,value=1,tristatevalue=0)
        ON.place(x=620,y=475)
        OFF = Radiobutton(second_frame, text="Offline", font=("Bahnschrift Condensed",14),bg="white",variable=o,value=2,tristatevalue=0)
        OFF.place(x=740,y=475)
        
        CONFIRM = Button(second_frame , text="Confirm Appointment", font=("Bahnschrift Condensed",16),bg="white")
        CONFIRM.place(x=450,y=745)

def generalcalc():
        GCPage=Toplevel(MPage)
        GCPage.geometry('1000x1500')
        main_frame=Frame(GCPage)
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

        global image7
        background6=Canvas(second_frame,width=1100,height=1500)
        image7=ImageTk.PhotoImage(Image.open("220d4aa99d158cfff3ad66bdd1f3357b.jpg"))
        background6.create_image(0,0,anchor='nw',image=image7)
        background6.pack(expand=True,fill=BOTH)

        intro=Label(second_frame, text='''- CONFIRMATION PAGE -''', font=('Bahnschrift Condensed',24),bg='white',fg='black')
        intro.place(x=380,y=10)
        details=Label(second_frame, text='''Please confirm your details before proceeding to the next step!''',font=('Bahnschrift Condensed',15),bg='white',fg='black')
        details.place(x=305,y=60)
        details=Label(second_frame, text='''ENTER DETAILS''', font=('Bahnschrift Condensed',18),bg='white',fg='black')
        details.place(x=160,y=109)
        fname=Label(second_frame,text='First Name',font=('Bahnschrift Condensed',16),bg='white',fg='black')
        fname.place(x=50, y=160)
        fname_entry=Entry(second_frame)
        fname_entry.place(x=160,y=160,width=250)
        fname.bind()
        lname=Label(second_frame,text='Last Name',font=('Bahnschrift Condensed',16),bg='white',fg='black')
        lname.place(x=50, y=200)
        lname_entry=Entry(second_frame)
        lname_entry.place(x=160,y=200,width=250)
        email=Label(second_frame,text='Email ID ',font=('Bahnschrift Condensed',16),bg='white',fg='black')
        email.place(x=50, y=240)
        email_entry=Entry(second_frame)
        email_entry.place(x=160,y=240,width=250)
        number1=Label(second_frame,text='Phone No.1',font=('Bahnschrift Condensed',16),bg='white',fg='black')
        number1.place(x=50, y=280)
        number1_entry=Entry(second_frame)
        number1_entry.place(x=160,y=280,width=250)
        number2=Label(second_frame,text='Phone No.2',font=('Bahnschrift Condensed',16),bg='white',fg='black')
        number2.place(x=50, y=320)
        number2_entry=Entry(second_frame)
        number2_entry.place(x=160,y=320,width=250)
        gender=Label(second_frame,text='GENDER',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        gender.place(x=95,y=360)
        a = IntVar()
        choose_gender=Radiobutton(second_frame,text='Male',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=a,value=1,tristatevalue=0)
        choose_gender.place(x=55,y=405)
        choose_gender=Radiobutton(second_frame,text='Female',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=a,value=2,tristatevalue=0)
        choose_gender.place(x=130,y=405)
        choose_gender=Radiobutton(second_frame,text='Others',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=a,value=3,tristatevalue=0)
        choose_gender.place(x=85,y=450)
        age=Label(second_frame,text='AGE',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        age.place(x=275,y=360)
        options=[
        "8 to 12",
        "13 to 19",
        "20 to 40",
        "40 and above"]
        clicked=StringVar()
        clicked.set(options[0])
        drop=OptionMenu(second_frame,clicked,*options)
        drop.place(x=250,y=405)
        hours=Label(second_frame,text='DURATION',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        hours.place(x=55,y=500)
        options=[
        "30 min",
        "1 hour",
        "1.5 hour",
        "2 hours"]
        clicked=StringVar()
        clicked.set(options[0])
        drop=OptionMenu(second_frame,clicked,*options)
        drop.place(x=140,y=503)
        mode=Label(second_frame,text='CHOOSE YOUR MODE',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        mode.place(x=250,y=465)
        b = IntVar()
        choose_mode=Radiobutton(second_frame,text='Offline mode',font=('Bahnschrift Condensed',15),bg='white',fg='black',variable=b,value=1,tristatevalue=0)
        choose_mode.place(x=265,y=505)
        choose_gender=Radiobutton(second_frame,text='Online mode',font=('Bahnschrift Condensed',15),bg='white',fg='black',variable=b,value=2,tristatevalue=0)
        choose_gender.place(x=265,y=545)
        confirm_doc=Label(second_frame, text='''CHOOSE YOUR GENERAL DOCTOR''',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        confirm_doc.place(x=520,y=109)
        v = IntVar()
        confirm_button=Radiobutton(second_frame,text=' John Varghese - Oak Grove Therapy',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=v,value=1,tristatevalue=0)
        confirm_button.place(x=520,y=160)
        confirm_button=Radiobutton(second_frame,text=' Dr. Usha Manda - Therapistic',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=v,value=2,tristatevalue=0)
        confirm_button.place(x=520,y=210)
        confirm_button=Radiobutton(second_frame,text=' Dr Jasmin Raju - Tiger Health',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=v,value=3,tristatevalue=0)
        confirm_button.place(x=520,y=260)
        confirm_button=Radiobutton(second_frame,text=' Anand Radhakrishnan - TalkTechniques',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=v,value=4,tristatevalue=0)
        confirm_button.place(x=520,y=310)
        days=Label(second_frame, text='''CHOOSE DAYS OF WEEK''',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        days.place(x=585,y=360)
        r = IntVar()
        day=Checkbutton(second_frame, text='Monday', variable=r,font=('Bahnschrift Condensed',16),bg='white')
        day.place(x=520,y=405)
        s = IntVar()
        day=Checkbutton(second_frame, text='Tuesday', variable=s,font=('Bahnschrift Condensed',16),bg='white')
        day.place(x=620,y=405)
        t = IntVar()
        day=Checkbutton(second_frame, text='Wednesday', variable=t,font=('Bahnschrift Condensed',16),bg='white')
        day.place(x=725,y=405)
        u = IntVar()
        day=Checkbutton(second_frame, text='Thursday', variable=u,font=('Bahnschrift Condensed',16),bg='white')
        day.place(x=850,y=405)
        v = IntVar()
        day=Checkbutton(second_frame, text='Friday', variable=v,font=('Bahnschrift Condensed',16),bg='white')
        day.place(x=570,y=450)
        w = IntVar()
        day=Checkbutton(second_frame, text='Saturday', variable=w,font=('Bahnschrift Condensed',16),bg='white')
        day.place(x=660,y=450)
        x = IntVar()
        day=Checkbutton(second_frame, text='Sunday', variable=x,font=('Bahnschrift Condensed',16),bg='white')
        day.place(x=770,y=450)
        
        
        button=Button(second_frame, text='Confirm Appointment', font=('Bahnschrift Condensed',18),bg='white',fg='black')
        button.place(x=410,y=600)
        note=Label(second_frame, text='''NOTE- Once your appointment is confirmed hospital representative will
        be in contact with you through your registered
        phone number and email ID to reconfirm the appointment as per the doctors availability slots.
        Thank you!!''', font=('Bahnschrift Condensed',18),bg='yellow',fg='black')
        note.place(x=100,y=680)
        

def workshopcalc():
        def confirm():
                Invoice=Label(second_frame,text='INVOICE',fg='black')
                Invoice.place(x=570,y=450)


        
        WCPage = Toplevel(MPage)
        WCPage.geometry('1000x1500')

        main_frame=Frame(WCPage)
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

        global image7
        background6=Canvas(second_frame,width=1000,height=1500)
        image7=ImageTk.PhotoImage(Image.open("220d4aa99d158cfff3ad66bdd1f3357b.jpg"))
        background6.create_image(0,0,anchor='nw',image=image7)
        background6.pack(expand=True,fill=BOTH)

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()


        DEFAULT_MESSAGE=Label(second_frame,text=''' Dear MINDCOLOGISTS,
 We are sad to announce that the offline sessions for the workshops have been cancelled temporarily following strict COVID-19 
 protocal. The restrictions on group gatherings and travel allowances have cramped associated partners. Therefore workshops will be 
 conducted only in a restricted timeframe. Every workshop will be conducted everyday from 6 p.m. to 8 p.m. through an online Zoom 
 Meeting. You may choose the days of your choice. The details of each specific workshop will be emailed to you directly.''', justify=LEFT, font=('Bahnschrift Condensed',16),bg='yellow',fg='black', borderwidth=2, relief='solid')
        DEFAULT_MESSAGE.place(x=15,y=10)

        DETAILS=Label(second_frame,text='ENTER YOUR DETAILS',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        DETAILS.place(x=170, y=170)
    
        FIRSTNAME=Label(second_frame,text='Enter First Name',font=('Bahnschrift Condensed',15),bg='white',fg='black')
        FIRSTNAME.place(x=15, y=210)
        FIRSTNAME1_entry=Entry(second_frame,width=60)
        FIRSTNAME1_entry.place(x=145, y=215)
        FIRSTNAME1_entry.bind('<Return>',confirm)
        
        LAST_NAME = Label(second_frame, text="Enter Last Name:", font=("Bahnschrift Condensed",15),bg="white")
        LAST_NAME.place(x=15,y=250)
        LAST_NAME_ENTRY = Entry(second_frame, width=60)
        LAST_NAME_ENTRY.place(x=145,y=255)

        PHONE_NUMBER_1=Label(second_frame, text="Enter Phone Number 1:", font=("Bahnschrift Condensed",15),bg="white")
        PHONE_NUMBER_1.place(x=15,y=290)
        PHONE_NUMBER_1_ENTRY=Entry(second_frame, width=55)
        PHONE_NUMBER_1_ENTRY.place(x=180,y=295)
        PHONE_NUMBER_2 = Label(second_frame, text="Enter Phone Number 2:", font=("Bahnschrift Condensed",15),bg="white")
        PHONE_NUMBER_2.place(x=15,y=330)
        PHONE_NUMBER_2_ENTRY = Entry(second_frame, width=55)
        PHONE_NUMBER_2_ENTRY.place(x=180,y=335)

        EMAIL=Label(second_frame, text="Enter E-Mail Address:", font=("Bahnschrift Condensed",15),bg="white")
        EMAIL.place(x=15,y=370)
        EMAIL_ENTRY = Entry(second_frame, width=55)
        EMAIL_ENTRY.place(x=175,y=375)

        DATES=Label(second_frame,text='''CHOOSE DAYS OF THE WEEK''',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        DATES.place(x=130,y=420)

        Monday=Checkbutton(second_frame,text ='Monday',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=var1)
        Monday.place(x=15,y=470)

        Tuesday=Checkbutton(second_frame,text ='Tuesday',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=var2)
        Tuesday.place(x=125,y=470)

        Wednesday=Checkbutton(second_frame,text ='Wednesday',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=var3)
        Wednesday.place(x=235,y=470)

        Thursday=Checkbutton(second_frame,text ='Thursday',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=var4)
        Thursday.place(x=365,y=470)

        Friday=Checkbutton(second_frame,text ='Friday',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=var5)
        Friday.place(x=60,y=515)

        Saturday=Checkbutton(second_frame,text ='Saturday',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=var6)
        Saturday.place(x=160,y=515)

        Sunday=Checkbutton(second_frame,text ='Sunday',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=var7)
        Sunday.place(x=285,y=515)

        CHOICE=Label(second_frame,text='CHOOSE YOUR WORKSHOP',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        CHOICE.place(x=650,y=170)

        v=IntVar()
       

        BUTTON=Radiobutton(second_frame,text='AbsolutAnxiety - Mental || Message',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=v,value=1,tristatevalue=0)
        BUTTON.place(x=600,y=210)

        BUTTON=Radiobutton(second_frame,text='DawnOverDepression - Mending Minds',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=v,value=2,tristatevalue=0)
        BUTTON.place(x=600,y=260)

        BUTTON=Radiobutton(second_frame,text='Tata Trauma - Stepping Stone Health Centre',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=v,value=3,tristatevalue=0)
        BUTTON.place(x=600,y=310)

        BUTTON=Radiobutton(second_frame,text='AdiosAddiction - Medica Zone',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=v,value=4,tristatevalue=0)
        BUTTON.place(x=600,y=360)

        BUTTON=Radiobutton(second_frame,text='Addiction Extinction - The Sierra Club',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=v,value=5,tristatevalue=0)
        BUTTON.place(x=600,y=410)

        BUTTON=Radiobutton(second_frame,text='Feeling and Healing - Army Welfare Association',font=('Bahnschrift Condensed',16),bg='white',fg='black',variable=v,value=6,tristatevalue=0)
        BUTTON.place(x=600,y=460)

        

        CONFIRML=Button(second_frame,text='CONFIRM',font=('Bahnschrift Condensed',15),bg='white',fg='black',command=confirm)
        CONFIRML.place(x=475,y=570)

        sep=Separator(second_frame,orient='horizontal')
        sep.place(x=0,y=540)

        noOfDays = var1.get()+var2.get()+var3.get()+var4.get()+var5.get()+var6.get()+var7.get()
        Price = noOfDays*1499






        

def services():
    def viewworkshops():
        WPage = Toplevel(MPage)
        WPage.geometry('1000x1500')

        main_frame=Frame(WPage)
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

        global image6
        background5=Canvas(second_frame,width=1000,height=1500)
        image6=ImageTk.PhotoImage(Image.open("220d4aa99d158cfff3ad66bdd1f3357b.jpg"))
        background5.create_image(0,0,anchor='nw',image=image6)
        background5.pack(expand=True,fill=BOTH)

        WELCOME = Label(second_frame,text='''WELCOME TO THE WORKSHOPS PAGE
Here, find yourself amongst like-minded thinkers who'll help you get through any
problem! Talk and find new friends who'll join you hand-in-hand along with expert mentors
to guide you through this journey!! ''',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        WELCOME.place(x=130,y=7)

        ADDICTION_EXTINCTION=Label(second_frame,text=''' ADDICTION EXTINCTION - THE SIERRA CLUB

 WHEN - EVERY SUNDAY AT 6 p.m.

 Addiction Extinction is a nationwide program run by the Sierra Club. With the first program being held in 2001, they have been helping people of 
 all age groups come out of addiction for over 20 years. One of the most popular discussion groups today, the Sierra Club and its program is 
 mediated by highly trained professionals. Each group has about 10 to 15 people, making individual attention a key ascpect of this program.The 
 program is held in all major cities every Sunday.''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        ADDICTION_EXTINCTION.place(x=20,y=150)
        AD_SEAT=Button(second_frame,text='Book A Seat',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=workshopcalc)
        AD_SEAT.place(x=705,y=170)  

        FEELING_AND_HEALING=Label(second_frame,text=''' FEELING AND HEALING - ARMY ASSOCIATION

 WHEN - EVERY EVENING AT 4:30 p.m.

 Do you have an experience that has been haunting you? Are you suffering from post-trauma? Well then join the veterans of our Army everyday at
 4:30 p.m. to learn how to overcome post trauma and deal with it. Based out of the Army Welfare Association in Bangalore, they conduct offline
 as well as online sessions for those who are not living in Bangalore.''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        FEELING_AND_HEALING.place(x=20,y=360)
        FH_SEAT=Button(second_frame,text='Book A Seat',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=workshopcalc)
        FH_SEAT.place(x=705,y=380) 
        

        ABSOLUT_ANXIETY=Label(second_frame,text=''' ABSOLUT ANXIETY - MENTAL || MESSAGE
 
 WHEN - MONDAYS,WEDNESDAYS AND FRIDAYS FROM 6 TO 8 PM
 
 AbolutAnxiety is a workshop designed just for the patients experiencing anxiety related issues. Group discussions and interactive sessions are 
 designed to provide participants with the opportunity to increase their awareness on anxiety and how to overcome that illness. Held at RMA Hall 
 in Indiranagar, this support groups now also holds online conferences for better access.''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        ABSOLUT_ANXIETY.place(x=20,y=550)
        AA_SEAT=Button(second_frame,text='Book A Seat',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=workshopcalc)
        AA_SEAT.place(x=705,y=570) 

        DAWN_OVER_DEPRESSION=Label(second_frame,text=''' DAWN OVER DEPRESSION - MENDING MINDS
        
 WHEN - EVERY SATURDAY AND SUNDAY FROM 5 TO 8 PM

 DawnOverDepression is a workshop designed just for the patients experiencing depression and are not able to overcome depression. This 
 workshop consists of the following activities such as group discussions, interactive session, virtual meetings with people who fought depression
 in their past. This idea is designed to provide participants with the opportunity to increase their awareness of depression.''',justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        DAWN_OVER_DEPRESSION.place(x=20,y=740)
        DOD_SEAT=Button(second_frame,text='Book A Seat',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=workshopcalc)
        DOD_SEAT.place(x=705,y=760) 

        TATA_TRAUMA=Label(second_frame,text=''' TATA TRAUMA - STEPPING STONE HEALTH CENTRE
 
 WHEN - 4 DAYS A WEEK, AT ANY SUITABLE TIME FOR 4 HOURS
 
 Tata Trauma is a workshop that has been designed specifically for those patients who are suffering from post traumatical effects. The workshop
 includes interactive sessions, speeches from specialized doctors and more to help participants in broadening their knowledge on
 post trauma as well as how to overcome it.''',justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        TATA_TRAUMA.place(x=20,y=930)
        TT_SEAT=Button(second_frame,text='Book A Seat',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=workshopcalc)
        TT_SEAT.place(x=705,y=950)

        ADIOS_ADDICTION=Label(second_frame,text=''' ADIOS ADDICTION - MEDICAZONE
 
 WHEN - 3 DAYS A WEEK, FOR 4 HOURS
 
 Adios Addiction is a workshop that was born out of the thought to help those who wish to come out of of addiction. Whether the addiction may be
 a behavioural aspect, a chemical aspect or anything else, we've got you covered. The workshop includes group discussions, interactive 
 sessions, documentaries and more to allow participants an opportunity to widen their knowledge over addiction and conquer it.''',justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        ADIOS_ADDICTION.place(x=20,y=1120)
        ADD_SEAT=Button(second_frame,text='Book A Seat',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=workshopcalc)
        ADD_SEAT.place(x=705,y=1140)
    
    
    
    
    def viewspecial():
        SPage = Toplevel(MPage)
        SPage.geometry('1000x1500')

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
        background4=Canvas(second_frame,width=1000,height=1500)
        image5=ImageTk.PhotoImage(Image.open("220d4aa99d158cfff3ad66bdd1f3357b.jpg"))
        background4.create_image(0,0,anchor='nw',image=image5)
        background4.pack(expand=True,fill=BOTH)

        WELCOME = Label(second_frame,text='''WELCOME TO SPECIAL APPOINTMENTS PAGE
Here, choose amongst the best doctors who'll tackle any problem! You can count on 
them to heal you from the GCPages. Counter any problem in the best way possible
What are you waiting for? GO EXPLORE! ''',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        WELCOME.place(x=150,y=7)

        VIJAY_GANESHA=Label(second_frame,text=''' DR. VIJAY GANESHA - INSTITUTION OF MENTAL HEALTH
 QUALIFICATIONS - B.A in Psychology, M.A in Counselling Psychology and Social Psychology,
 PhD in Counselling Psychology

 SPECIALISATION - ANXIETY
 
 Dr Vijay Ganesha has over 40 years of experience in helping patients deal with anxiety-related issues. He also authored the best-selling book named
 "Declutter Your Mind". He frequently conducts workshops in both India and abroad on anxiety and how to deal with it.''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        VIJAY_GANESHA.place(x=15,y=150)
        VG_BOOK=Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=specialcalc)
        VG_BOOK.place(x=700,y=170)    

        RADHIKA_RAMANATHAN=Label(second_frame,text=''' RADHIKA RAMANATHAN - CAREFORYOU
 QUALIFICATIONS - B.A. in Psychology, M.A in Developmental Psychology and Social Psychology,
 PhD in Social Psychology

 SPECIALISATION - DEPRESSION

 Dr. Radhika Ramanathan is not a new name in the books. She is the host of the popular TV show "The Happy Labs", where she helps people overcome
 depression by showing the power of happiness. She has helped over 2500 people both on and off the show. ''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid' )
        RADHIKA_RAMANATHAN.place(x=15,y=360)
        RR_BOOK=Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=specialcalc)
        RR_BOOK.place(x=700,y=380)

        ANANYA_BAHRI = Label(second_frame,text=''' ANANYA BAHRI - OAK GROVE THERAPY CENTRE
 QUALIFICATIONS - B.A in Psychology, M.A in Social Psychology, PhD in Social Psychology
  
 SPECIALISATION - DEPRESSION
  
 Dr Ananya Bahri has over 21 years of experience in helping patients overcome depression. She regularly conducts workshops in India. She also helps
 over 150 people each year to come out of that phase let it be either online or offline consultations.''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black',
borderwidth=2, relief="solid")
        ANANYA_BAHRI.place(x=15,y=570)
        AB_BOOK=Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=specialcalc)
        AB_BOOK.place(x=700,y=590)

        DIYA_MORE=Label(second_frame,text=''' DR. DIYA MORE - A BETTER WAY THERAPY CENTRE
 QUALIFICATIONS - B.A in Psychology, M.A in Counselling Psychology, PhD in Counselling
 Psychology

 SPECIALISATION - ANXIETY
 
 Dr. Diya More has over 19 years of experience in helping patients overcome anxiety. She regularly visits countries like USA, UK, Australia etc to help
 patients who are dealing with anxiety. She has helped over 1300 people by taking 2 weeks of regular counselling sessions with her clients to get to  
 know more and more about their mental health/background, that makes it easy for her to help them get over this dreadful situation .''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black',
borderwidth=2, relief="solid")
        DIYA_MORE.place(x=15,y=760)
        DM_BOOK=Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=specialcalc)
        DM_BOOK.place(x=700,y=780)

        TARUN_MATTHEW=Label(second_frame,text=''' DR. TARUN MATTHEW - WELLBEING THERAPUTIC
 QUALIFICATIONS - B.A in Psychology, M.A in Developmental Psychology, M.A in Organizational
 Psychology, PhD. in Councelling Psychology
 
 SPECIALISATION - POST TRAUMA
 
 Dr. Tarun Matthew has over 25 years of experience in assisting more than 80000 patients suffering from post-trauma. He is the author of the book 
 "Trampling Trauma" which educates people on how to come out of trauma. Dr. Tarun Matthew is also the receiver of the prestigious B.C Roy National
 Award.''', justify=LEFT, font=("Bahnschrift Condensed",14),
 bg="white", fg="black", borderwidth=2, relief="solid")
        TARUN_MATTHEW.place(x=15, y=990)
        TM_BOOK=Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=specialcalc)
        TM_BOOK.place(x=700,y=1010)

        KARIM_LOK=Label(second_frame,text=''' DR. KARIM LOK - NIMHANS
 QUALIFICATIONS - B.A in Psychology, M.A in Social Psychology, PhD. in Social Psychology
 
 SPECIALISATION - ADDICTION

 Dr. Karim Lok is one of the most reputed doctors worldwide. He possesses over 25 years of experience in treating people with problems related to 
 addiction. Dr. Karim Lok frequently travels abroad to countries such as USA, UK and Australia to lecture to medical aspirants and also provides aid 
 to victims of addiction. Dr. Karim Lok records consulting over 150000 patients till date and also conducts regular seminars to educate 
 people about the negative effects of addiction and how to overcome addiction.''',justify=LEFT, font=("Bahnschrift Condensed",14), bg="white", fg="black", borderwidth=2, relief="solid")
        KARIM_LOK.place(x=15,y=1220)
        KL_BOOK = Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=specialcalc)
        KL_BOOK.place(x=700, y=1240)

    def viewgeneral():
        GDPage=Toplevel(MPage)
        GDPage.geometry('1000x900')
        

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
        background3=Canvas(second_frame,width=1000,height=900)
        image4=ImageTk.PhotoImage(Image.open("220d4aa99d158cfff3ad66bdd1f3357b.jpg"))
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
        JV_BOOK = Button (second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=generalcalc)
        JV_BOOK.place(x=700,y=170)

        USHA_MANDA=Label(second_frame,text = ''' DR. USHA MANDA - THERAPISTIC
 QUALIFICATIONS - B.A in Psychology, M.A in Organizational Psychology and in Councelling Psychology, 
 Ph.D in Councelling Psychology 

 Dr. Usha Manda has over 30 years of experience in the field of general Psychology. She is presently waged Therapistic() but is affiliated with several
 reputed health care centers in India such as NIMHANS, Apollo and Fortis. Dr. Usha Manda has helped more than 120000 people overcome obstacles
 related to mental health, stress, well-being and has also provided councelling to over 30000 patients.''',justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        USHA_MANDA.place(x=15,y=330)
        UM_BOOK = Button (second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=generalcalc)
        UM_BOOK.place(x=700,y=350)

        JASMIN_RAJU=Label(second_frame,text = ''' DR JASMIN RAJU - TIGER HEALTH
 QUALIFICATIONS - B.A in Psychology, M.A in Developmental Psychology and Organizational Psychology,
 PhD in Developmental Psychology
        
 Dr Jasmin Raju has over 25 years of experience in the field of psychology and has collabrated with several big companies on how to promote better 
 mental health amongst the employees. She is currently helping over 1500 people in Bangalore alone in conquering a diversity of mental issues. She 
 has been awarded several accolades for her tremendous feat in helping people.''',justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        JASMIN_RAJU.place(x=15,y=510)
        JS_BOOK = Button (second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=generalcalc)
        JS_BOOK.place(x=700,y=530)

        ANAND_RADHAKRISHAN=Label(second_frame,text = ''' ANAND RADHAKRISHNAN - TALK TECHNIQUES
 QUALIFICATIONS - B.A in Psychology, M.A in Human Factors Psychology and Counselling Psychology

 Anand Radhakrishnan is a reputed therapist who has been associated with Talk Techniques, an internationally reputed centre, for over 15 years. He 
 held high positions in several other organisations as the Head Therapist. He has helped well over 7000 patients so far and
 regularly holds workshops for group interactions as well.''',justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        ANAND_RADHAKRISHAN.place(x=15,y=690)
        AR_BOOK = Button (second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid",command=generalcalc)
        AR_BOOK.place(x=700,y=710)
        


    CPage=Toplevel(MPage)
    CPage.geometry('1000x600')

    global image3
    background2=Canvas(CPage,width=6000,height=600)
    image3=ImageTk.PhotoImage(Image.open("220d4aa99d158cfff3ad66bdd1f3357b.jpg"))
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

    WORKSHOPS=Button(CPage,text='SHOW ME THE WORKSHOPS',font=('Bahnschrift Condensed',14),bg='white',fg='black', command = viewworkshops)
    WORKSHOPS.place(x=650,y=320)


    
def loginclicked():
    def clicked_l():
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
                    SLogin = Label(LPage,text='LOGIN  SUCCESSFUL!!!',font=('Bahnschrift Condensed',20),bg='white',fg='black')
                    SLogin.place(x=200,y=250)
                    Click = Button(LPage,text='Click to Continue',font=('Bahnschrift Condensed',20),bg='white',fg='black',command=services)
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
