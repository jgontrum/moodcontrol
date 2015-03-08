import AufnahmeundVerarbeitung
# Analysiere eine gerade aufgenommene Datei
# also berechne den Integral etc. (mit AufnahmeundVerarbeitung.py)
# und vergleiche es mit dem Profil

# Für Aline: Alle Werte aus der Tabelle auslesen
# Aggro: Wenn Integral größer 30
# Normal: Wenn Integral zwischen 0 und 29
# Müde: Wenn Integral kleiner 0

# ggf. Profile für alle anlegen :D

# neu aufgenommene Datei mit Profil vergleichen
# und richtige Stimmung zurückgeben!

def profil(name):
    score = AufnahmeundVerarbeitung.analyse()
    if name == "Aline":
        if score >= 30.0 or score < -2.0:
            return "aggro"
        elif score < 30 and score > 0:
            return "normal"
        elif score < 0.0 and score > -2.0:
            return "tired
        else:
            return "Whaaaattt"

auswertung = profil("Aline")
print auswertung

