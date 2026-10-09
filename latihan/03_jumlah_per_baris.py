# Program Menghitung Jumlah per Baris

matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matriks)):
    jumlah = 0

    for j in range(len(matriks[i])):
        jumlah += matriks[i][j]

    print(f"Jumlah baris {i + 1}: {jumlah}")