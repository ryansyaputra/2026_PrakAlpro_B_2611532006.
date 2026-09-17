# Buat file dengan nama assignment_2611532006.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka_2006
# Program ini menggunakan funsgi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam python

angka1_2006 = int(input("Input angka-1: "))
angka2_2006 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_2006)
print("Nilai angka2 =", angka2_2006)

# Assignment biasa
hasil_2006 = angka1_2006
print("\nAssignment biasa (=)")
print("hasil =", hasil_2006)

# Assignment penambahan
hasil_2006 = angka1_2006
hasil_2006 += angka2_2006
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_2006)

# Assignment pengurangan
hasil_2006 = angka1_2006
hasil_2006 -= angka2_2006
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_2006)

# Assignment perkalian 
hasil_2006 = angka1_2006
hasil_2006 *= angka2_2006
print("\nAssignment perkalian (*=)")
print("hasil =", hasil_2006)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2006 != 0:
    hasil_2006 = angka1_2006
    hasil_2006 /= angka2_2006
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_2006)
    # Operator tambahan
    hasil_2006 = angka1_2006
    hasil_2006 //= angka2_2006
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_2006)
    hasil_2006 = angka1_2006
    hasil_2006 %= angka2_2006
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_2006)
else:
    print("\nPembagian tidak dapat dilakukan.")    
    print("Angka kedua tidak boleh bernilai 0")

# Operator tambahan: assignment perpangkatan
hasil_2006 = angka1_2006
hasil_2006 **= angka2_2006
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_2006)