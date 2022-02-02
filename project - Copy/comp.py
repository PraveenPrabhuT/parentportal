def fee_receipt():
    f=open('fee_receipt.txt','w')
    name=input('Enter the name:')
    fees=str(70000)
    x=' has paid the annual fee of '
    f.write(name)
    f.write(x)
    f.write(fees)
    print('The fees of Miss/Master',name,'has been paid')
    f.close()
def holiday_list():
    f=open('holiday_list.txt','r')
    x=f.read()
    print(x)
    f.close()
def feedback():
    f=open('feedback.txt','w')
    s=input('Kindly give your valuable feedback:')
    f.write(s)
    f.close()
print('''
8. for fee receipt
9. for holiday list
10. for feedback
''')
ch=int(input('Enter your command:'))
if ch==8:
       fee_receipt()
elif ch==9:
    holiday_list()
elif ch==10:
    feedback()
