import numpy as np


def getInputArray():
    global vecs
    global numDim
    for i in range(3):
        for j in range(numDim):
            vecs[i][j] = float(input(f"Vector {i+1}'s x{j+1}: "))
        print()


def printVecs():
    print(f"Vector 1: {vecs[0]}")
    print(f"Vector 2: {vecs[1]}")
    print(f"Vector 3: {vecs[2]}")


def proj(vec1, vec2):
    temp = np.dot(vec1, vec2)
    return temp*vec2


numDim = int(input("Input number of dimensions per vector: "))
vecs = np.ndarray(shape=(3, numDim), dtype=float)
getInputArray()
print()
vecs[0] = np.true_divide(vecs[0], np.linalg.norm(vecs[0]))
vec1notnormal = vecs[1]-proj(vecs[1], vecs[0])
print(
    f"Showing work, dot prod (v2 . u1) = {np.dot(vecs[1],vecs[0])}, (v2 . u1)u1 ={proj(vecs[1], vecs[0])}\n")
vecs[1] = np.true_divide(vec1notnormal, np.linalg.norm(vec1notnormal))
vec2notnormal = vecs[2]-proj(vecs[2], vecs[1])-proj(vecs[2], vecs[0])
print(
    f"Showing work, dot prod (v3 . u2) = {np.dot(vecs[2],vecs[1])}, (v3 . u2)u2 ={proj(vecs[2], vecs[1])}")
print(
    f"Showing work, dot prod (v3 . u1) = {np.dot(vecs[2],vecs[0])} (v3 . u1)u1={proj(vecs[2], vecs[0])}\n")
vecs[2] = np.true_divide(vec2notnormal, np.linalg.norm(vec2notnormal))
print()
printVecs()
