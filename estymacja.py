import math
import scipy.stats as st


class SzeregPunktowy:
    def przedzial_ufnosci_srednia(self):
        pass
        """Rozklad t-Studenta"""
        # print('Podaj wsp. ufnosci 1-a')
        # wsp_ufnosci = float(input())
        # a = 1 - wsp_ufnosci
        # ta = st.t.ppf(a, self.ilosc - 1)
        # print(ta)
        # f = self.srednia - ta * self.odch_standardowe / math.sqrt(self.ilosc - 1)
        # s = self.srednia + ta * self.odch_standardowe / math.sqrt(self.ilosc - 1)
        # print('P({0} < {1} < {2}) = {3}'.format(f, self.srednia, s, wsp_ufnosci))
        # return f, s

# ---------------------------------------

class SzeregPrzedzialowy:
    def __init__(self, data):
        self.data = data
        self.ilosc = self.ilosc()
        self.srednia = self.srednia()
        self.wariancja = self.wariancja()
        self.odch_standardowe = math.sqrt(self.wariancja)
        self.mediana = self.mediana()
        self.moda = self.moda()

    def ilosc(self):
        i = 0
        for line in self.data:
            i += line[2]
        return i

    def srednia(self):
        a = 0
        for line in self.data:
            s, e, n = line
            a += (s + e) / 2 * n
        return a / self.ilosc

    def wariancja(self):
        a = 0
        for line in self.data:
            s, e, n = line
            a += ((s + e) / 2 - self.srednia) ** 2 * n
        return a / self.ilosc

    def __liczebnosci_skumulowane(self):
        l = 0
        for i, line in enumerate(self.data):
            l += line[2]
            self.data[i].append(l)

    def mediana(self):
        self.__liczebnosci_skumulowane()
        s = 0
        e = 0
        n = 0
        sk = 0
        poz_mediany = (self.ilosc + 1) / 2
        for i, line in enumerate(self.data):
            if poz_mediany <= line[3]:
                s, e, n = line[0:3]
                sk = data[i - 1][3]
                break
        h = e - s
        mediana = s + (poz_mediany - sk) * (h / n)
        # DEBUG
        # print('Med:' + str(s) + ' + (' + str(poz_mediany) + ' - ' + str(sk) + ') * (' + str(h) + ' / ' + str(n) + ') ')
        return mediana

    def moda(self):
        s = 0
        e = 0
        n = 0
        np1 = 0
        nm1 = 0
        for i, line in enumerate(self.data):
            if line[2] > n:
                s, e, n = line[0:3]
                nm1 = data[i - 1][2]
                np1 = data[i + 1][2]
        h = e - s
        moda = s + ((n - nm1) / ((n - nm1) + (n - np1))) * h
        return moda

    def przedzial_ufnosci_srednia(self):
        """Rozklad Normalny"""
        print('Podaj wsp. ufnosci 1-a')
        wsp_ufnosci = float(input())
        a = 1 - wsp_ufnosci
        qua = 1 - a / 2
        ua = st.norm.ppf(qua)
        f = self.srednia - ua * self.odch_standardowe / math.sqrt(self.ilosc)
        s = self.srednia + ua * self.odch_standardowe / math.sqrt(self.ilosc)
        print('P({0} < {1} < {2}) = {3}'.format(f, self.srednia, s, wsp_ufnosci))
        return f, s

    def przedzial_ufnosci_odchylenie(self):
        pass

# ---------------------------------------

def get_data():
    data = list()
    while True:
        a = [int(x) for x in input().split()]
        if (a[0] == 0 and len(a) == 1):
            break
        else:
            data.append(a)
    return data


# na przykład [[2, 4, 1], [4, 6, 112], [6, 8, 76]]

# ---------------------------------------


data = get_data()
szereg1 = SzeregPrzedzialowy(data)

print('----------------------------------------')
print(f'Liczba danych: {szereg1.ilosc}')
print(f'Średnia: {szereg1.srednia}')
print(f'Wariancja: {szereg1.wariancja}')
print(f'Odchylenie standardowe: {szereg1.odch_standardowe}')
print(f'Mediana: {szereg1.mediana}')
print(f'Moda: {szereg1.moda}')
print('----------------------------------------')
print(szereg1.przedzial_ufnosci_srednia())
