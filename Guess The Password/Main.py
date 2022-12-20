import time
import random
Error = random.randint(0,10) #picks a random number to couse errors on
Max = 3
Password = ""
Count = 10
validpasswords = ["Job","job","Jobs","jobs"]

while Count != "0":   
 Password = input("Password:")
 if Password in validpasswords:
    print ("Success")
    
    while Count != 0: #Starts countdown loop
        print (Count)
        Count = Count -1 #Decreases the value of count 
        time.sleep (1)
        if Count == Error:
            print ("ERROR REBOOTING")
            Count = 10
            Error = random.randint (1,10)
            break #stops the look 
    
 elif len(Password) == 0:
    print ("Please input Password")
    
 elif Count == 0:
     print ("You won the game congrats")
     break
    
 else: 
    if Max == 1:
      print ("YOU HAVE FAILED BEGONE!")
      break
    Max = Max -1
    print ("You have", Max, "Attepts") #Prints how many attepts you have left
    continue #Continue the loop

      
 

    