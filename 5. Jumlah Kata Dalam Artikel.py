isi_artikel = 'Apakah Anda masih semangat? Semangat merupakan separuh jalan menuju kesuksesan. Kesuksesan tidak ditentukan hanya oleh bakat / kemampuan. Bakat / kemampuan terkadang menjadi tidak berguna jika tidak memiliki semangat. Jadi, tetap semangat menjalani hari ini!'
tanda_baca = [",", ".", "/"]

def hapus_tandabaca(word):
    temp = ""
    for w in word:
        hapus = False 
        i = 0
        while (i<len(tanda_baca) and (not hapus)):
            if (w==tanda_baca[i]):
                hapus = True
            else:
                i = i + 1 
        if not hapus:
            temp = temp + w
    return temp

tanpa_tandabaca=hapus_tandabaca(isi_artikel)

l = tanpa_tandabaca.split()

jumlah=len(l)

print(isi_artikel)
print(tanpa_tandabaca)
print(l)
print(jumlah)

if jumlah <= 40:
    print("Anda Lolos Tahap Verifikasi")

else:
    print("Anda Tidak Lolos Tahap Verifikasi")