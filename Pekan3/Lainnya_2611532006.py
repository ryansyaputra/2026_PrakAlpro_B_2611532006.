# Buat file dengan nama Lainnya_2611532006.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_2006
# Program ini menggunakan funsgi input()
# Program operator keanggotaan dan identitas dalam python

print("==============================")
print("1. OPERATOR KEANGGOTAAN")
print("==============================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2006 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2006 = [int(angka.strip()) for angka in input_data_2006.split(",")]

nilai_dicari_2006 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil = nilai_dicari_2006 in data_2006
print("\nOperator keanggotaan IN")
print(nilai_dicari_2006, "in", data_2006, "=", hasil)

# Operator not in
hasil = nilai_dicari_2006 not in data_2006
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2006, "not in", data_2006, "=", hasil)

print("\n================================")
print("2. OPERATOR IDENTITAS")
print("================================")

# objek1 menggunakan list dari input pengguna
objek1_2006 = data_2006

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2006 = objek1_2006

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2006 = data_2006.copy()

print("objek1 =", objek1_2006)
print("objek2 =", objek2_2006)
print("objek3 =", objek3_2006)

# Operator is
hasil = objek1_2006 is objek2_2006
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil)

# Operator is not
hasil = objek1_2006 is not objek3_2006
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_2006 is objek3_2006)
print("objek1 == objek3 =", objek1_2006 == objek3_2006)