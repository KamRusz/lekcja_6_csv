import csv
from sys import argv, exit
from os import listdir, path, getcwd


"""
class Parameters():
    def __init__ (self, sc_odczyt, sc_zapis, *zmiany)
        self.sc_odczyt
        self.sc_zapis
        self.
"""    

try:
    sciezka_odczyt = argv[1]
    sciezka_zapis = argv[2]
except IndexError:
    exit("nie podano argumentów")
    #print("nie podano argumentów")
    #sciezka_odczyt = None
    #sciezka_zapis = None
else:
    sciezka_odczyt = argv[1]
    sciezka_zapis = argv[2]

def odczyt_csv(sciezka):
    data = []
    with open(f"{sciezka}", "r", newline="") as plik:
        reader = csv.reader(plik, skipinitialspace=True, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data = list(reader)
    return data

try:
    print("lista plikow: ",listdir(sciezka_odczyt))
except FileNotFoundError:
    print("nie ma takiego katalogu")


print("czy sciezka istnieje: ",path.exists(argv[1]))
print("czy sciezka jest plikiem: ",path.isfile(argv[1]))
print("czy sciezka jest dir: ",path.isdir(argv[1]))
print("abs patch: ",path.abspath(sciezka_odczyt))

 
data = odczyt_csv("sn.csv")

#print(data)

if len(argv) > 3:
    zmiany = argv[3:]
    wspolrzedne=True 
    for x in range(len(zmiany)):
        zmiany[x] = zmiany[x].split(",")
        try:
            int(zmiany[x][0])
            int(zmiany[x][1])
        except:
            print(
                "podane współrzędne są nie prawidłowe - plik zapisany bez zmian"
            )
            wspolrzedne=False 

for zmiana in zmiany:
    if wspolrzedne:
        if len(data)<=int(zmiana[0]) or len(data[0])<=int(zmiana[1]):
            print(f"współrzedne [{zmiana[0]},{zmiana[1]}] poza zakresem pliku")
        else:
            data[int(zmiana[0])][int(zmiana[1])] = zmiana[2]

def zapis_csv(sciezka):
    with open(f"{sciezka}", "w", newline="") as plik:
        writer = csv.writer(plik)
        writer.writerows(data)

zapis_csv("sn2.csv")


#data2 = [['Game Number', 'Game Length'], ['1', '30,1'], ['2', '29'], ['3', '31'], ['4', '16'], ['5', '24'], ['6', '29'], ['7', '28'], ['8', '117'], ['9', '42'], ['10', '23']]