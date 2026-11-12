# Name: Ryan Syaputra
# NIM: 2611532006
# Question 7

name = "ryan syaputra"
nim = "2611532006"

posisi_spasi = name.find(" ")
if posisi_spasi == -1:
    nama_depan = name.lower()
else:
    nama_depan = name[:posisi_spasi].lower()
username = nama_depan + nim[-3:]
intake = "20"+nim[0:2]

print("=" * 30)
print(f"{'STUDENT CARD':^30}")
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)
