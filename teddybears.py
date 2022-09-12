print ('This program will allow you to input values and output the wage.(Developed by Zainab Sarwar)')
wt=0
wh=0
nt= int(input('Enter number of teddy bears made: '))
nh= int(input('Enter number of  hours worked: '))
wt=nt*2
wh=nh*5
if wt>wh:
    print ('The wage is ', wt, ' (teddy bears made)')
elif wh>wt:
    print ('The wage is ', wh, ' (hours worked)')
else:
    print (('The wage is ', wt, ' (both teddy bears made and hours worked)'))