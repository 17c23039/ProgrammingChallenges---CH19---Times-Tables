import time
import random

def quiz () :
  questsel = random.randint(1,3)
  if questsel == 1 :
    print(f"What is {num} x 1?" )
    answer = int(input())
    if answer == num * 1 :
      print("Correct!")
    else : 
      print("Incorrect!")
  elif questsel == 2 :
    print(f"What is {num} x 2?" )
    answer = int(input())
    if answer == num * 2 :
      print("Correct!")
    else : 
      print("Incorrect!")
  elif questsel == 3 :
    print(f"What is {num} x 1?" )
    answer = int(input())
    if answer == num * 1 :
      print("Correct!")
    else : 
      print("Incorrect!")




print("Times Tables! Let's learn them, with TT Guru!")
time.sleep(3)
print("What times tables would you like to learn? Enter the number.")
num = int(input())
print("Okay, generating a quiz for you...")
time.sleep(2)
quiz ()