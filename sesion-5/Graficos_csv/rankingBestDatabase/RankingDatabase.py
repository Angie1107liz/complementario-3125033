import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ruta del archivo CSV
ruta_csv = r'C:\Users\Angie\OneDrive\Documentos\complementario-3125033\sesion-5\Graficos_csv\rankingBestDatabase\BestDatabase.csv'

# Intentar leer el archivo CSV
try:
    df = pd.read_csv(ruta_csv)
    print("DataFrame leído correctamente:")
    print(df.head())  # Muestra las primeras filas del DataFrame para verificar la lectura
    
    # Verifica si las columnas necesarias están en el DataFrame
    columnas_requeridas = ['BaseDatos', 'Porcentaje']  # Columnas necesarias
    for col in columnas_requeridas:
        if col not in df.columns:
            print(f"Error: La columna '{col}' no existe en el archivo.")
            raise ValueError(f"La columna '{col}' no existe en el archivo CSV.")
    
    # Filtra las columnas necesarias
    data = df[['BaseDatos', 'Porcentaje']]

    # Verifica si la columna 'Porcentaje' contiene valores numéricos
    data['Porcentaje'] = pd.to_numeric(data['Porcentaje'], errors='coerce')

    # Eliminar filas con valores nulos o no numéricos en 'Porcentaje'
    data = data.dropna(subset=['Porcentaje'])

    # Usamos el índice como variable x para el ajuste polinómico
    x = np.arange(len(data))  # Crea un arreglo con índices (0, 1, 2, ..., N-1)
    y = data['Porcentaje'].values  # La columna de porcentajes

    # Ajuste polinómico de segundo grado (curvado) entre los índices y los valores de 'Porcentaje'
    p = np.polyfit(x, y, 2)  # Ajuste polinómico de grado 2
    poly = np.poly1d(p)  # Crea una función polinómica

    # Crear valores de x para la línea de ajuste (usamos el rango de índices)
    x_range = np.linspace(x.min(), x.max(), 100)
    y_range = poly(x_range)

    # Graficar los puntos de dispersión entre 'Base de Datos' y 'Porcentaje'
    plt.figure(figsize=(10, 6))

    # Asignar un color único para cada punto
    colores = plt.cm.get_cmap('viridis', len(data))  # Paleta de colores
    for idx, (BaseDatos, porcentaje) in enumerate(zip(data['BaseDatos'], y)):
        plt.scatter(BaseDatos, porcentaje, color=colores(idx), label=BaseDatos, edgecolor='black')

    # Graficar la línea de ajuste polinómico
    # Convertimos índices de `x_range` a herramientas usando `iloc` y mapeo lineal
    herramientas_range = np.interp(x_range, x, np.arange(len(data)))
    plt.plot(data['BaseDatos'].iloc[herramientas_range.astype(int)], y_range, color='black', label='Ajuste polinómico (grado 2)', linestyle='--')

    # Títulos y etiquetas
    plt.title('Correlación entre BaseDatos y Porcentaje')
    plt.xlabel('BaseDatos')
    plt.ylabel('Porcentaje')
    
    # Rotar las etiquetas de las herramientas para mejorar la legibilidad
    plt.xticks(rotation=45)

    # Ajustar leyenda para mostrar cada BaseDatos con su color
    plt.legend(title='BaseDatos', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')

    # Mostrar la gráfica
    plt.tight_layout()  # Ajusta el espaciado
    plt.show()

except FileNotFoundError:
    print(f"Error: El archivo CSV no se encuentra en la ruta {ruta_csv}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Se ha producido un error: {e}")
