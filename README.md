# hmrparentportal-clone 
#parent portal
import  pickle
f=open(r'C:\Users\Sachin\Desktop\p.portal.txt','rb')
i=input('Do you want to enter student details(y/n):')
count=0
if i=='y':
    student_form_no=int(input('Enter the form number:'))
    student_name=input('Enter the name of the student:')
    Fathers_name=input('Enter the name of Father:')
    Mothers_name=input('Enter the name of Mother:')
    
