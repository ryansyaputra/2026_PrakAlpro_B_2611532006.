# Name: Ryan Syaputra
# NIM: 2611532006
# Question 5

username = input("Username: ")
if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")

Nim = input("Masukkan Nim: ")
if len(Nim) != 10:
    print("Invalid Nim")
elif not Nim.isdigit():
    print("Invalid Nim")
else:
    print("Valid, Intake Year 20"+Nim[0:2])