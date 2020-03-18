#1
class Pesan(object):
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimatku memiliki', len(self.teks), 'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru

#a
    def apakahTerkandung(self, a):
        if a in self.teks:
            return True
        else :
            return False
#b
    def hitungKonsonan(self):
        kon = 0
        x = self.teks
        alfaKon = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        for i in x:
            if i in alfaKon:
                kon += 1
        return kon
#c
    def hitungVokal(self):
        voc = 0
        x = self.teks
        alfaVoc = "aiueoAIUEO"
        for i in x:
            if i in alfaVoc:
                voc += 1
        return voc
