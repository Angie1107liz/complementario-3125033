import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Ruta del archivo CSV
ruta_csv = r'C:\Users\Angie\OneDrive\Documentos\complementario-3125033\sesion-5\Graficos_csv\RankingMejoresLenguajes\rankingLenguajesProgramacion.csv'

# Intentar leer el archivo CSV
try:
    df = pd.read_csv(ruta_csv)
    print("DataFrame leído correctamente:")
    print(df.head())  # Muestra las primeras filas del DataFrame para verificar la lectura
    
    # Verifica si las columnas necesarias están en el DataFrame
    columnas_requeridas = ['Lenguaje', 'Deseado', 'Admirado']  # Columnas necesarias
    for col in columnas_requeridas:
        if col not in df.columns:
            print(f"Error: La columna '{col}' no existe en el archivo.")
            raise ValueError(f"La columna '{col}' no existe en el archivo CSV.")
    
    # Filtra las columnas necesarias
    data = df[['Lenguaje', 'Deseado', 'Admirado']]

    # Verifica si las columnas 'Deseado' y 'Admirado' contienen valores numéricos
    data[['Deseado', 'Admirado']] = data[['Deseado', 'Admirado']].apply(pd.to_numeric, errors='coerce')

    # Eliminar filas con valores nulos o no numéricos
    data = data.dropna()

    # Graficar con colores únicos para cada punto
    plt.figure(figsize=(8, 6))
    
    # Generar una paleta de colores para cada punto
    colores = plt.cm.viridis(np.linspace(0, 1, len(data)))  # Asigna colores a cada punto

    # Graficar cada punto con un color único
    for idx, (lenguaje, deseado, admirado) in enumerate(zip(data['Lenguaje'], data['Deseado'], data['Admirado'])):
        plt.scatter(deseado, admirado, label=lenguaje, color=colores[idx], edgecolor='black', s=100)

    # Ajuste polinómico de segundo grado (curvado) entre 'Deseado' y 'Admirado'
    p = np.polyfit(data['Deseado'], data['Admirado'], 2)
    poly = np.poly1d(p)

    # Crear valores de x para la línea de ajuste (usamos el rango de 'Deseado')
    x_range = np.linspace(data['Deseado'].min(), data['Deseado'].max(), 100)
    y_range = poly(x_range)

    # Graficar la línea de ajuste polinómico
    plt.plot(x_range, y_range, color='black', label='Ajuste polinómico (grado 2)', linestyle='--')

    # Títulos y etiquetas
    plt.title('Correlación ranking lenguajes de programación')
    plt.xlabel('Deseado')
    plt.ylabel('Admirado')
    
    # Agregar leyenda
    plt.legend(title='Lenguaje', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
    
    # Mostrar la gráfica
    plt.tight_layout()  # Ajusta el espaciado para evitar sobreposición
    plt.show()

except FileNotFoundError:
    print(f"Error: El archivo CSV no se encuentra en la ruta {ruta_csv}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Se ha producido un error: {e}")
