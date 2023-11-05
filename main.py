import sqlite3
import csv

# with open ('students.csv','r') as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader) # skip first row
#     for row in reader:
#         myCursor.execute("INSERT INTO Students(FirstName, LastName, GPA, Major, FacultyAdvisor, Address, City, State, ZipCode, MobilePhoneNumber, isDeleted) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
#                          (row[0],row[1], row[8], row[7], 0, row[2], row[3], row[4], row[5], row[6], 0),)
#         conn.commit()
###### Function for Section B #######
def getAllStudents():
    conn = sqlite3.connect('../StudentDB.sqlite')
    myCursor = conn.cursor()
    myCursor.execute("SELECT * From Students")
    data = myCursor.fetchall()
    for row in data:
        if row[11] == 0:
            print(row)
    myCursor.close()
###### Function for Section C #######
def addNewStudent():
    conn = sqlite3.connect('../StudentDB.sqlite')
    myCursor = conn.cursor()
    ##### Start of information gathering #####
    fName = input("Please enter the new student's first name:\n")
    lName = input("Please enter the new student's last name:\n")
    GPA = input("Please enter the new student's GPA:\n")
    ##### Checks for valid Float Input #####
    isGPA = False
    while isGPA == False:
        try:
            float(GPA)
            isGPA = True
        except ValueError:
            GPA = input('Please input a valid GPA:\n')
    major = input("Please enter the new student's major:\n")
    facAdvisor = input("Please enter the new student's Faculty Advisor:\n")
    address = input("Please enter the new student's street address:\n")
    city = input("Please enter the new student's city address:\n")
    state = input("Please enter the new student's state address:\n")
    zipCode = input("Please enter the new student's ZIP Code:\n")
    mobilePhone = input("Please enter the new student's mobile phone number:\n")
    ##### End of Information gathering ######
    myCursor.execute(
        "INSERT INTO Students(FirstName, LastName, GPA, Major, FacultyAdvisor, Address, City, State, ZipCode, MobilePhoneNumber, isDeleted) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                              (fName, lName, GPA, major, facAdvisor, address, city, state, zipCode,mobilePhone, 0),)
    conn.commit()
    print('Completed:')
    myCursor.execute(f"SELECT * From Students WHERE FirstName = '{fName}' AND LastName = '{lName}'")
    data = myCursor.fetchall()
    print(data)
    myCursor.close()

###### Function for Section D #######
def updateStudentRecord():
    conn = sqlite3.connect('../StudentDB.sqlite')
    myCursor = conn.cursor()
    studentID = input("Please input the Student ID you would like to update:\n")
    validInput = False
    ##### Checks for a valid input, ensuring INT Value is provided ######
    while validInput == False:
        try:
            studentID = int(studentID)
            myCursor.execute(f"SELECT * From Students Where StudentId = '{studentID}';")
            data = myCursor.fetchall()
            ##### Confirms whether the student is found or not #####
            if len(data) < 1:
                studentID = input('We can not find that Student ID, please try another:\n')
            else:
                print(data)
                confirm = input("Is this the correct student? (Y/N):\n")
                if confirm.lower() == 'y':
                    validInput = True
                else:
                    studentID = input("Please input the Student ID you would like to update:\n")
        except ValueError:
            studentID = input('Please input a valid selection:\n')
    ##### Checks for a valid input, ensuring INT Value is provided ######
    field = input("Please the NUMBER of which field you would like to update:\n1. Major\n2. Advisor ID\n3. Mobile Phone Number\n4. Exit\n")
    validInput = False
    while validInput == False:
        try:
            field = int(field)
            if field < 1 or field > 4:
                field = input('Please input a valid selection:\n')
            else:
                validInput = True
        except ValueError:
            field = input('Please input a valid selection:\n')
    ##### Conditional to update correct field #####
    if field == 1:
        newVal = input("What is the student's new major?\n")
        myCursor.execute(f"UPDATE Students SET Major = '{newVal}' WHERE StudentId = '{studentID}'")
        conn.commit()
        myCursor.execute(f"SELECT * From Students Where StudentId = '{studentID}';")
        data = myCursor.fetchall()
        print(f"Student ID: {studentID} has been updated.")
        print(data)
    elif field == 2:
        newVal = input("What is the Advisor ID of the student's new Advisor?")
        myCursor.execute(f"UPDATE Students SET AdvisorID = '{newVal}' WHERE StudentId = '{studentID}'")
        conn.commit()
        myCursor.execute(f"SELECT * From Students Where StudentId = '{studentID}';")
        data = myCursor.fetchall()
        print(f"Student ID: {studentID} has been updated.")
        print(data)
    elif field == 3:
        newVal = input("What is the student's new mobile number?\n")
        myCursor.execute(f"UPDATE Students SET MobilePhoneNumber = '{newVal}' WHERE StudentId = '{studentID}'")
        conn.commit()
        myCursor.execute(f"SELECT * From Students Where StudentId = '{studentID}';")
        data = myCursor.fetchall()
        print(f"Student ID: {studentID} has been updated.")
        print(data)
    myCursor.close()

###### Function for Section E #######
def deleteStudent():
    conn = sqlite3.connect('../StudentDB.sqlite')
    myCursor = conn.cursor()
    studentID = input("Please enter the student ID you would like to delete:\n")
    validInput = False
    while validInput == False:
        try:
            studentID = int(studentID)
            myCursor.execute(f"SELECT * From Students Where StudentId = '{studentID}';")
            data = myCursor.fetchall()
            ##### Confirms whether the student is found or not #####
            if len(data) < 1:
                studentID = input('We can not find that Student ID, please try another:\n')
            else:
                print(data)
                confirm = input("Is this the correct student? (Y/N):\n")
                if confirm.lower() == 'y':
                    myCursor.execute(
                        f"UPDATE Students SET isDeleted = 1 WHERE StudentId = '{studentID}'")
                    print(f"Student ID: {studentID} has been deleted.")
                    conn.commit()
                    validInput = True
                else:
                    studentID = input("Please input the Student ID you would like to update:\n")
        except ValueError:
            studentID = input('Please input a valid selection:\n')
            
