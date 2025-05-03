# IF = Do some code only IF some condition is true Else do something else

age =  int(input("Enter Your Age : "))


if age > 100:
          print("You to old to sign up")
          
elif age >=  18 :
 print("You are now signed up!")
 
elif age < 0:
          print("You haven't born yet")

else:
          print("You must be 18+ to sign up")