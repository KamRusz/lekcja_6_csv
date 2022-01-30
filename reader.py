import csv
from sys import argv, exit
from os import listdir, path, getcwd

try:
    sciezka_odczyt = argv[1]
    sciezka_zapis = argv[2]
except IndexError:
    exit("nie podano argumentów")

else:
    sciezka_odczyt = argv[1]
    sciezka_zapis = argv[2]

def odczyt_csv(sciezka):
    data = []
    with open(f"{sciezka}", "r", newline="") as plik:
        reader = csv.reader(plik, skipinitialspace=True, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data = list(reader)
    return data

if path.exists(sciezka_odczyt):
    if path.isfile(sciezka_odczyt):
        pass
    else:
        quit(
            "\nścieżka odczytu nie jest plikiem!\nPoniżej lista plików z katalogu"
            f" [{path.abspath(sciezka_odczyt)}]:\n{listdir(sciezka_odczyt)}\n"
            )
else:
    quit("ścieżka odczytu nie istnieje")

if not path.isfile(sciezka_zapis):
    if path.isdir(path.abspath(sciezka_zapis)):
        quit("\nnie podano nazwy pliku do zapisu\n")
 
data = odczyt_csv(sciezka_odczyt)

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

zapis_csv(sciezka_zapis)