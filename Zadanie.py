from math import fabs

def setTemperatureClosestToZero(values):
    A = values[0]
    closest = []

    for i in values:
        if i==0:                                    #jeśli wartość równa 0
            A = 0                                   #zmienna równa 0
            break                                   #przerywamy pętle
        elif fabs(i)<fabs(A):                       #jeśli wartość bezwzględna z i jest niższa niż wartość bezwględna obecnej wartości najbliższej 0
            A = i                                   #to wartość staje się naszą Wartością najbliższą zeru
            closest.clear()                         #czyścimy listę wartości najbliższych zeru
            closest.append(i)                       #dodajemy tę wartość do listy wartości najbliższych zeru
        elif fabs(i) == fabs(A):                    #jeśli wartość bezwzględna z i jest równa wartości bezwględnej wartości najbliższej zeru
            closest.append(i)                       #dodajemy tę wartość do listy wartości najbliższych zeru

    if A==0:
        return print("0 is found")
    else:
        return print("closest values: " + str(closest))


temperatureValues=[-50, -54, -23, 20, 17, -14, -7, 20, 25, 150, -42, 50, -59, 17, -17, -23, -14, 26, 34, -7, 14]
setTemperatureClosestToZero(temperatureValues)