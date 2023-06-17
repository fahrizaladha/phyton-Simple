ujian = int (input("Berapa Nilai Ujian Anda: "))
tugas = int (input("Berapa Nilai Tugas Anda: "))
kehadiran = int(input("Berapa Kali Anda Hadir Kuliah: "))

if kehadiran >= 11:
    if ujian >= 80 and tugas >= 80:
        print("Anda Dinyatakan Lulus Mata Kuliah Logika Pemrograman dengan nilai A")
    elif ujian >= 80 and tugas >= 60:
        print("Anda Dinyatakan Lulus Mata Kuliah Logika Pemrograman dengan nilai B")
    elif ujian >= 60 and tugas >= 80:
        print("Anda Dinyatakan Lulus Mata Kuliah Logika Pemrograman dengan nilai B")
    elif ujian >= 60 and tugas >= 60:
        print("Anda Dinyatakan Lulus Mata Kuliah Logika Pemrograman dengan nilai C")
        
else:
    print("Anda Dinyatakan Tidak Lulus Mata Kuliah Logika Pemrograman")