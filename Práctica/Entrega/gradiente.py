import numpy as np
import pandas as pd

X = df[
    [
        "wage_eur",
        "overall",
        "potential",
    ]
]  # Las características para predecir la calidad del vino
Y = df["value_eur"]  # Calidad del vino
X = np.hstack(
    (np.ones((X.shape[0], 1)), X)
)  # Se agrega una columna para representar el B0
coefs = np.random.uniform(-0.5, 0.5, size=X.shape[1])  # Los valores iniciales
paso = 0.00000001  # Valor del paso
tolerancia = 10e-07  # Tolerancia aceptada
maxIteraciones = 30000
iteraciones = 1
f = lambda coeficientes, X, Y: np.sum(
    (Y - np.dot(X, coeficientes)) ** 2
)  # La función a minimizar
derivada_f = lambda coeficientes, X, Y: [
    -2 * np.sum((Y - np.dot(X, coeficientes)) * X[:, i]) for i in range(X.shape[1])
]  # Las derivadas parciales
xprev = coefs
xnew = xprev - paso * np.array(derivada_f(xprev, X, Y))  # Se calcula el nuevo x
error = abs(f(xnew, X, Y) - f(xprev, X, Y))
print(iteraciones)
print(xnew)
print(error)

# Mientras el error sea mayor a la tolerancia y las iteraciones menor al maximo de iteraciones
while (error > tolerancia) and iteraciones < maxIteraciones:
    iteraciones += 1
    xprev = xnew
    xnew = xprev - paso * np.array(derivada_f(xprev, X, Y))
    error = abs(f(xnew, X, Y) - f(xprev, X, Y))
    print(iteraciones)
    print(xnew)
    print(error)
