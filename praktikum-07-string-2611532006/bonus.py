kalimat = "Kasur ini rusak"
teks = kalimat.replace(" ", "").lower()
balik = teks[::-1]
if teks == balik:
    print("Palindrome")
else:
    print("Not a palindrome")


kalimat = "Algoritma"
teks = kalimat.replace(" ", "").lower()
balik = teks[::-1]
if teks == balik:
    print("Palindrome")
else:
    print("Not a palindrome")


kalimat = "malam ini malam"
teks = kalimat.replace(" ", "").lower()
balik = teks[::-1]
if teks == balik:
    print("Palindrome")
else:
    print("Not a palindrome")