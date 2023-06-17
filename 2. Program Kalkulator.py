print('Pilih operasi')
print('1.Penjumlahan')
print('2.Pengurangan')
print('3.Perkalian')
print('4.Pembagian')

print('Inputan pilihan operasi(1/2/3/4)?')

operasi = int(input('Pilih Operasi:'))
nilai1 = float(input('Nilai Pertama:'))
nilai2 = float(input('Nilai Kedua:'))

if operasi == 1:
    print(nilai1 + nilai2)
elif operasi == 2:
    print(nilai1 - nilai2)
elif operasi == 3:
    print(nilai1 * nilai2)
elif operasi == 4:
    print(nilai1 / nilai2)
else:
    print('Tidak Ada Oprasi')  