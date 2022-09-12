nums=[]
highvar=0
lowvar=100

for nums in range(8):
    nums=int(input("Enter a number between 0 and 100: "))
    if nums>=100 or nums<=0:
        print ("Invalid number. Enter a number between 0 and 100 and try again.")
        nums=int(input("Enter a number between 0 and 100: ")) 
    else:
        if nums>highvar:
            highvar=nums
        if nums<lowvar:
            lowvar=nums
next

print ("Highest is ", highvar)
print ("Lowest is ", lowvar)