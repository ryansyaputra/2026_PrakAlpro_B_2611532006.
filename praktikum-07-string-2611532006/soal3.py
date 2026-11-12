# Name: Ryan Syaputra
# NIM: 2611532006
# Question 3

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

text = "Algoritma dan Pemrograman"
count = 0
for char in text:
    if char in "Aaiueo":
        count += 1
print("Vowels:", count)

text = "Ryan Syaputra"
count = 0
for char in text:
    if char in "Aaiueo":
        count += 1
print("Vowels:", count)