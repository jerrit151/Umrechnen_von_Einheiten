
while 1==1:

    #Programmierung Menüauswahl
    print ("1: Umrechnung Bar in Pascal\n")
    print ("2: Meter pro Sekunde in Kilometer pro Stunde\n")
    print ("3: Kilometer in Meilen\n")
    print ("4: Grad Celsius in  Grad Fahrenheit\n")
    print ("5: Zentimeter in Zoll\n")
    print ("6: Abbruch der Umrechnung")
    eingabe = input ("Welche Einheit darf ich für dich umrechnen: ")
    

    if eingabe == '1':
        #Druck (Bar in Pascal)
        #Abfrage welcher Wert umgewandelt werden soll
        bar = float(input("Gib die Zahl in Bar ein: "))
        urf_bar_pa = 100000
        #Rechnung
        pascal = bar * urf_bar_pa
        #Ausgabe des Ergebnis
        print("Die Umrechnung von", bar, "bar in", "pascal", "ist:", pascal, "pascal");

    if eingabe == '2':
        #Strecke (Meter pro Sekunde in Kilometer pro Stunde)
        #Abfrage welcher Wert umgewandelt werden soll
        m_s = float(input("Gib die Zahl in Meter pro Sekunde ein: "))
        urf_ms_kmh = 3.6
        #Rechnung
        kmh = m_s * urf_ms_kmh
        #Ausgabe des Ergebnis
        print("Die Umrechnung von", m_s, "meter pro sekunde in", "Kilometer pro Stunde", "ist:", kmh, "Kilometer pro Stunde")
         
    if eingabe == '3':
        #Strecke (Kilometer in Meilen)
        #Abfrage welcher Wert umgewandelt werden soll
        km = float(input("Gib die Zahl in Kilometer ein: "))
        urf_km_mi = 1.609
        #Rechnung
        mi = km / urf_km_mi
        #Ausgabe des Ergebnis
        print("Die Umrechnung von", km, "Kilometer in", "Meilen", "ist:", mi, "Meilen")

    if eingabe == '4':
        #Temperatur (Grad Celsius in Fahrenheit)
        #Abfrage welcher Wert umgewandelt werden soll
        tc = float(input("Gib die Zahl in Grad Celsius ein: "))
        #urf_tc_tf = 1.8 + 32
        #Rechnung
        tf = (tc * 1.8) + 32
        #Ausgabe des Ergebnis
        print("Die Umrechnung von", tc, "Grad Celsius in", "Grad Fahrenheit", "ist:", tf, "Grad Fahrenheit")

    if eingabe == '5':
        #Größe (Zentimeter in Zoll)
        #Abfrage welcher Wert umgewandelt werden soll
        cm = float(input("Gib die Zahl in Zentimeter ein: "))
        urf_cm_zoll = 2.54
        #Rechnung
        zoll = cm / urf_cm_zoll
        #Ausgabe des Ergebnis
        print("Die Umrechnung von", cm, "Zentimeter in", "Zoll", "ist:", zoll, "Zoll")
     
    if eingabe == '6':
        print("Die Umrechnung wird abgebrochen, bitte starten Sie erneut")
        
