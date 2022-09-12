theSeason=str
numMonth=int(input("Enter a month (between 1 to 12): "))

if numMonth>12 or numMonth<=0:
    print("Invalid input. Enter a value between 1 to 12 and try again.")
    numMonth=int(input("Enter a month (between 1 to 12): "))

if numMonth<=12 and numMonth>=1:
    if numMonth == 12:
        theSeason= "Winter"
    elif numMonth>=9:
        theSeason= "Autumn"
    elif numMonth>=6:
        theSeason= "Summer"
    elif numMonth>=3:
        theSeason= "Spring"
    else:
        theSeason= "Winter"
print ("the season is: ", theSeason)