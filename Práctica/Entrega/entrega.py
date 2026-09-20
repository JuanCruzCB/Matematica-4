import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from google.colab import drive
import sys


# Cargar y montar Google drive y luego cargar el .csv en un DataFrame de pandas
def cargar_csv(archivo):
    MY_DRIVE = "/content/drive/"
    DATA_DIR = MY_DRIVE + "MyDrive/MAT4/"

    # Montar Google Drive
    drive.mount("/content/drive")
    sys.path.append(DATA_DIR)

    # Cargar el .csv en un DataFrame
    df = pd.read_csv(DATA_DIR + archivo, sep=",")
    return df


# Borrar todas las columnas no numéricas y borrar la columna Y = value_eur
def seleccionar_columnas_validas(df):
    df_columnas_numericas = df.select_dtypes(include=["float64", "int64"]).apply(
        pd.to_numeric, errors="coerce"
    )

    df_columnas_numericas = df_columnas_numericas.drop(columns=["value_eur"])

    return df_columnas_numericas


# Calcular estadísticas de regresión lineal para cada atributo válido
def calcular_estadisticas_regresion(df_numerico, columna_y):
    resultados = {}

    for column in df_numerico.columns:
        filas_validas = df_numerico[[column]].join(columna_y).dropna().astype("float64")
        filas_x = filas_validas[column].values
        filas_y = filas_validas["value_eur"].values

        # Calcular estadísticas de regresión lineal para cada atributo válido si la cantidad de filas de esa columna es más que 2
        if len(filas_x) > 2:
            resultados[column] = calcular_estadisticas_regresion_columna(
                filas_x, filas_y
            )

    return resultados


# Calcular todas las estadísticas de regresión lineal dado y (variable dependiente), y filas_x (variable independiente)
def calcular_estadisticas_regresion_columna(filas_x, filas_y):
    n = len(filas_x)

    # Sumatoria de xi de 1 hasta n
    sumatoria_x = np.sum(filas_x)

    # Sumatoria de yi de 1 hasta n
    sumatoria_y = np.sum(filas_y)

    # Sumatoria de xi^2 de 1 hasta n
    sumatoria_x_cuadrado = np.sum(filas_x**2)

    # Sumatoria de yi^2 de 1 hasta n
    sumatoria_y_cuadrado = np.sum(filas_y**2)

    # Sumatoria de xi * yi de 1 hasta n
    sumatoria_x_por_y = np.sum(filas_x * filas_y)

    # Suma de productos cruzados
    Sxy = sumatoria_x_por_y - (sumatoria_x * sumatoria_y) / n

    # Suma de los cuadrados de las desviaciones de X respecto de su media
    Sxx = sumatoria_x_cuadrado - (sumatoria_x**2) / n

    # Suma de los cuadrados de las desviaciones de Y respecto de su media
    Syy = sumatoria_y_cuadrado - (sumatoria_y**2) / n

    if np.isnan(Sxx) or np.isnan(Syy) or np.isnan(Sxy):
        return None

    # β1 y β0
    β1 = Sxy / Sxx
    β0 = (sumatoria_y / n) - β1 * (sumatoria_x / n)

    # Suma de residuos al cuadrado
    SSR = Syy - β1 * Sxy

    # R^2 (coeficiente de determinación)
    R2 = 1 - (SSR / Syy)

    # r (coeficiente de correlación)
    r = np.sign(β1) * np.sqrt(R2)

    # Sigma cuadrado y estadístico t
    sigma_cuadrado = SSR / (n - 2)
    estadistico_t = β1 / np.sqrt(sigma_cuadrado / Sxx)

    # Valor crítico t y p-valor
    t_critico = stats.t.ppf(1 - 0.025, df=n - 2)
    p_valor = (1 - stats.t.cdf(np.abs(estadistico_t), df=n - 2)) * 2

    return {
        "Sxx": Sxx,
        "Syy": Syy,
        "Sxy": Sxy,
        "β1": β1,
        "β0": β0,
        "SSR": SSR,
        "R²": R2,
        "r": r,
        "estadístico t": estadistico_t,
        "p_valor": p_valor,
        "t_crit": t_critico,
        "pasa_la_prueba": abs(estadistico_t) > t_critico,
    }


# Top 5 atributos según su coeficiente de correlación (R²)
def top5_atributos(resultados, key, top_n=5):
    return sorted(resultados.items(), key=lambda x: abs(x[1][key]), reverse=True)[
        :top_n
    ]


# Crear un DataFrame en base a los resultados de los atributos
def crear_df_top5_atributos(top_atributos):
    datos_top5 = {
        "Atributo": [],
        "r": [],
        "R²": [],
        "β1": [],
        "β0": [],
        "Sxx": [],
        "Syy": [],
        "Sxy": [],
        "SSR": [],
        "Estadístico t": [],
        "Pvalor": [],
        "Pasa la prueba de regresión": [],
    }

    for atributo, resultado in top_atributos:
        datos_top5["Atributo"].append(atributo)
        datos_top5["r"].append(resultado["r"])
        datos_top5["R²"].append(resultado["R²"])
        datos_top5["β1"].append(resultado["β1"])
        datos_top5["β0"].append(resultado["β0"])
        datos_top5["Sxx"].append(resultado["Sxx"])
        datos_top5["Syy"].append(resultado["Syy"])
        datos_top5["Sxy"].append(resultado["Sxy"])
        datos_top5["SSR"].append(resultado["SSR"])
        datos_top5["Estadístico t"].append(resultado["estadístico t"])
        datos_top5["Pvalor"].append(resultado["p_valor"])
        datos_top5["Pasa la prueba de regresión"].append(
            "Sí" if resultado["pasa_la_prueba"] else "No"
        )

    return pd.DataFrame(datos_top5)


# Código principal
def main():
    df = cargar_csv("players_21.csv")

    # Variable dependiente
    y = df[["value_eur"]].astype("float64")

    df_numerico = seleccionar_columnas_validas(df)

    resultados = calcular_estadisticas_regresion(df_numerico, y)

    top_5_correlacion_lineal = top5_atributos(resultados, "r")
    top_5_coeficiente_determinacion = top5_atributos(resultados, "R²")

    # Crear DataFrame de los 5 atributos con mejor correlación lineal (r)
    df_top_corr = crear_df_top5_atributos(top_5_correlacion_lineal)

    # No mostrar decimales si es .000
    def formattear_decimales(valor):
        if valor == int(valor):
            return f"{int(valor)}"
        else:
            return f"{valor:.3f}"  # 3 decimales

    pd.set_option("display.float_format", formattear_decimales)

    return df_top_corr


df_top_corr = main()
df_top_corr
