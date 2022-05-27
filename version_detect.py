def version():
    from glob import glob
    import json
    result = glob('*.json')
    result1 = result[-1]
    database = str(result1)
    data = json.loads(open(database).read())
    DataVersion = data["DataVersion"]
    if 100 <= DataVersion <= 168:
        mc_version = "Snapshot"
    elif DataVersion == 169:
        mc_version = "1.9"
    elif 170 <= DataVersion <= 172:
        mc_version = "Snapshot"
    elif DataVersion == 175:
        mc_version = "1.9.1"
    elif DataVersion == 176:
        mc_version = "1.9.2"
    elif 177 <= DataVersion <= 182:
        mc_version = "Snapshot"
    elif DataVersion == 183:
        mc_version = "1.9.3"
    elif DataVersion == 184:
        mc_version = "1.9.4"
    elif 501 <= DataVersion <= 507:
        mc_version = "Snapshot"
    elif DataVersion == 510:
        mc_version = "1.10"
    elif DataVersion == 511:
        mc_version = "1.10.1"
    elif DataVersion == 512:
        mc_version = "1.10.2"
    elif 800 <= DataVersion <= 818:
        mc_version = "Snapshot"
    elif DataVersion == 819:
        mc_version = "1.11"
    elif DataVersion == 920:
        mc_version = "Snapshot"
    elif DataVersion == 921:
        mc_version = "1.11.1"
    elif DataVersion == 922:
        mc_version = "1.11.2"
    elif 1022 <= DataVersion <= 1138:
        mc_version = "Snapshot"
    elif DataVersion == 1139:
        mc_version = "1.12"
    elif DataVersion == 1240:
        mc_version = "Snapshot"
    elif DataVersion == 1241:
        mc_version = "1.12.1"
    elif 1341 <= DataVersion <= 1342:
        mc_version = "Snapshot"
    elif DataVersion == 1343:
        mc_version = "1.12.2"
    elif 1444 <= DataVersion <= 1518:
        mc_version = "Snapshot"
    elif DataVersion == 1519:
        mc_version = "1.13"
    elif 1620 <= DataVersion <= 1627:
        mc_version = "Snapshot"
    elif DataVersion == 1628:
        mc_version = "1.13.1"
    elif DataVersion == 1631:
        mc_version = "1.13.2"
    elif 1901 <= DataVersion <= 1951:
        mc_version = "Snapshot"
    elif DataVersion == 1952:
        mc_version = "1.14"
    elif DataVersion == 1957:
        mc_version = "1.14.1"
    elif DataVersion == 1963:
        mc_version = "1.14.2"
    elif DataVersion == 1968:
        mc_version = "1.14.3"
    elif DataVersion == 1976:
        mc_version = "1.14.4"
    elif 2067 <= DataVersion <= 2224:
        mc_version = "Snapshot"
    elif DataVersion == 2225:
        mc_version = "1.15"
    elif DataVersion == 2227:
        mc_version = "1.15.1"
    elif DataVersion == 2230:
        mc_version = "1.15.2"
    elif 2320 <= DataVersion <= 2565:
        mc_version = "Snapshot"
    elif DataVersion == 2566:
        mc_version = "1.16"
    elif DataVersion == 2567:
        mc_version = "1.16.1"
    elif DataVersion == 2578:
        mc_version = "1.16.2"
    elif DataVersion == 2580:
        mc_version = "1.16.3"
    elif DataVersion == 2584:
        mc_version = "1.16.4"
    elif DataVersion == 2586:
        mc_version = "1.16.5"
    elif 2701 <= DataVersion <= 2723:
        mc_version = "Snapshot"
    elif DataVersion == 2724:
        mc_version = "1.17"
    elif DataVersion == 2730:
        mc_version = "1.17.1"
    elif 2825 <= DataVersion <= 2859:
        mc_version = "Snapshot"
    elif DataVersion == 2860:
        mc_version = "1.18"
    elif DataVersion == 2865:
        mc_version = "1.18.1"
    elif DataVersion == 2975:
        mc_version = "1.18.2"
    if mc_version == "Snapshot":
        quit(1)
    return mc_version
