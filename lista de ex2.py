import numpy as np
import statistics as st

notas = [7, 5, 4, 5, 6, 3, 8, 4, 5, 4, 6, 4, 5, 6, 4, 5, 6, 4, 6, 6, 3, 8, 4, 5, 4, 5, 5, 6]
aprovados = [7, 5, 5, 6, 8, 5, 6, 5, 6, 5, 6, 6, 6, 8, 5, 5, 5, 6]

media = np.mean(notas)
mediana = np.median(notas)

print("media = %d" %(media))
print("mediana = %d" %(mediana))