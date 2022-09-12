print ('This program will allow you to input your age and output whether you are able to drive or not.(Developed by Zainab Sarwar)')
age= int(input('Enter your age: '))
if age>=18:
    print('You are ligible for a drivers license')
elif age<18:
    print('You are inegible for a drivers license')
else:
    print('Invalid input')
