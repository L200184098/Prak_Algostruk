class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.tempatTinggal = kota
        self.uangSaku = uangsaku

m0 = Mahasiswa("Jono", 123, "Sragen", 240000)
m1 = Mahasiswa("Andi", 154, "Yogyakarta", 230000)
m2 = Mahasiswa("Jordi", 108, "Surakarta", 230000)
m3 = Mahasiswa("Lala", 140, "Surakarta", 235000)
m4 = Mahasiswa("Putri", 113, "Boyolali", 240000)
m5 = Mahasiswa("Raihan", 132, "Semarang", 250000)
m6 = Mahasiswa("Janis", 186, "Klaten", 245000)
m7 = Mahasiswa("Nanda", 199, "Wonogiri", 245000)
m8 = Mahasiswa("Putantri", 187, "Klaten", 245000)
m9 = Mahasiswa("Hardi", 153, "Karanganyar", 270000)
m10 = Mahasiswa("Maya", 148, "Purwodadi", 265000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

def binSeMass(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [2, 4, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
print(binSeMass(kumpulan, 6))
