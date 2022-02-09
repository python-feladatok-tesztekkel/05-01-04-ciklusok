# feladat.py
# Minden feladatra készítsen legalább három tesztet

# 1. feladat
# Készítsen függvényt faktorialis néven
# A függvénynek bemeneti paramétere egy egész szám
# Ha a szám nulla, akkor térjen vissza egyel
# Ha a szám (n) nullánál nagyob, akkor térjen vissza az n! értékével
# Ha a szám negatív térjen vissza a None eredménnyel
def faktorialis(n:int) -> int:
    if n > 0:
        szorzat = 1
        for i in range(1, n+1):
            szorzat = szorzat*i
        return szorzat
    elif n==0:
      return 1
    else:
         return None

# 2. feladat
# Írjon függvényt ketto_hatvany néven
# A függvény bemeti paramétere a kitevő
# Ha a kitevő az egy, akkor a visszatérési érték legyen a kitte kitevőedik hatványa
# Ha a kitevő nulla, akkor a visszatérési érték legyen egy
# Más kitevő esetén a visszatérési érték legyen nulla

def ketto_hatvany(kitevo:int)->int:
    if (kitevo>=0):
        szorzat = 1
        for i in range(1,kitevo+1):
            szorzat = szorzat * 2
        return szorzat
    else:
        return None

# 3. feladat
# Készítsen függvényt szorzat_es_osszeg néven
# A függvény n bemeneti paraméter esetén határozza meg a következő összeget: 1·1 + 2·2 + 3·3 + 4·4 + ... + n·n
# n<1 esetén a visszatérési érték legyen None

def szorzat_es_osszeg(n:int)->int:
    if n>0:
        szum = 0
        for i in range(1,n+1):
            szum = szum+(i*i)
        return szum
    else:
        return None

# 4. feladat
# Készítsen függvényt szorzat_osszeg néven
# A függvény n bemeneti paraméter esetén határozza meg a következő összeget: 1·2 + 2·3 + 3·4 + 4·5 + ... + n·(n+1)
# n<1 esetén a visszatérési érték legyen None

def szorzat_osszeg(n:int)->int:
    if n>0:
        szum = 0
        for i in range(1,n+1):
            szum = szum+(i*(i+1))
        return szum
    else:
        return None


# 5. feladat
# Írjon függvényt osztok_szama neven
# A függvény bemeneti paramétere egy szám
# Határozza meg, hogy a számnak hány osztója van
# Ha a paraméter nulla vagy annál kisebb akkor térjen vissza a None értékkel

def osztok_szama(n:int)->int:
    if n < 1:
        return None
    else:
        db = 0
        for i in range(1,n+1):
            if (n % i) == 0:
                db = db + 1
        return db

# 6. feladat
# Egy szám primszám, ha önmagán és egyen kívül más osztója nincs
# Írjon függvényt primszam_e neven
# A függvény bemeneti paramétere egy szám, amelyről meg kell állapítani, hogy primszám-e
# Ha a paraméter egy vagy annál kisebb akkor térjen vissza a None értékkel

def primszam_e(n:int)->bool:
    if n < 2:
        return None
    else:
        db = 0
        for i in range (1,n+1):
            if (n % i) == 0:
                db = db + 1
        if db == 2:
            return True
        else:
            return False




