# Importing Necessary Modules

import mysql.connector
import csv
import stdiomask
import getpass
from prettytable import PrettyTable

# Login Function

access = 0
user = 'default'
def sqlLogin():
    global user
    user = input ("Enter Username: ")
    password = stdiomask.getpass(prompt = "Enter Password: ")
    mysql_connection = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "loginDetails")
    mycursor = mysql_connection.cursor()
    query = "SELECT password FROM login WHERE userID = \'"+user+"\';"
    mycursor.execute(query)
    loginDetails = mycursor.fetchall()
    CorrectPassword = str(loginDetails[0])
    CorrectPassword = CorrectPassword[2:-3]
    if len(loginDetails) == 0:
        print("User not found")
    else:
        if password == CorrectPassword:
            print("You have logged in successfully")
            global access
            access = 1
        else:
            print("Enter correct password")

# Fee Details Function

def fee_details():
    mysql_connection = mysql.connector.connect(host = "localhost", user = "root", passwd = "root",database = "feeDetails")
    mycursor = mysql_connection.cursor()
    rollNo = int(input("Enter roll number"))
    query = "SELECT * FROM fees WHERE roll = {}".format(rollNo)
    mycursor.execute(query)
    feeDetails = mycursor.fetchall()
    if len(feeDetails) == 0:
        print("Roll No not found")
    else:
        print("Name         :",feeDetails[1])
        print("Class        :",feeDetails[2])
        print("Amount Paid  :",feeDetails[3])
        print("Payment Mode :",feeDetails[4])
        print("Due left     :",50000-feeDetails[3])
    mycursor.close()

# Fee Receipt Generator Function

def fee_receipt():
    file = open('fee_receipt.txt','w')
    rollNo = int(input('Enter roll number:'))
    mysql_connection = mysql.connector.connect(host = "localhost", user = "root", passwd = "root",database = "feeDetails")
    mycursor = mysql_connection.cursor()
    query = "SELECT * FROM fees WHERE roll = {}".format(rollNo)
    mycursor.execute(query)
    feeDetails = mycursor.fetchall()
    if len(feeDetails) == 0:
        print("Roll No not found")
    else:
        detailTuple = tuple(feeDetails[0])
        f.write("         ABC INTERNATIONAL SCHOOL \n")
        f.write("             FEE RECEIPT \n\n")
        line1 = ("Name         :  " + str(detailTuple[1]) + "\n")
        line2 = ("Class        :  " + str(detailTuple[2]) + "\n")
        line3 = ("Received     :  " + str(detailTuple[3]) + "\n")
        line4 = ("Payment mode :  " + str(detailTuple[4]) + "\n")
        due_left = 50000 - detailTuple[3]
        line5 = ("Due left     :  " + due_left] + "\n")
        file.write(line1)
        file.write(line2)
        file.write(line3)
        file.write(line4)
        file.write(line5)
        file.write("\nAddress : #2, Abc street, 560043\n")
        file.write("Phone no: 1800-XXX-XXX")
        file.close()
        print("The receipt is generated as fee_receipt.txt")
    mycursor.close()

#Holiday List Function

def holiday_list():
    file = open('holiday_list.txt','r')
    HolidayList = file.read()
    print(HolidayList)
    file.close()

#Feedback Function

def feedback():
    file = open('feedback.txt','a')
    userFeedback = input('Kindly give your valuable feedback:')
    global user
    userFeedback = userFeedback+' given by '+str(user)+'\n'
    file.write(s)
    file.close()

#Class Diary Function

def class_diary():
    file = open('class_diary.txt','r')
    ClassDiary = file.readlines()
    print("\t\t\tCLASS DIARY")
    for i in ClassDiary:
        diaryContent = i.split("|")
        recepient = diaryContent[0].strip()
        if recepient in ['General',user]:
            print(diaryContent[1])
    file.close()

#Assignment Details Function

def assignment_details():
    file = open('assignment_details.txt','r')
    assignmentDetails = file.read()
    print("\t\t\tASSIGNMENT DETAILS")
    print(assignmentDetails)
    file.close()

#Announcements Function

def announcements():
    file = open('announcements.txt','r')
    announcements = file.read()
    print("\t\t\tANNOUNCEMENTS")
    print(announcements)
    file.close()

#Attendance Function

def attendance():
    global user
    file = open('attendance.csv','r')
    attendance = csv.reader(file)
    table = PrettyTable()
    table.title = 'Attendance'
    table.field_names = (['Name','Mon','Tue','Wed','Thu','Fri','Sat'])
    for row in attendance:
        if row[0] == user:
            table.add_row(row)
    table.align = "c"
    print(table)
    file.close()

#Timetable Function

def timetable():
    file = open('timetable.csv','r')
    time_table = csv.reader(file)
    table = PrettyTable()
    table.title = 'Class Timetable'
    table.field_names = (['Day','09 - 10','10 - 11','11 - 12','12 - 01','01 - 02','02 - 03'])
    for row in time_table:
        table.add_row(row)
    table.align = "c"
    print(table)
    file.close()

#Menu

def menu():
    print('''
        WELCOME TO PARENT PORTAL
        1. Class Diary
        2. Assignment
        3. Announcements
        4. Attendance 
        5. Timetable
        6. Fee Details
        7. Fee Receipt
        8. Holiday List
        9. Feedback
        0. Exit
    ''')
    choice = int(input('Enter your choice:'))
    if choice == 1:
        class_diary()
    elif choice == 2:
        assignment_details()
    elif choice == 3:
        announcements()
    elif choice == 4:
        attendance()
    elif choice == 5:
        timetable()   
    elif choice == 6:
        fee_details()
    elif choice == 7:
        fee_receipt()
    elif choice == 8:
        holiday_list()
    elif choice == 9:
        feedback()
    elif choice == 0:
        global stop
        stop = 1
    else:
        print("Please enter a number between 1 to 9")

while access == 0:
    sqlLogin()

stop = 0
while stop == 0:
    menu()