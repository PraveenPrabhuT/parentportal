# Importing Necessary Modules
import mysql.connector
import csv

# Login Function
access=0
def login():
    user = input("Enter Username: ")
    password= input("Enter Password: ")
    users = {"praveen":"password1", "sachin":"password2","aravind":"password3"}
    keyz=users.keys()
    if user in keyz:
        if users[user]==password:
            global login
            login=1
            print("Success")
        else:
            print("Enter correct password")
    else:
        print("User not found") 

# Fee Details Function
def fee_details():
    fee_detail=mysql.connector.connect(host="localhost", user="root", passwd="root",database="feeDetails")
    mycursor=mydb.cursor()
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
    mycursor=mydb.cursor()
    query1="SELECT * FROM fees WHERE roll = {}".format(rollNo)
    mycursor.execute(query)
    detail=mycursor.fetchall()
    if len(detail)==0:
        print("Roll No not found")
        break
    else:
        f.write("         ABC INTERNATIONAL SCHOOL \n")
        f.write("             FEE RECEIPT \n\n")
        line1=("Name         :  " + detail[1] + "\n")
        line2=("Class        :  " + detail[2] + "\n")
        line3=("Received     :  " + detail[3] + "\n")
        line4=("Payment mode :  " + detail[4] + "\n")
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
    f.write(s)
    f.close()

#Class Diary Function
def class_diary():
    f=open('class_diary.txt','r')
    diary=f.read()
    print (diary)
    f.close()

#Assignment Details Function
def assignment_details():
    f=open('assignment_details.txt','r')
    assignments=f.read()
    print(assignments)
    f.close()

#Announcements Function
def announcements():
    f=open('announcements.txt','r')
    announcements=f.read()
    print(announcements)
    f.close()

#Attendance Function
def attendance():
    f=open('attendance.txt','r')
    attendance=f.read()
    print(attendance)
    f.close()

#Timetable Function
def timetable():
    f=open('timetable.csv','r')
    timetable=csv.reader(f)
    for row in timetable:
        print(row)
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

while access=0:
    login()

stop=0
while stop==0:
    menu()
    ch=int(input('Enter your choice:'))

if ch==1:
    class_diary()
elif ch==2:
    assignment()
elif ch==3:
    announcement()
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
    stop=1
else:
    print("Please enter between 1 to 9")
