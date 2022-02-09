# Importing Necessary Modules
import mysql.connector
import csv
import stdiomask
import getpass
from prettytable import PrettyTable

# Login Function
access=0
user='default'
def login():
    global user
    user = input("Enter Username: ")
    password= stdiomask.getpass(prompt="Enter Password: ")
    users = {"praveen":"password1", "sachin":"password2","aravind":"password3"}
    keyz=users.keys()
    if user in keyz:
        if users[user]==password:
            global access 
            access=1
            print("You have logged in successfully")
        else:
            print("Enter correct password")
    else:
        print("User not found") 

#Login Function SQL Version
def sqlLogin():
    global user
    user = input ("Enter Username: ")
    password=stdiomask.getpass(prompt="Enter Password: ")
    login_details=mysql.connector.connect(host="localhost",user="root",passwd="root",database="loginDetails")
    mycursor=login_details.cursor()
    query="SELECT password FROM login WHERE userID = \'"+user+"\';"
    print(query)
    mycursor.execute(query)
    detail=mycursor.fetchall()
    CorrectPassword=str(detail[0])
    CorrectPassword=CorrectPassword[2:-3]
    if len(detail)==0:
        print("User not found")
    else:
        if password==CorrectPassword:
            print("You have logged in successfully")
            global access
            access=1
        else:
            print("Enter correct password")
# Fee Details Function
def fee_details():
    fee_detail=mysql.connector.connect(host="localhost", user="root", passwd="root",database="feeDetails")
    mycursor=fee_detail.cursor()
    rollNo=int(input("Enter roll number"))
    query="SELECT * FROM fees WHERE roll = {}".format(rollNo)
    mycursor.execute(query)
    detail=mycursor.fetchall()
    if len(detail)==0:
        print("Roll No not found")
    else:
        print(detail)
    mycursor.close()

# Fee Receipt Generator Function
def fee_receipt():
    f=open('fee_receipt.txt','w')
    rollNo=int(input('Enter roll number:'))
    fee_detail=mysql.connector.connect(host="localhost", user="root", passwd="root",database="feeDetails")
    mycursor=fee_detail.cursor()
    query1="SELECT * FROM fees WHERE roll = {}".format(rollNo)
    mycursor.execute(query1)
    detail=mycursor.fetchall()
    if len(detail)==0:
        print("Roll No not found")
    else:
        detailTuple=tuple(detail[0])
        f.write("         ABC INTERNATIONAL SCHOOL \n")
        f.write("             FEE RECEIPT \n\n")
        line1=("Name         :  " + str(detailTuple[1]) + "\n")
        line2=("Class        :  " + str(detailTuple[2]) + "\n")
        line3=("Received     :  " + str(detailTuple[3]) + "\n")
        line4=("Payment mode :  " + str(detailTuple[4]) + "\n")
        f.write(line1)
        f.write(line2)
        f.write(line3)
        f.write(line4)
        f.write("\nAddress : #2, Abc street, 560043\n")
        f.write("Phone no: 1800-XXX-XXX")
        f.close()
        print("The receipt is generated as fee_receipt.txt")
    mycursor.close()

#Holiday List Function
def holiday_list():
    f=open('holiday_list.txt','r')
    x=f.read()
    print(x)
    f.close()

#Feedback Function
def feedback():
    f=open('feedback.txt','a')
    s=input('Kindly give your valuable feedback:')
    global user
    s=s+' given by '+str(user)+'\n'
    f.write(s)
    f.close()

#Class Diary Function
def class_diary():
    f=open('class_diary.txt','r')
    diary=f.read()
    print("\t\t\tCLASS DIARY")
    print(diary)
    f.close()

#Assignment Details Function
def assignment_details():
    f=open('assignment_details.txt','r')
    assignments=f.read()
    print("\t\t\tASSIGNMENT DETAILS")
    print(assignments)
    f.close()

#Announcements Function
def announcements():
    f=open('announcements.txt','r')
    announcements=f.read()
    print("\t\t\tANNOUNCEMENTS")
    print(announcements)
    f.close()

#Attendance Function
def attendance():
    global user
    f=open('attendance.csv','r')
    attendance=csv.reader(f)
    table=PrettyTable()
    table_title='Attendance'+' Name :'+str(user)
    table.title=table_title
    table.field_names=(['Mon','Tue','Wed','Thu','Fri','Sat'])
    for row in attendance:
        table.add_row(row)
    table.align="c"
    print(table)
    f.close()

#Timetable Function
def timetable():
    f=open('timetable.csv','r')
    time_table=csv.reader(f)
    table=PrettyTable()
    table.title='Class Timetable'
    table.field_names=(['Day','09 - 10','10 - 11','11 - 12','12 - 01','01 - 02','02 - 03'])
    for row in time_table:
        table.add_row(row)
    table.align="c"
    print(table)
    f.close()

#Menu
def menu():
    print('''
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
    ch=int(input('Enter your choice:'))
    if ch==1:
        class_diary()
    elif ch==2:
        assignment_details()
    elif ch==3:
        announcements()
    elif ch==4:
        attendance()
    elif ch==5:
        timetable()   
    elif ch==6:
        fee_details()
    elif ch==7:
        fee_receipt()
    elif ch==8:
        holiday_list()
    elif ch==9:
        feedback()
    elif ch==0:
        global stop
        stop=1
    else:
        print("Please enter between 1 to 9")

while access==0:
    sqlLogin()

stop=0
while stop==0:
    menu()
