# Matriks A dan B berukuran 5x5
A = [
    [3, 5, 7, 9, 11],
    [2, 4, 6, 8, 10],
    [1, 3, 5, 7, 9],
    [9, 7, 5, 3, 1],
    [10, 8, 6, 4, 2]
]

B = [
    [2, 1, 3, 0, 4],
    [0, 2, 1, 3, 1],
    [1, 0, 2, 1, 0],
    [3, 1, 0, 2, 1],
    [0, 4, 1, 0, 3]
]

# Inisialisasi matriks hasil sebagai matriks kosong
hasil = []

# Perkalian matriks
for i in range(5):
    baris = []  # baris untuk hasil[i]
    for j in range(5):
        total = 0
        for k in range(5):
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)

# Menampilkan hasil
print("Hasil perkalian matriks A x B:")
for row in hasil:
    print(row)
