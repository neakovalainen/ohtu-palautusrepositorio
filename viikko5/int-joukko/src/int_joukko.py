KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            pass
        elif type(kapasiteetti) is not int or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D

        self.kapasiteetti = kapasiteetti or KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko or OLETUSKASVATUS

        self.lista = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.lista

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False
        
        self.lista[self.alkioiden_lkm] = luku
        self.alkioiden_lkm = self.alkioiden_lkm + 1

        if self.alkioiden_lkm == 1:
            return True

        # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
        if self.alkioiden_lkm % len(self.lista) == 0:
            lista_old = self.to_int_list()
            self.lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(lista_old, self.lista)

        return True

    def poista(self, luku):
        try:
            kohta = self.lista.index(luku)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            self.lista = self.lista[:kohta] + self.lista[kohta + 1:] + [0]

            return True
        except ValueError: # lukua ei ole listassa
            return False

    def kopioi_lista(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        lista = self._luo_lista(self.alkioiden_lkm)

        for i in range(len(lista)):
            lista[i] = self.lista[i]

        return lista

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        lista_a = a.to_int_list()
        lista_b = b.to_int_list()

        [joukko.lisaa(luku) for luku in lista_a]
        [joukko.lisaa(luku) for luku in lista_b]

        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        lista_a = a.to_int_list()
        lista_b = b.to_int_list()

        [joukko.lisaa(luku) for luku in lista_a if luku in lista_b]

        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        lista_a = a.to_int_list()
        lista_b = b.to_int_list()

        [joukko.lisaa(luku) for luku in lista_a if luku not in lista_b]

        return joukko

    def __str__(self):
        return f"{{{ ', '.join([str(luku) for luku in self.lista[:self.alkioiden_lkm]]) }}}"
