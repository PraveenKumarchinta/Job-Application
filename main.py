import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
import re
from tkinter import filedialog
import os
import webbrowser
from pathlib import Path


filepath = ''
init_filePath = ''
ontop = False
ontop1 = False


def setflag(event):
    global ontop
    ontop = False


def setflag1(event):
    global ontop1
    ontop1 = False


def root():
    global ontop
    if not ontop:
        def choose_file():
            global filepath
            filepath = StringVar()
        # file = label_file_explorer.get()
            if(filepath == ""):
                filepath = filedialog.askopenfilename(initialdir=os.getcwd(),
                                                      title="Upload Your Resume",

                                                      filetypes=(("PDF",
                                                                  "*.pdf*"),
                                                                 #  ("all files",
                                                                 #   "**"),
                                                                 ))
            else:
                filepath = filedialog.askopenfilename(initialdir=filepath,
                                                      title="Upload Your Resume", filetypes=(("PDF",
                                                                                              "*.pdf*"),
                                                                                             #  ("all files",
                                                                                             #   "**"),
                                                                                             ))
                label_file_explorer.delete(0, "end")
                if not filepath:
                    label_file_explorer.insert(
                        0, "                           "+'No file choosen.')
                else:
                    fileName = Path(filepath).name
                    label_file_explorer.insert(
                        0, "                           "+fileName)

        def btn1():
            global validation
            validation = ''

            is_any_error = False
            first_name = f_name.get()
            last_name = l_name.get()
            E_mail = email.get()
            edu = n.get()
            Address_1 = Address1.get()
            Address_2 = Address2.get()
            country = select_country.get()
            city_name = ci_name.get()
            state_name = st_name.get()
            zipcode_number = zipcode.get()
            prifx = Phone_prifx.get()
            prifx = str(prifx)
            prifx = prifx.strip()
            phone = Phone_number.get()
            hobbiess = hobbies.get()
            company_name = company.get()
            job_title = job.get()
            year = yrs.get()
            reference1_name = ref1.get()
            reference1_phone_number = refph1.get()
            reference2_name = ref2.get()
            reference2_phone_number = refph2.get()

            # validation patterns
            first_name_last_name_validation = re.compile("^[A-Za-z ]+$")
            pattern_mail_validation = re.compile(
                r"^([a-z0-9\.-]+)@([a-z0-9-]+).([a-z]{2,8})(.[a-z]{2,8})?$")
            Address_validation = re.compile("([A-Za-z0-9 ])([/])?")
            city_pattern = re.compile("^[A-Za-z ]+$")
            state_pattern = re.compile("^[A-Za-z ]+$")
            zipcode_india = re.compile("^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$")
            # zipcode_usa = re.compile(
            #     "^([0-9]{5}(?:([- ])?:([])[0-9]{4}))$")
            zipcode_usa = re.compile(
                "^\d{5}([-]|\s*)?(\d{4})?$")
            prifx_pattern_india = re.compile("^[(+)]91$")
            # prifx_pattern_usa = re.compile("^[+1]+$")
            prifx_pattern_usa = re.compile("^[(+)]1")
            phone_number_pattern_india = re.compile(r"^[0-9]{10}$")
            phone_number_pattern_usa = re.compile(
                r"^\(?([0-9]{3})\)?[-.● ]?([0-9]{3})[-.●]?([0-9]{4})$")
            hobbies_pattern = re.compile("^[A-Za-z,0-9 ]+$")
            company_pattern = re.compile("^[A-Za-z ]+$")
            job_pattern = re.compile("^[A-Za-z. ]+$")
            year_pattern = re.compile("^[0-9A-za-z ]+$")
            reference1_pattern_name = re.compile("^[a-zA-Z ]+$")
            reference2_pattern_name = re.compile("^[a-zA-Z ]+$")

            # conditions for validations
            # first name and second name validation
            if not first_name:
                is_any_error = True
                validation += "|First Name| "
                # Messagebox.showerror("Warning!", "first name is blank")
            elif re.match(first_name_last_name_validation, first_name) is None:
                is_any_error = True
                Messagebox.showerror("Warning!", "Invalid First Name.")
            if not last_name:
                is_any_error = True
                validation += "|Last Name| "
                # Messagebox.showerror("Warning!", "last name is blank")
            elif re.match(first_name_last_name_validation, last_name) is None:
                is_any_error = True
                Messagebox.showerror("Warning!", "Invalid Last Name.")

            # E_mail validation

            if not E_mail:
                is_any_error = True
                validation += "|Email| "
                # Messagebox.showerror("Warning!", "Email is blank")
            elif re.match(pattern_mail_validation, E_mail) is None:
                is_any_error = True
                Messagebox.showerror("Warning!", "Invalid Email.")

            # Eduction validation

            if(edu == "Please Choose"):
                validation += "|Education| "
                # Messagebox.showerror("Warning!", "please Choose Education")

            # resume validation

            filename = filepath
            if not filename:
                validation += "|Upload Resume| "
                # Messagebox.showerror("Warning!", "choose file")
            else:
                def convertToBinaryData(filename):
                    with open(filename, 'rb') as file:
                        binaryData = file.read()
                    return binaryData

                def insertBLOB(biodataFile):
                    global file
                    file = convertToBinaryData(biodataFile)
                    return file

                insertBLOB(filename)
            # else:
            #   label_file_explorer.delete(0, "end")
            #   label_file_explorer.insert(0, "                           "+filepath)

            # address validation

            if not Address_1:
                is_any_error = True
                validation += "|Address#1| "
                # Messagebox.showerror("Warning!", "address1 is blank")
            elif re.match(Address_validation, Address_1) is None:
                is_any_error = True
                Messagebox.showerror("Warning!", "Invalid Address#1.")
            if not Address_2:
                is_any_error = True
                validation += "|Address#2| "
                # Messagebox.showerror("Warning!", "address2 is blank")
            elif re.match(Address_validation, Address_2) is None:
                is_any_error = True
                Messagebox.showerror("Warning!", "Invalid Address#2.")

            # country validation
            if(country == "Select a Country"):
                is_any_error = True
                validation += "|Country| "
                # Messagebox.showerror("Warning!", "select the country")

            # city and state validation

            if not city_name:
                is_any_error = True
                validation += "|City| "
                # Messagebox.showerror("Warning!", "City is blank")
            elif re.match(city_pattern, city_name) is None:
                is_any_error = True
                Messagebox.showerror("Warning!", "Invalid City.")
            if not state_name:
                is_any_error = True
                validation += "|State| "
                # Messagebox.showerror("Warning!", "State is blank")
            elif re.match(state_pattern, state_name) is None:
                is_any_error = True
                Messagebox.showerror("Warning!", "Invalid State.")

            # zipcode validation

            if not zipcode_number:
                is_any_error = True
                validation += "|ZipCode| "
                # Messagebox.showerror("Warning!", "zipcode number is blank")
            elif(country == "India"):
                if re.match(zipcode_india, zipcode_number) is None:
                    is_any_error = True
                    Messagebox.showerror(
                        "Warning!", "Invalid ZipCode(India).")
            elif(country == "USA"):
                if re.match(zipcode_usa, zipcode_number) is None:
                    is_any_error = True
                    Messagebox.showerror("Warning!", "Invalid ZipCode(USA).")

            # prefix validation
            if not prifx:
                is_any_error = True
                validation += "|Country Prefix Code| "
                # Messagebox.showerror("Warning!", "prifx number is blank")
            elif(country == "India"):
                if re.match(prifx_pattern_india, prifx) is None:
                    is_any_error = True
                    Messagebox.showerror(
                        "Warning!", "Invalid Country Prefix Code(India).")
            elif(country == "USA"):
                if re.match(prifx_pattern_usa, prifx) is None:
                    is_any_error = True
                    Messagebox.showerror(
                        "Warning!", "Invalid Country Prefix Code(USA).")

            # phone validation
            if not phone:
                is_any_error = True
                validation += "|Phone Number| "
                # Messagebox.showerror("Warning!", "phone number is blank")
            elif(country == "India"):
                if re.match(phone_number_pattern_india, phone) is None:
                    is_any_error = True
                    Messagebox.showerror(
                        "Warning!", "Invalid Phone Number(India).")
            elif(country == "USA"):
                if re.match(phone_number_pattern_usa, phone) is None:
                    is_any_error = True
                    Messagebox.showerror(
                        "Warning!", "Invalid Phone Number(USA).")

            # validate hobbies

            if not hobbiess:
                is_any_error = True
                validation += "|Hobbies| "
                # Messagebox.showerror("Warning!", "Hobby is blank")
            elif re.match(hobbies_pattern, hobbiess) is None:
                is_any_error = True
                Messagebox.showerror("Warning!", "Invalid Hobbies.")

            # Company validation

            if not company_name:
                is_any_error = True
                validation += "|Company| "
                # Messagebox.showerror("Warning!", "Company Name is blank")
            elif re.match(company_pattern, company_name) is None:
                is_any_error = True
                Messagebox.showerror("Warning!", "Invalid Company.")

            # job validation

            if not job_title:
                is_any_error = True
                validation += "|Job Position| "
                # Messagebox.showerror("Warning!", "Job is blank")
            elif re.match(job_pattern, job_title) is None:
                is_any_error = True
                Messagebox.showerror("Warning!", "Invalid Job Position.")

            # years validation

            if not year:
                is_any_error = True
                validation += "|Experience| "
                # Messagebox.showerror("Warning!", "Experience is blank")
            elif re.match(year_pattern, year) is None:
                is_any_error = True
                Messagebox.showerror(
                    "Warning!", "Invalid Months/Years of Experience.")

            # validation reference1 name

            if not reference1_name:
                is_any_error = True
                validation += "|Referer#1 Name| "
                # Messagebox.showerror("Warning!", " Name is blank in reference1")
            elif re.match(reference1_pattern_name, reference1_name) is None:
                is_any_error = True
                Messagebox.showerror("Warning!", "Invalid Referer#1 Name.")

            # validation reference1 phone
            if not reference1_phone_number:
                is_any_error = True
                validation += "|Referer#1 Number| "
                # Messagebox.showerror("Warning!", "phone number is blank in reference1")
            elif(country == "India"):
                if re.match(phone_number_pattern_india, reference1_phone_number) is None:
                    is_any_error = True
                    Messagebox.showerror(
                        "Warning!", "Invalid Referer#1 Number(India).")
            elif(country == "USA"):
                if re.match(phone_number_pattern_usa, reference1_phone_number) is None:
                    is_any_error = True
                    Messagebox.showerror(
                        "Warning!", "Invalid Referer#1 Number(USA).")

            # validation reference2 name
            if not reference2_name:
                is_any_error = True
                validation += "|Referer#2 Name| "
                # Messagebox.showerror("Warning!", " Name is blank in reference2")
            elif re.match(reference2_pattern_name, reference2_name) is None:
                is_any_error = True
                Messagebox.showerror("Warning!", "Invalid Referer#2 Name.")

            # validation reference2 phone
            if not reference2_phone_number:
                is_any_error = True
                validation += "|Referer#2 Number| "
            elif(country == "India"):
                if re.match(phone_number_pattern_india, reference2_phone_number) is None:
                    is_any_error = True
                    Messagebox.showerror(
                        "Warning!", "Invalid Referer#2 Number(India).")
            elif(country == "USA"):
                if re.match(phone_number_pattern_usa, reference2_phone_number) is None:
                    is_any_error = True
                    Messagebox.showerror(
                        "Warning!", "Invalid Referer#2 Number(USA).")

            if validation == '':
                # Messagebox.showinfo("su")
                if(is_any_error != False):
                    return
                else:
                    # sending data to database
                    con = mysql.connect(host="remotemysql.com", user="c6gfkUVJgL",
                                        password="pnYLdMlB7F", database="c6gfkUVJgL")
                    cursor = con.cursor()
                    query = "INSERT INTO student_details (First_name,Last_name,Email,Education,resume,Address_1,Address_2,City_name,State_name,Zipcode_number,Country,Prefix,Phone_number,Hobbies,Company_name,Job_title,Duration,Reference1_name,Reference1_phone_number,Reference2_name,Reference2_phone_number) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    values = (first_name, last_name, E_mail, edu, file, Address_1, Address_2, city_name, state_name, zipcode_number, country, prifx,
                              phone, hobbiess, company_name, job_title, year, reference1_name, reference1_phone_number, reference2_name, reference2_phone_number)
                    course = cursor.execute(query, values)
                    con.commit()

                    Messagebox.showinfo(
                        "Insert Status", "Inserted successfully")
                    con.close()

            else:
                Messagebox.showerror("Enter the following", validation)

        root = tkinter.Toplevel()
        root.geometry("412x717")
        root.configure(background='white')
        style = ttk.Style()
        root.title("Job Application")
        root.resizable(False, False)

        label = ttk.Label(root, background="brown")
        # width=412, height=1
        label.pack(ipadx=412, ipady=1)

        label_1 = ttk.Label(root, text="Job Application", background='white', foreground="black", font=(
            'Verdana', 18, 'bold'))  # .pack(ipadx=200, ipady=21)
        label_1 = label_1.place(x=105, y=21)

        label_2 = ttk.Label(root, text="Personal Information",
                            background='white', foreground="brown", font=('Roboto', 10, 'bold'))
        label_2.place(x=5, y=55)

        label_3 = Label(root, text="Name", background='white',
                        foreground="black")
        label_3.place(x=5, y=80)

        label_4 = Label(root, text="First Name", font=(
            'verdana', 7), background="white")
        label_4.place(x=125, y=100)

        label_5 = Label(root, text="Last Name", font=(
            'verdana', 7), background="white")
        label_5.place(x=262, y=100)

        label_6 = Label(root, text="Email", background='white',
                        foreground="black")
        label_6.place(x=5, y=120)

        label_7 = Label(root, text="Education", background='white',
                        foreground="black").place(x=5, y=150)
        label_8 = Label(root, text="Resume", background='white',
                        foreground="black").place(x=5, y=180)
        label_9 = Label(root, text="Address", background='white',
                        foreground="black").place(x=5, y=215)
        label_10 = Label(root, text="Address Line #1", font=(
            'verdana', 6), background="white").place(x=230, y=230)
        label_11 = Label(root, text="Address Line #2", font=(
            'verdana', 6), background="white").place(x=230, y=260)
        label_12 = Label(root, text="Country", font=(
            'verdana', 6), background="white").place(x=230, y=295)
        label_13 = Label(root, text="City", font=(
            'verdana', 6), background="white").place(x=190, y=327)
        label_14 = Label(root, text="State", font=(
            'verdana', 6), background="white").place(x=280, y=327)
        label_15 = Label(root, text="Zip Code", font=(
            'verdana', 6), background="white").place(x=325, y=327)
        label_16 = Label(root, text="Phone Number", background='white',
                         foreground="black").place(x=5, y=340)
        label_17 = Label(root, text="Prefix", font=(
            'verdana', 6), background="white").place(x=131, y=358)
        label_18 = Label(root, text="Number", font=(
            'verdana', 6), background="white").place(x=262, y=358)
        label_19 = Label(root, text="What are your hobbies?",
                         background='white', foreground="black").place(x=5, y=370)
        label_20 = Label(root, text="Previous/Current Employment Details", background='white', foreground="brown", font=(
            'Verdana', 10, 'bold')).place(x=5, y=410)
        label_21 = Label(root, text="Company", background='white',
                         foreground="black").place(x=5, y=430)
        label_22 = Label(root, text="Job Position", background='white',
                         foreground="black").place(x=5, y=460)
        label_23 = Label(root, text="Experience", background='white',
                         foreground="black").place(x=5, y=485)
        # Label(root, text="here?", background='white', foreground="black").place(x=5, y=500)
        label_24 = Label(root, text="Reference #1", background='white', foreground="brown", font=(
            'Verdana', 10, 'bold')).place(x=5, y=520)
        label_25 = Label(root, text="Name", background='white',
                         foreground="black").place(x=5, y=545)
        label_26 = Label(root, text="Phone", background='white',
                         foreground="black").place(x=5, y=565)
        label_27 = Label(root, text="Reference #2", background='white', foreground="brown", font=(
            'Verdana', 10, 'bold')).place(x=5, y=590)
        label_28 = Label(root, text="Name", background='white',
                         foreground="black").place(x=5, y=615)
        label_29 = Label(root, text="Phone", background='white',
                         foreground="black").place(x=5, y=640)
        # NAME ENTRY
        f_name = Entry(root, background="white")
        f_name.place(x=128, y=80)
        l_name = Entry(root, background="white")
        l_name.place(x=265, y=80)

        # email entry
        email = Entry(root, width="40", background="white")
        email.place(x=128, y=123)

        # Education Entry

        n = tkinter.StringVar(value='Please Choose')
        course = ttk.Combobox(root, width=26, textvariable=n,
                              state="readonly")
        course['values'] = ("Under Graduate", "Post Graduate",
                            "Diploma", "High School")
        course.place(x=128, y=150)
        course.current()

        # File browser
        label_file_explorer = Entry(
            root, background="white", width=43, state="normal")
        label_file_explorer.insert(INSERT, "                           ")
        label_file_explorer.insert(END, " No file choosen yet.")
        label_file_explorer.bind("<Key>", lambda e: "break")
        label_file_explorer.place(x=128, y=177, height=32)
        Btn2 = Button(root, text="choose file", command=choose_file)
        Btn2.pack(ipadx=10, ipady=1)
        Btn2.place(x=130, y=179)

        # Address
        Address1 = Entry(root, width="43", background="white")
        Address1.place(x=128, y=215)
        Address2 = Entry(root, width="43", background="white")
        Address2.place(x=128, y=243)

        # select a country
        select_country = tkinter.StringVar(value='Select a Country')
        course = ttk.Combobox(
            root, width=38, textvariable=select_country, state="readonly")
        course['values'] = ("India", "USA")
        course.place(x=128, y=275)
        course.current()

        # City
        ci_name = Entry(root, width="23", background="white")
        ci_name.place(x=128, y=310)

        # state
        st_name = Entry(root, width="6", background="white")
        st_name.place(x=273, y=310)

        # Zip code
        zipcode = Entry(root, width="10", background="white")
        zipcode.place(x=316, y=310)

        # Phone Number
        Phone_prifx = Entry(
            root, width="5", background="white")
        Phone_prifx.place(x=128, y=340)

        Phone_number = Entry(root, width="36", background="white")
        Phone_number.place(x=170, y=340)

        # hobbies?
        hobbies = Entry(root, width="65", background="white")
        hobbies.place(x=5, y=390)

        # company name
        company = Entry(root, width="40", background="white")
        company.place(x=128, y=435)

        # Job title
        job = Entry(root, width="40", background="white")
        job.place(x=128, y=460)

        # how long were you here?
        yrs = Entry(root, width="40", background="white")
        yrs.place(x=128, y=490)

        # Reference#1 name
        ref1 = Entry(root, width="40", background="white")
        ref1.place(x=128, y=545)

        # Reference#1 Phone
        refph1 = Entry(root, width="40", background="white")
        refph1.place(x=128, y=570)

        # Reference#2 name
        ref2 = Entry(root, width="40", background="white")
        ref2.place(x=128, y=615)

        # Reference#2 Phone
        refph2 = Entry(root, width="40", background="white")
        refph2.place(x=128, y=640)
        # style.configure('W.TButton', font=(
        #     'Roboto', 10, 'bold'), background="brown")
        # btn1 = Button(root, text="Apply", style='W.TButton', command=btn1)
        # btn1.place(x=169, y=685)
        style.configure('C.TLabel', padding=[
                        5, 5, 15, 5], font=('Roboto', 10, 'bold'))
        style.map('C.TLabel',
                  foreground=[('!active', 'white'), ('active', 'white')],
                  background=[('!disabled', 'brown')],
                  relief=[('active', 'sunken'),
                          ('active', 'raised')]
                  )
        btn1 = Button(root, text="  Apply", style='C.TLabel', command=btn1)
        btn1.place(x=169, y=675)
        root.bind('<Destroy>', setflag)

    ontop = True


