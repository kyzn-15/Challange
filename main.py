import fisika
import fisika.JualBeli
import fisika.massajenis
import time

def batas():
    print("-"*30)

waktu_awal = time.time()

print(f"Massa jenis = {fisika.massajenis.MassaJenis(4, 2)}")
print(f"Massa = {fisika.massajenis.Massa(4, 2)}")

waktu_akhir = time.time()

print(f"waktu ayang dibutuhkan : {waktu_akhir - waktu_awal}")

batas()

print(f"Usaha = {fisika.U(5, 3)}")
print(f"Usaha = {fisika.G(5, 3)}")
print(f"Usaha = {fisika.J(5, 3)}")

batas()

print(f"hasil energi petensial {fisika.Ep(5, 3, 3)} ")

print(f"hasil energi kinenti {fisika.Ek(4, 2)}")

diskon_10 = fisika.jl(10)

print(f"diskon 10 = {diskon_10(10000)}")

