import random
import string
length=int(input("Enter the number of characters:"))
password=""
char=string.ascii_letters
char+=string.digits
char+=string.punctuation
for i in range(length):
  password+=random.choice(char)
print("Your Password is:",password)  