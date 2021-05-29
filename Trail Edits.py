from tkinter import * 
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from tkinter import scrolledtext
from tkinter import ttk

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

        WELCOME = Label(second_frame,text='''WELCOME TO THE WORKSHOPs PAGE
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
        AD_SEAT=Button(second_frame,text='Click For More Info',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        AD_SEAT.place(x=705,y=170)  

        FEELING_AND_HEALING=Label(second_frame,text=''' FEELING AND HEALING - ARMY ASSOCIATION

 WHEN - EVERY EVENING AT 4:30 p.m.

 Do you have an experience that has been haunting you? Are you suffering from post-trauma? Well then join the veterans of our Army everyday at
 4:30 p.m. to learn how to overcome post trauma and deal with it. Based out of the Army Welfare Association in Bangalore, they conduct offline
 as well as online sessions for those who are not living in Bangalore.''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        FEELING_AND_HEALING.place(x=20,y=360)
        FH_SEAT=Button(second_frame,text='Click For More Info',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        FH_SEAT.place(x=705,y=380) 
        
#CONFIGURE THE TEXT FOR ABSOLUT ANXIETY
        ABSOLUT_ANXIETY=Label(second_frame,text=''' ABSOLUT ANXIETY - MENTAL || MESSAGE
 
 WHEN - MONDAYS,WEDNESDAYS AND FRIDAYS FROM 6 TO 8 PM
 
 AbolutAnxiety is a workshop designed just for the patients experiencing anxiety related issues. Group discussions and interactive sessions are 
 designed to provide participants with the opportunity to increase their awareness on anxiety and how to overcome that illness. Held at RMA Hall 
 in Indiranagar, this support groups now also holds online conferences for better access.''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        ABSOLUT_ANXIETY.place(x=20,y=550)
        AA_SEAT=Button(second_frame,text='Click For More Info',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        AA_SEAT.place(x=705,y=570) 

        DAWN_OVER_DEPRESSION=Label(second_frame,text=''' DAWN OVER DEPRESSION - MENDING MINDS
        
 WHEN - EVERY SATURDAY AND SUNDAY FROM 5 TO 8 PM

 DawnOverDepression is a workshop designed just for the patients experiencing depression and are not able to overcome depression. This 
 workshop consists of the following activities such as group discussions, interactive session, virtual meetings with people who fought depression
 in their past. This idea is designed to provide participants with the opportunity to increase their awareness of depression.''',justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        DAWN_OVER_DEPRESSION.place(x=20,y=740)
        DOD_SEAT=Button(second_frame,text='Click For More Info',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        DOD_SEAT.place(x=705,y=760) 

        TATA_TRAUMA=Label(second_frame,text=''' TATA TRAUMA - STEPPING STONE HEALTH CENTRE
 
 WHEN - 4 DAYS A WEEK, AT ANY SUITABLE TIME FOR 4 HOURS
 
 Tata Trauma is a workshop that has been designed specifically for those patients who are suffering from post traumatical effects. The workshop
 includes interactive sessions, speeches from specialized doctors and more to help participants in broadening their knowledge on
 post trauma as well as how to overcome it.''',justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        TATA_TRAUMA.place(x=20,y=930)
        TT_SEAT=Button(second_frame,text='Click For More Info',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        TT_SEAT.place(x=705,y=950)

        ADIOS_ADDICTION=Label(second_frame,text=''' ADIOS ADDICTION - MEDICAZONE
 
 WHEN - 3 DAYS A WEEK, FOR 4 HOURS
 
 Adios Addiction is a workshop that was born out of the thought to help those who wish to come out of of addiction. Whether the addiction may be
 a behavioural aspect, a chemical aspect or anything else, we've got you covered. The workshop includes group discussions, interactive 
 sessions, documentaries and more to allow participants an opportunity to widen their knowledge over addiction and conquer it.''',justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        ADIOS_ADDICTION.place(x=20,y=1120)
        ADD_SEAT=Button(second_frame,text='Click For More Info',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
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
them to heal you from the roots. Counter any problem in the best way possible
What are you waiting for? GO EXPLORE! ''',font=('Bahnschrift Condensed',18),bg='white',fg='black')
        WELCOME.place(x=150,y=7)

        VIJAY_GANESHA=Label(second_frame,text=''' DR. VIJAY GANESHA - INSTITUTION OF MENTAL HEALTH
 QUALIFICATIONS - B.A in Psychology, M.A in Counselling Psychology and Social Psychology,
 PhD in Counselling Psychology

 SPECIALISATION - ANXIETY
 
 Dr Vijay Ganesha has over 40 years of experience in helping patients deal with anxiety-related issues. He also authored the best-selling book named
 "Declutter Your Mind". He frequently conducts workshops in both India and abroad on anxiety and how to deal with it.''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        VIJAY_GANESHA.place(x=15,y=150)
        VG_BOOK=Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        VG_BOOK.place(x=700,y=170)    

        RADHIKA_RAMANATHAN=Label(second_frame,text=''' RADHIKA RAMANATHAN - CAREFORYOU
 QUALIFICATIONS - B.A. in Psychology, M.A in Developmental Psychology and Social Psychology,
 PhD in Social Psychology

 SPECIALISATION - DEPRESSION

 Dr. Radhika Ramanathan is not a new name in the books. She is the host of the popular TV show "The Happy Labs", where she helps people overcome
 depression by showing the power of happiness. She has helped over 2500 people both on and off the show. ''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid' )
        RADHIKA_RAMANATHAN.place(x=15,y=360)
        RR_BOOK=Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        RR_BOOK.place(x=700,y=380)

        ANANYA_BAHRI = Label(second_frame,text=''' ANANYA BAHRI - OAK GROVE THERAPY CENTRE
 QUALIFICATIONS - B.A in Psychology, M.A in Social Psychology, PhD in Social Psychology
  
 SPECIALISATION - DEPRESSION
  
 Dr Ananya Bahri has over 21 years of experience in helping patients overcome depression. She regularly conducts workshops in India. She also helps
 over 150 people each year to come out of that phase let it be either online or offline consultations.''', justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black',
borderwidth=2, relief="solid")
        ANANYA_BAHRI.place(x=15,y=570)
        AB_BOOK=Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
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
        DM_BOOK=Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
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
        TM_BOOK=Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        TM_BOOK.place(x=700,y=1010)

        KARIM_LOK=Label(second_frame,text=''' DR. KARIM LOK - NIMHANS
 QUALIFICATIONS - B.A in Psychology, M.A in Social Psychology, PhD. in Social Psychology
 
 SPECIALISATION - ADDICTION

 Dr. Karim Lok is one of the most reputed doctors worldwide. He possesses over 25 years of experience in treating people with problems related to 
 addiction. Dr. Karim Lok frequently travels abroad to countries such as USA, UK and Australia to lecture to medical aspirants and also provides aid 
 to victims of addiction. Dr. Karim Lok records consulting over 150000 patients till date and also conducts regular seminars to educate 
 people about the negative effects of addiction and how to overcome addiction.''',justify=LEFT, font=("Bahnschrift Condensed",14), bg="white", fg="black", borderwidth=2, relief="solid")

        KARIM_LOK.place(x=15,y=1220)
        KL_BOOK = Button(second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
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

        JASMIN_RAJU=Label(second_frame,text = ''' DR JASMIN RAJU - TIGER HEALTH
 QUALIFICATIONS - B.A in Psychology, M.A in Developmental Psychology and Organizational Psychology,
 PhD in Developmental Psychology
        
 Dr Jasmin Raju has over 25 years of experience in the field of psychology and has collabrated with several big companies on how to promote better 
 mental health amongst the employees. She is currently helping over 1500 people in Bangalore alone in conquering a diversity of mental issues. She 
 has been awarded several accolades for her tremendous feat in helping people.''',justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        JASMIN_RAJU.place(x=15,y=510)
        JS_BOOK = Button (second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
        JS_BOOK.place(x=700,y=530)

        ANAND_RADHAKRISHAN=Label(second_frame,text = ''' ANAND RADHAKRISHNAN - TALK TECHNIQUES
 QUALIFICATIONS - B.A in Psychology, M.A in Human Factors Psychology and Counselling Psychology

 Anand Radhakrishnan is a reputed therapist who has been associated with Talk Techniques, an internationally reputed centre, for over 15 years. He 
 held high positions in several other organisations as the Head Therapist. He has helped well over 7000 patients so far and
 regularly holds workshops for group interactions as well.''',justify=LEFT, font=('Bahnschrift Condensed',14),bg='white',fg='black', borderwidth=2, relief='solid')
        ANAND_RADHAKRISHAN.place(x=15,y=690)
        AR_BOOK = Button (second_frame,text='Book An Appointment',font=('Bahnschrift Condensed',14),bg='white',fg='black',borderwidth=2, relief="solid")
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
