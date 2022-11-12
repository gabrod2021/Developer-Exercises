import itertools
import numpy as np

#PARA PROBAR
"""mat = [
    [2, 1, 34, 5, 50],
    [3, 10, 13, 17, 9],
    [4, 5, 6, 7, 11],
    [5, 24, 6, 7, 8],
    [20, 18, 17, 16, 15],
]"""
#MATRIZ RANDOM
mat = np.random.randint(1,4, size=(5, 5)) 
print("MATRIZ RANDOM")
print(mat) 

def check(mat, template):
    for row, row_content in enumerate(mat):
        deltas = (int(abs(x - y) == 1) for x, y in itertools.pairwise(row_content))
        delta_string = "".join(map(str, deltas))
        pos = delta_string.find("111")
        if pos >= 0:
            print(template.format(row=row, ini=pos, end=pos + 3))

check(mat, "Posicion inicial fila: ({row}, {ini}) - Posicion final fila: ({row}, {end})")
print("")
print("MISMA RANDOM,TRASPUESTA")
t=list(zip(*mat))
tr=np.array(t)
print(tr)

check(tr, "Posicion inicial columna: ({ini}, {row}) - Posicion final columna: ({end}, {row})")