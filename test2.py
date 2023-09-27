'''import random
import string

account = input("for which account do you want the password: ")
num = int(input("enter the length of the password: "))
password = "".join(random.choice(string.printable) for i in range(num))  # The string.printable contains a combination of digits, ascii_letters (lowercase and uppercase letters), punctuation, and whitespace.
print("Your password is:", password)'''
ch=input()
print("yes") if ch=='y' else print("no")