# 📘 Perkalian Matriks 5x5 di Python

Program ini melakukan **perkalian dua matriks 5x5** Matriks dikalikan menggunakan perulangan `for` dan disimpan menggunakan `append`.

---

## 🧮 Matriks Input

### Matriks A:

```
|  3   5    7   9  11  |
|  2   4    6   8  10  |
|  1   3    5   7   9  |
|  9   7    5   3   1  |
|  10  8    6   4   2  |
```

### Matriks B:

```
| 2  1  3  0  4 |
| 0  2  1  3  1 |
| 1  0  2  1  0 |
| 3  1  0  2  1 |   
| 0  4  1  0  3 |
```

---

## 🔧 Cara Kerja Kode

### Inisialisasi Matrix

```python
hasil = []
```

### Penjelasan:

- Melakukan Inisalisasi untuk hasil dari matriks

---

### Perhitungan Kali Dalam Matrix

```python
hasil = []  # Matriks hasil kosong

for i in range(5):         # Untuk setiap baris di A
    baris = []
    for j in range(5):     # Untuk setiap kolom di B
        total = 0
        for k in range(5): # Perkalian elemen baris A dengan kolom B
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)
```

### Penjelasan:

- Mengambil **baris ke-i dari A** dan **kolom ke-j dari B**.
- Mengalikan elemen yang bersesuaian lalu menjumlahkannya.
- Hasilnya adalah elemen `[i][j]` pada matriks `hasil`.

---

### Menampilkan Hasil

```python
print("Hasil perkalian matriks A x B:")
for row in hasil:
    print(row)
```

### Penjelasan:

- Menampilkan Output dari hasil perkalian matriks

---

## ✅ Contoh Perhitungan Elemen `hasil[0][0]`

Baris pertama A: `[3, 5, 7, 9, 11]`  
Kolom pertama B: `[0, 2, 1, 3, 1]`

```
= 3×2 + 5×0 + 7×1 + 9×3 + 11×0
= 6 + 0 + 7 + 27 + 0
= 40
```

---

## 📊 Matriks Hasil

Hasil dari `A x B` adalah:

```
[40, 66, 39, 40, 59]
[34, 58, 32, 34, 50]
[28, 50, 25, 28, 41]
[32, 30, 45, 32, 49]
[38, 38, 52, 38, 58]
```

---

## 🔍 Ringkasan

- Tidak menggunakan library eksternal seperti `numpy`.
- Operasi dilakukan sepenuhnya dengan nested loops dan list native Python.
- Cocok untuk pembelajaran dasar matriks dan algoritma perkalian manual.
