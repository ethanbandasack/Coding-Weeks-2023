import numpy as np
import matplotlib.pyplot as plt


def conversion(M):
    N = [[(0, 0, 0) for j in range(len(M[0]))] for i in range(len(M))]
    x = len(M)
    y = len(M[0])
    for i in range(x):
        for j in range(y):
            if M[i][j] == "":
                N[i][j] = (255, 255, 255)
            elif M[i][j] == 1:
                N[i][j] = (0, 0, 0)
    return np.array(N)


def affichage(M):
    plt.imshow(conversion(M))
    plt.axis('off')
    plt.show()
