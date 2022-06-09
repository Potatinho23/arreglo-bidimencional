import numpy as np

matriz1 = np.array([[1, 2, 3], 
                   [4, 5, 6],
                   [7, 8, 9]])

print("matriz 1:")

for f in range(3):
    for c in range(3):
        print(matriz1[f][c])

print("suma: ", matriz1.sum())
print("ndim: ", matriz1.ndim)
print("shape: ", matriz1.shape)
print("tamaño matriz 1:", matriz1.size)

matriz2 = np.array([[5, 6, 7],
                    [8, 9, 10]])

print("\nmatriz 2:")

for f in range(2):
    for c in range(3):
        print(matriz2[f][c])

print("suma: ", matriz2.sum())
print("ndim: ", matriz2.ndim)
print("shape: ", matriz2.shape)
print("tamaño matriz 1:", matriz2.size, "\n")

concatenar = np.concatenate((matriz1,matriz2), axis=0)

print("concatenación:\n", concatenar, "\n")

for f in range(5):
    print(concatenar[f,:])

print("\nfin xd")
