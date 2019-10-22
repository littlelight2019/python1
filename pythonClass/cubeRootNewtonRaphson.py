# -*- coding: utf-8 -*-

def cubeRoot(y, guessX):
    """
    improve the approximate root with Newton-Raphson method:
        deltaX = (f(x1) - f(x)) / f'(x1)
    """
    epsilon = 1e-3
    guessedCube = guessX ** 3
    while abs(guessedCube - y) > epsilon:
        if guessedCube > y:
            guessX = guessX - (guessedCube-y) / (guessX**2 * 3)
        else:
            guessX = (y-guessedCube) / (guessX**2 * 3) + guessX
        guessedCube = guessX ** 3
        print(guessX, guessedCube)
    return guessX
        
