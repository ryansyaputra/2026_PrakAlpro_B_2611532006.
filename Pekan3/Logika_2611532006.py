# Buat file dengan nama Logika_2611532006.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_2006
# Program ini menggunakan funsgi input()
# Program operator logika dalam python

# Memasukkan bilai boolean
# Inout tidak oeka terhadap huruf besar dan kecil
a1_2006 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_2006 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 =", a1_2006)
print("A2 =", a2_2006)

# Konjungsi : bernilai True jika keduanya true
hasil_2006 = a1_2006 and a2_2006
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_2006)

# Disjungsi : bernilai True jika salah satunya true
hasil_2006 = a1_2006 and a2_2006
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_2006)

# Negasi A1 : membalik nilai A1
hasil_2006 = not a1_2006
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_2006)

# Negasi A2 : membalik nilai A2
hasil_2006 = not a2_2006
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_2006)

# XOR : bernilai True jika kedua nilai berbeda
hasil_2006 = a1_2006 != a2_2006
print("\nDisjungsi Ekslusif (XOR)")
print("A1 XOR A2 =", hasil_2006)