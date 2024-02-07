import random 
import string 
password=""
char=string.ascii_letters
char+=string.digits
char+=string.punctuation
length=int(input("Enter the number of characters:"))
for i in range(length):
    password+=random.choice(char)
print(password)