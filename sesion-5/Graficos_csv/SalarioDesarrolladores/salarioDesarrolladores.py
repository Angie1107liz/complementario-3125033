import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

# Ruta del archivo CSV
ruta_csv = r'C:\Users\Angie\OneDrive\Documentos\complementario-3125033\sesion-5\Graficos_csv\SalarioDesarrolladores\Software Engineer Salaries.csv'

# Función para procesar rangos salariales
def procesar_salario(salario):
    # Extraer números usando expresiones regulares
    numeros = re.findall(r'\d+', salario.replace(',', ''))
    if len(numeros) == 2:  # Si hay un rango (dos números)
        return (int(numeros[0]) + int(numeros[1])) / 2  # Retornar el promedio
    elif len(numeros) == 1:  # Si hay un único número
        return int(numeros[0])
    return None  # Si no se pudo procesar, retornar None

try:
    # Leer el archivo CSV
    df = pd.read_csv(ruta_csv)
    print("Archivo leído correctamente. Primeras filas:")
    print(df.head())

    # Validación de columnas necesarias
    columnas_requeridas = ['Company', 'Salary']
    for col in columnas_requeridas:
        if col not in df.columns:
            raise ValueError(f"La columna '{col}' no existe en el archivo.")

    # Aplicar la función para procesar la columna 'Salary'
    df['Salary'] = df['Salary'].apply(procesar_salario)

    # Eliminar filas con valores nulos en 'Salary'
    df = df.dropna(subset=['Salary'])

    # Asignar índices numéricos
    x = np.arange(len(df))  # Índices numéricos para el eje x
    y = df['Salary'].values  # Valores de salarios en el eje y

    # Ajuste lineal usando numpy.polyfit (grado 1 para línea recta)
    coeficientes = np.polyfit(x, y, 1)
    linea_ajuste = np.poly1d(coeficientes)

    # Crear valores de x para graficar la línea de ajuste
    x_linea = np.linspace(x.min(), x.max(), 100)
    y_linea = linea_ajuste(x_linea)

    # Graficar los puntos y la línea de ajuste
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', edgecolor='black', label='Datos')
    plt.plot(x_linea, y_linea, color='red', label='Línea de ajuste (lineal)', linestyle='--')
    
    # Etiquetas de empresas en el eje x
    plt.xticks(x, df['Company'], rotation=45)

    # Títulos y etiquetas
    plt.title('Correlación lineal entre Company y Salary')
    plt.xlabel('Company')
    plt.ylabel('Salary')
    plt.legend()

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Error: El archivo CSV no se encuentra en la ruta {ruta_csv}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Se ha producido un error: {e}")
