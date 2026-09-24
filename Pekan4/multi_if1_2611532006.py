# Buat file dengan nama multi_if1_2611532006.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_2006
# Program ini menggunakan fungsi input()

umur_2006 = int(input("Input umur anda: "))
sim_2006 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_2006 >= 17 and sim_2006 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_2006 >= 17 and sim_2006 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_2006 < 17 and sim_2006 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

if umur_2006 < 17 and sim_2006 != 'y':
    print("Anda Belum Cukup Umur bawa motor")