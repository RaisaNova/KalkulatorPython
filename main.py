angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("\nPilih operasi:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")
print("5. Sisa Pembagian (modulus %)")

pilihan = input("Masukkan pilihan (1/2/3/4/5): ")


if pilihan == "1":
    hasil = angka1 + angka2
    operasi = "+"
elif pilihan == "2":
    hasil = angka1 - angka2
    operasi = "-"
elif pilihan == "3":
    hasil = angka1 * angka2
    operasi = "*"
elif pilihan == "4":
    if angka2 != 0:
        hasil = angka1 / angka2
        operasi = "/"
    else:
        print("Error: Tidak bisa membagi dengan 0!")
        exit()
elif pilihan == "5":
    if angka2 != 0:
        hasil = angka1 % angka2
        operasi = "%"
    else:
        print("Error: Tidak bisa modulus dengan 0!")
        exit()
else:
    print("Pilihan tidak valid!")
    exit()
