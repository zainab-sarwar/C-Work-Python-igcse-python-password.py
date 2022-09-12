lang=str(input("Enter the programming language you want to learn: "))
match lang:
  case 'JavaScript': 
    print ("You can become a web developer.")
  case 'Python': 
    print ("You can become a data scientist.")
  case 'PHP': 
    print ("You can become a backend developer..")
  case 'Solidity': 
    print ("You can become a blockchain developer.")
  case 'Java': 
    print ("You can become a mobile app developer.")
  case 'None': 
    print ("The language doesn't matter, what matters is solving problems!")
  case default:
    print ("Invalid language. Please try again")
