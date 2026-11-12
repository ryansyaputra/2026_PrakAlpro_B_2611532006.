# Name: Ryan Syaputra
# NIM: 2611532006
# Question 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

full_name = "  Siti Aisyah  "
nim = "2610511023"
nama = full_name.strip()
posisi_spasi = nama.find(" ")
if posisi_spasi == -1:
    nama_depan = nama.lower()
else:
    nama_depan = nama[:posisi_spasi].lower()
username = nama_depan + nim[-3:]
print("Username:", username)


full_name = "Muhammad Rafi Pratama"
nim = "2610511023"
nama = full_name.strip()
posisi_spasi = nama.find(" ")
if posisi_spasi == -1:
    nama_depan = nama.lower()
else:
    nama_depan = nama[:posisi_spasi].lower()
username = nama_depan + nim[-3:]
print("Username:", username)


full_name = "Kartika"
nim = "2610511007"
nama = full_name.strip()
posisi_spasi = nama.find(" ")
if posisi_spasi == -1:
    nama_depan = nama.lower()
else:
    nama_depan = nama[:posisi_spasi].lower()
username = nama_depan + nim[-3:]
print("Username:", username)


full_name = "Ryan Syaputra"
nim = "2611532006"
nama = full_name.strip()
posisi_spasi = nama.find(" ")
if posisi_spasi == -1:
    nama_depan = nama.lower()
else:
    nama_depan = nama[:posisi_spasi].lower()
username = nama_depan + nim[-3:]
print("Username:", username)