import csv
from sys import argv

try:
    sciezka_odczyt = argv[1]
    sciezka_zapis = argv[2]
    zmiany = argv[3:]
except IndexError:
    print("nie podano argumentów")
    sciezka_odczyt = None
    sciezka_zapis = None
    zmiany = []
else:
    sciezka_odczyt = argv[1]
    sciezka_zapis = argv[2]
    zmiany = argv[3:]

class Parameters():
    def __init__ (self, sc_odczyt, sc_zapis, *zmiany)
        self.sc_odczyt
    

print("in = ",sciezka_odczyt)
print("out = ",sciezka_zapis)
print(zmiany)
print("zmiana 1 = ", zmiany[0])
print("zmiana 1 = ", zmiany[0].split(","))



def odczyt_csv(sciezka):
    data = []
    with open(f"{sciezka}", "r", newline="") as plik:
        reader = csv.reader(plik, skipinitialspace=True, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data = list(reader)
    return data
    

data = odczyt_csv("sn.csv")
data2 = [['Game Number', 'Game Length'], ['1', '30,1'], ['2', '29'], ['3', '31'], ['4', '16'], ['5', '24'], ['6', '29'], ['7', '28'], ['8', '117'], ['9', '42'], ['10', '23']]


def zapis_csv(sciezka):
    with open(f"{sciezka}", "w", newline="") as plik:
        writer = csv.writer(plik)
        writer.writerows(data2)
zapis_csv("sn2.csv")