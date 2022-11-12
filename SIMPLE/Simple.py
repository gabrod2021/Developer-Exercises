import random

def generaListaDic():
    for edad in edades:
      for clave,valor in edad.items():
        return edades

def ordenayMuestra(mifuncion):
    sortedDict=sorted(mifuncion(), key = lambda i: i['edad'],reverse=True)
    maximo = max(edades, key=lambda e: e["edad"])
    minimo = min(edades, key=lambda e: e["edad"])
    print(f"La persona de mas edad es: {maximo['nombre']} y la de menor edad, {minimo['nombre']}")
    print("LISTA ORDENADA:")
    return sortedDict

#MAIN###################################################################################################

edades=[{"nombre":"Gabriela","edad":random.randint(1,100)},{"nombre":"Claudia","edad":random.randint(1,100)},
        {"nombre":"Nancy","edad":random.randint(1,100)},{"nombre":"Roma","edad":random.randint(1,100)},
       {"nombre":"Neri","edad":random.randint(1,100)},{"nombre":"Blapo","edad":random.randint(1,100)},
        {"nombre":"Laura","edad":random.randint(1,100)},{"nombre":"Julio Cesar","edad":random.randint(1,100)},
        {"nombre":"BallNose","edad":random.randint(1,100)},{"nombre":"Moni","edad":random.randint(1,100)}]




genera=generaListaDic()
maxminlistaordenada=ordenayMuestra(generaListaDic)
print(maxminlistaordenada)


  