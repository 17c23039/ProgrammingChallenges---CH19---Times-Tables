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
    print(f"What is {num} x 3?" )
    answer = int(input())
    if answer == num * 3 :
      print("Correct!")
    else : 
      print("Incorrect!")
  elif questsel == 4 :
    print(f"What is {num} x 4?" )
    answer = int(input())
    if answer == num * 4 :
      print("Correct!")
    else : 
      print("Incorrect!")
  elif questsel == 5 :
    print(f"What is {num} x 5?" )
    answer = int(input())
    if answer == num * 5 :
      print("Correct!")
    else : 
      print("Incorrect!")
  elif questsel == 6 :
    print(f"What is {num} x 6?" )
    answer = int(input())
    if answer == num * 6 :
      print("Correct!")
    else : 
      print("Incorrect!")
  elif questsel == 7 :
    print(f"What is {num} x 7?" )
    answer = int(input())
    if answer == num * 7 :
      print("Correct!")
    else : 
      print("Incorrect!")
  elif questsel == 8 :
    print(f"What is {num} x 8?" )
    answer = int(input())
    if answer == num * 8 :
      print("Correct!")
    else : 
      print("Incorrect!")
  elif questsel == 9 :
    print(f"What is {num} x 9?" )
    answer = int(input())
    if answer == num * 9 :
      print("Correct!")
    else : 
      print("Incorrect!")
  elif questsel 10 :
    print(f"What is {num} x 10?" )
    answer = int(input())
    if answer == num * 10 :
      print("Correct!")
    else : 
      print("Incorrect!")
  elif questsel 11 :
    print(f"What is {num} x 11?" )
    answer = int(input())
    if answer == num * 11 :
      print("Correct!")
    else : 
      print("Incorrect!")
  elif questsel == 12 :
    print(f"What is {num} x 12?" )
    answer = int(input())
    if answer == num * 12 :
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