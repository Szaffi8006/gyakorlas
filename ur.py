# Megoldás függvényekkel
# Nagy János, 15m, 2023-10-21
from urhajo import Urhajo

print('Nagy János, 15m 2023-10-21')

urhajoLista = []

def beolvas():

    fp = open('urhajok.csv', 'r', encoding='utf-8')
    lines = fp.readlines()
    
    for line in lines:
        # jobbról sortörés törölve:
        line = line.rstrip()
        
        # egy sor feldarabolása
        az, tipus, hatotav, index, letszam, ar = line.split(';')
        
        # urhajo objektumo létrehozása
        urhajo = Urhajo(int(az), tipus, int(hatotav), int(index), int(letszam), float(ar))
        
        # Hozzáfűzzük az urhajo objektumot a listához:
        urhajoLista.append(urhajo)
        
        #print(urhajo.ar)
        
    fp.close()


def ki_haromfos():
    darab = 0
    for urhajo in urhajoLista:
        if urhajo.letszam == 3 :
            # print(urhajo.letszam)
            #darab += 1
            darab = darab + 1
        
    print('Háromfős:', darab)

def ki_atlagos_hatotav():
    osszeg = 0
    for urhajo in urhajoLista:
        osszeg = osszeg + urhajo.hatotav
    darab = len(urhajoLista)
    atlag = osszeg / darab
    print('Átlag: %.3f' % atlag)

def fajlba_haromfos_adat():
    
    fp = open('harmas.txt', 'w', encoding='utf-8')
    
    for urhajo in urhajoLista:
        if urhajo.letszam == 3 :
            fp.write(str(urhajo.az))
            fp.write(':')
            fp.write(str(urhajo.tipus))
            fp.write(':')
            fp.write(str(urhajo.hatotav))
            fp.write(':')
            fp.write(str(urhajo.index))
            fp.write(':')
            fp.write(str(urhajo.letszam))
            fp.write(':')
            fp.write(str(urhajo.ar))            
            fp.write('\n')
        
    fp.close()

beolvas()
ki_haromfos()
ki_atlagos_hatotav()
fajlba_haromfos_adat()
