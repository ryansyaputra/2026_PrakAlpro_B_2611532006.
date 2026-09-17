# TUGAS 2 PRAKTIKUM ALPRO 20206
print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_2006 = input("Masukkan Nama Mahasiswa:")
jenis_kelamin_2006 = input("Masukkan Jenis Kelamin (L/P):")
umur_2006 = int(input("Masukkan Umur:"))
skor_tes_2006 = float(input("Masukkan Skor Tes Awal:"))
print()
print("=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa  :", nama_2006, '|', "tipe:", type(nama_2006) )
print("Jenis Kelamin   :", jenis_kelamin_2006, '|', "tipe:", type(jenis_kelamin_2006) )
#========================================================================================
alamat_2006 = """
   Jalan Tenggiri
   Kec.Padang Utara
   Kota Padang """

print("Alamat Domisili :", alamat_2006, '|', "tipe:", type(alamat_2006) )
print("Umur            :", umur_2006, '|', "tipe:", type(umur_2006) )
print("Skor Tes Awal   :", skor_tes_2006, '|', "tipe:", type(skor_tes_2006) )
id_token_sinyal_2006 = 50 + 5j
print("ID Token Sinyal :", id_token_sinyal_2006, '|', "tipe:", type(id_token_sinyal_2006) )
print()
print("=== STATUS KELULUSAN PRAKTIKUM ===")
batas_lulus_2006 = 80.0
kelulusan_2006 = skor_tes_2006 >= batas_lulus_2006
print("Batas Minimum Nilai :", batas_lulus_2006)
print("Apakah Dinyatakan Lulus?:", kelulusan_2006, '|', "tipe:", type(kelulusan_2006) )


