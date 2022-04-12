import sys
import subprocess
def install(paket):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', paket])
install("colorama")
from glob import glob
import os
import json
import shutil
from colorama import *
print(Fore.WHITE + Back.BLACK + "Willkommen im MC-Map-Detector!")
os.chdir('Minecraft-Map')
directroy = os.getcwd()
os.chdir('advancements')
result = glob('*.json')
result1 = result[-1]
database = str(result1)
data = json.loads(open(database).read())
DataVersion = data["DataVersion"]
if 100 <= DataVersion <= 168:
    print("Version = Snapshot")
elif DataVersion == 169:
    print("Version = 1.9")
elif 170 <= DataVersion <= 172:
    print("Version = Snapshot")
elif DataVersion == 175:
    print("Version = 1.9.1")
elif DataVersion == 176:
    print("Version = 1.9.2")
elif 177 <= DataVersion <= 182:
    print("Version = Snapshot")
elif DataVersion == 183:
    print("Version = 1.9.3")
elif DataVersion == 184:
    print("Version = 1.9.4")
elif 501 <= DataVersion <= 507:
    print("Version = Snapshot")
elif DataVersion == 510:
    print("Version = 1.10")
elif DataVersion == 511:
    print("Version = 1.10.1")
elif DataVersion == 512:
    print("Version = 1.10.2")
elif 800 <= DataVersion <= 818:
    print("Version = Snapshot")
elif DataVersion == 819:
    print("Version = 1.11")
elif DataVersion == 920:
    print("Version = Snapshot")
elif DataVersion == 921:
    print("Version = 1.11.1")
elif DataVersion == 922:
    print("Version = 1.11.2")
elif 1022 <= DataVersion <= 1138:
    print("Version = Snapshot")
elif DataVersion == 1139:
    print("Version = 1.12")
elif DataVersion == 1240:
    print("Version = Snapshot")
elif DataVersion == 1241:
    print("Version = 1.12.1")
elif 1341 <= DataVersion <= 1342:
    print("Version = Snapshot")
elif DataVersion == 1343:
    print("Version = 1.12.2")
elif 1444 <= DataVersion <= 1518:
    print("Version = Snapshot")
elif DataVersion == 1519:
    print("Version = 1.13")
elif 1620 <= DataVersion <= 1627:
    print("Version = Snapshot")
elif DataVersion == 1628:
    print("Version = 1.13.1")
elif DataVersion == 1631:
    print("Version = 1.13.1")
elif 1901 <= DataVersion <= 1951:
    print("Version = Snapshot")
elif DataVersion == 1952:
    print("Version = 1.14")
elif DataVersion == 1957:
    print("Version = 1.14.1")
elif DataVersion == 1963:
    print("Version = 1.14.2")
elif DataVersion == 1968:
    print("Version = 1.14.3")
elif DataVersion == 1976:
    print("Version = 1.14.4")
elif 2067 <= DataVersion <= 2224:
    print("Version = Snapshot")
elif DataVersion == 2225:
    print("Version = 1.15")
elif DataVersion == 2227:
    print("Version = 1.15.1")
elif DataVersion == 2230:
    print("Version = 1.15.2")
elif 2320 <= DataVersion <= 2565:
    print("Version = Snapshot")
elif DataVersion == 2566:
    print("Version = 1.16")
elif DataVersion == 2567:
    print("Version = 1.16.1")
elif DataVersion == 2578:
    print("Version = 1.16.2")
elif DataVersion == 2580:
    print("Version = 1.16.3")
elif DataVersion == 2584:
    print("Version = 1.16.4")
elif DataVersion == 2586:
    print("Version = 1.16.5")
elif 2701 <= DataVersion <= 2723:
    print("Version = Snapshot")
elif DataVersion == 2724:
    print("Version = 1.17")
elif DataVersion == 2730:
    print("Version = 1.17.1")
elif 2825 <= DataVersion <= 2859:
    print("Version = Snapshot")
elif DataVersion == 2860:
    print("Version = 1.18")
elif DataVersion == 2865:
    print("Version = 1.18.1")
elif DataVersion == 2975:
    print("Version = 1.18.2")
print(Fore.WHITE + Back.BLACK + "Map wird in Minecraft verschoben!")
try:
    os.chdir(directroy)
    original = os.getcwd()
    target = os.getenv('APPDATA') + "\.minecraft\saves"
    shutil.move(original, target)
except PermissionError:
    pass
