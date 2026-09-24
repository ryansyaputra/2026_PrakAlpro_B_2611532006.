# Buat file dengan nama if_elif_else1_2611532006.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_2006
# Program ini menggunakan fungsi input()

umur_2006 = int(input("Input umur anda: "))
sim_2006 = input("Apakah Anda Sudah Punya Sim C: ")[0]

if umur_2006 >= 17 and sim_2006 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")
elif umur_2006 >= 17 and sim_2006 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")
elif umur_2006 < 17 and sim_2006 == 'y':
    print("Anda Belum Cukup Umur punya SIM")
else:
    print("Anda Belum Cukup Umur dan tidak boleh bawa motor")

print("Program Selesai")