def root1():
    global ontop1
    if not ontop1:

        def write_file(data, filename):
            # Convert binary data to proper format and write it on Hard Disk
            with open(filename, 'wb') as file:
                file.write(data)

        def search():
            defaultValue = "Choose Applicant's ID"
            print("search started")
            id = entery_of_search.get()
            print(id)

            if (id == defaultValue):
                Messagebox.showerror(
                    "Select the ID", "Please choose an user ID to download their resume.")
            else:
                global init_filePath
                init_filePath = StringVar()

                init_filePath = filedialog.askdirectory()

                if not init_filePath:
                    print("no file path")
                    return Messagebox.showerror("No File Path", "Please select a valid path to download resume.")
                else:
                    print("entered file path")
                    try:
                        id = entery_of_search.get()
                        con = mysql.connect(host="remotemysql.com", user="c6gfkUVJgL",
                                            password="pnYLdMlB7F", database="c6gfkUVJgL")
                        cursor = con.cursor()
                        sql = "SELECT * FROM student_details WHERE id = %s"
                        cursor.execute(sql, (id,))
                        record = cursor.fetchall()

                        for row in record:
                            name = row[1]
                            userfilename = (name+".pdf")
                            finalPath = os.path.join(
                                init_filePath, userfilename)
                            file = row[5]
                            write_file(file, finalPath)
                            dlPath = ('file:///'+finalPath)
                            Messagebox.showinfo('Job Application', str(
                                'Successfully downloaded the Resume of '+name))
                        if not init_filePath:
                            return exit()
                        else:
                            entery_of_search.set(value=defaultValue)

                            webbrowser.open(dlPath)

                    except mysql.Error as error:
                        Messagebox.showerror("sql error", error)
                    # finally:
                    #     if con.is_connected():
                    #         cursor.close()
                    #         con.close()
                    #         print("MySQL connection is closed")

        def update(rows):
            for i in rows:
                trv.insert('', 'end', values=i)

        con = mysql.connect(host="remotemysql.com", user="c6gfkUVJgL",
                            password="pnYLdMlB7F", database="c6gfkUVJgL")
        cursor = con.cursor()
        cursor.execute(
            "select id,First_name,Last_name,Email,Education,Address_1,Address_2,City_name,State_name,Zipcode_number,Country,Prefix,Phone_number,Hobbies,Company_name,Job_title,Duration,Reference1_name,Reference1_phone_number,Reference2_name,Reference2_phone_number from student_details")
        rows = cursor.fetchall()

        root1 = tkinter.Tk()
        q = StringVar()
        root1.geometry("1530x720")
        root1.configure(bg='black')
        style = ttk.Style(root1)
        style = ttk.Style(root1)
        style.theme_use('alt')
        root1.title("Job Applications")
        root1.resizable(False, False)
        wrapper1 = LabelFrame(root1, text="  Applicant's Resume Details")
        wrapper1.pack(fill="both", expand="yes", padx="10", pady="5")
        trv = Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                          12, 13, 14, 15, 16, 17, 18, 19, 20, 21), show="headings", height="14")
        trv.pack()
        wrapper2 = LabelFrame(root1, text="  Download Resume")
        wrapper2.pack(fill="both", expand="yes", padx="10", pady="5")

        trv.pack(side=RIGHT)
        trv.place(x=0, y=0)
        trv.heading(1, text="ID")
        trv.heading(2, text="First Name")
        trv.heading(3, text="Last Name")
        trv.heading(4, text="Email")
        trv.heading(5, text="Education")
        trv.heading(6, text="Address")
        trv.heading(7, text="Address")
        trv.heading(8, text="City")
        trv.heading(9, text="State")
        trv.heading(10, text="PinCode")
        trv.heading(11, text="Country")
        trv.heading(12, text="Pre")
        trv.heading(13, text="Phone")
        trv.heading(14, text="Hobby")
        trv.heading(15, text="Company")
        trv.heading(16, text="Position")
        trv.heading(17, text="Experience")
        trv.heading(18, text="Ref#1 Name")
        trv.heading(19, text="Ref#1 Number")
        trv.heading(20, text="Ref#2 Name")
        trv.heading(21, text="Ref#2 Number")

        trv.column("1", width=20, minwidth=30)
        trv.column("2", width=80, minwidth=100)
        trv.column("3", width=80, minwidth=100)
        trv.column("4", width=120, minwidth=150)
        trv.column("5", width=92, minwidth=93)
        trv.column("6", width=100, minwidth=120)
        trv.column("7", width=100, minwidth=120)
        trv.column("8", width=70, minwidth=80)
        trv.column("9", width=60, minwidth=70)
        trv.column("10", width=50, minwidth=70)
        trv.column("11", width=50, minwidth=60)
        trv.column("12", width=20, minwidth=30)
        trv.column("13", width=70, minwidth=90)
        trv.column("14", width=90, minwidth=91)
        trv.column("15", width=80, minwidth=81)
        trv.column("16", width=80, minwidth=85)
        trv.column("17", width=68, minwidth=69)
        trv.column("18", width=70, minwidth=90)
        trv.column("19", width=60, minwidth=70)
        trv.column("20", width=70, minwidth=90)
        trv.column("21", width=60, minwidth=70)

        # vertical_scorllbar
        yscrollbar = ttk.Scrollbar(
            wrapper1, orient="vertical", command=trv.yview)
        yscrollbar.pack(side=RIGHT, fill="y")
        trv.configure(yscrollcommand=yscrollbar.set)
        # horizontal_scrollvar
        xscrollbar = ttk.Scrollbar(
            wrapper1, orient="horizontal", command=trv.xview)
        xscrollbar.pack(side=BOTTOM, fill="x")
        # trv.configure(yscorllcommand=yscrollbar.set, xscrollcommand=Scrollbar)
        trv.configure(xscrollcommand=xscrollbar.set)
        update(rows)

        def getId():
            con = mysql.connect(host="remotemysql.com", user="c6gfkUVJgL",
                                password="pnYLdMlB7F", database="c6gfkUVJgL")
            cursor = con.cursor()
            cursor.execute("select id from student_details")
            rows = cursor.fetchall()
            listOfID = []
            for row in rows:
                listOfID.append(row[0])
            return listOfID

        lel = Label(wrapper2, text="Download Applicant's Resume as PDF")
        lel.pack(side=tkinter.LEFT, padx=10)
        # lel1 = Label(wrapper2, text="Hear you can download Resume PDF ")
        # lel1.pack(side=tkinter.LEFT, padx=10, pady=10)

        entery_of_search = StringVar(wrapper2)
        entery_of_search.set("Choose Applicant's ID")
        course = ttk.Combobox(
            wrapper2, width=26, textvariable=entery_of_search, values=getId(), state="readonly")
        course.pack(side=tkinter.LEFT, padx=6)
        btn = Button(wrapper2, text="Download", command=search)
        btn.pack(side=tkinter.LEFT, padx=6)
        root1.bind('<Destroy>', setflag1)
    ontop1 = True


top = tkinter.Tk()
top.geometry("250x250")
top.configure(bg='white')
top.title("Applications")
top.resizable(False, False)

# top.iconbitmap('icon.ico')

'''
bg = PhotoImage(file="D:/Downloads/Untitled300(1).jpg")
label = Label(top, image=bg)
label(x=0, y=0, relwidth=1, relheigh=1)
'''
button = tkinter.Button(top, text="Apply", font=(
    'Roboto', 10, 'bold'), bg="brown", fg="white", width="8", height="1", command=root)
button.place(x=100, y=50)
button1 = tkinter.Button(top, text="Details", font=(
    'Roboto', 10, 'bold'), bg="brown", fg="white", width="8", height="1", command=root1)
button1.place(x=100, y=100)


top.mainloop()
