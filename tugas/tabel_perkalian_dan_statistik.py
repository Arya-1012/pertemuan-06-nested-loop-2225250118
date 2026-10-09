# Program Tabel Perkalian dan Statistik

n = int(input("Masukkan ukuran tabel perkalian: "))

total = 0
jumlah_data = 0

print("\nTabel Perkalian:")

for i in range(1, n + 1):
    for j in range(1, n + 1):
        hasil = i * j

        print(f"{hasil:4}", end="")

        total += hasil
        jumlah_data += 1

    print()

if jumlah_data > 0:
    rata_rata = total / jumlah_data

    print("\nStatistik Tabel Perkalian")
    print("Jumlah seluruh hasil:", total)
    print("Banyak data:", jumlah_data)
    print("Rata-rata:", rata_rata)