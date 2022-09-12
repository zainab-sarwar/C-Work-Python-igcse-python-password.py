password= "there_is_no_password"
pw=False
tries=0

while pw is False and tries<3: #to keep running until either 3 tries reached or password is correct
    userinput=str(input("Enter the Password: ")) #to collect the users answer
    if userinput==password:#to check if users input matches the answer
        print ("Correct Password")
        pw=True #stops taking answers since correct answer is reached
    else:
        tries=tries+1 #to count how many tries have been taken
        print ("Incorrect Password. ", 3-tries, " try/tries remaining.") #ask the user to reinput

