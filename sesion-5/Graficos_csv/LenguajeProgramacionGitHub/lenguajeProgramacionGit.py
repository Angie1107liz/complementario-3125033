import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Ruta del archivo CSV
ruta_csv = r'C:\Users\Angie\OneDrive\Documentos\complementario-3125033\sesion-5\Graficos_csv\LenguajeProgramacionGitHub\lenguajesProgramacion.csv'

# Intentar leer el archivo CSV
try:
    df = pd.read_csv(ruta_csv)
    print("DataFrame leído correctamente:")
    print(df.head())  # Muestra las primeras filas del DataFrame para verificar la lectura
    
    # Verifica si las columnas necesarias están en el DataFrame
    columnas_requeridas = ['name', 'quarter']  # Columnas necesarias
    for col in columnas_requeridas:
        if col not in df.columns:
            print(f"Error: La columna '{col}' no existe en el archivo.")
            raise ValueError(f"La columna '{col}' no existe en el archivo CSV.")
    
    # Filtra las columnas necesarias
    data = df[['name', 'quarter']]

    # Verifica si la columna 'quarter' contiene valores numéricos
    data['quarter'] = pd.to_numeric(data['quarter'], errors='coerce')

    # Eliminar filas con valores nulos o no numéricos en 'quarter'
    data = data.dropna(subset=['quarter'])

    # Crear un índice numérico para las tecnologías (lenguajes de programación)
    x = np.arange(len(data))  # Índices como valores de entrada (X)
    y = data['quarter'].values  # Valores de la columna 'quarter'

    # Ajustar un modelo lineal
    model = LinearRegression()
    x = x.reshape(-1, 1)  # Reshape para asegurar que x tiene 2 dimensiones
    model.fit(x, y)

    # Predicciones del modelo lineal
    x_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)  # Rango para línea de regresión
    y_pred = model.predict(x_range)

    # Usamos el estilo ggplot de matplotlib
    plt.style.use('ggplot')

    # Graficar los datos y la línea de regresión
    plt.figure(figsize=(12, 6))

    # Graficar los puntos de dispersión entre el índice y 'quarter'
    plt.scatter(x, y, c=y, cmap='plasma', s=100, edgecolors='black', alpha=0.7, label='Datos originales')

    # Graficar la línea de regresión lineal
    plt.plot(x_range, y_pred, color='red', linestyle='--', label='Regresión lineal')

    # Configuración de los ejes
    plt.title('Correlación lineal entre Popularidad de Lenguajes de Programación y Quartiles', fontsize=14)
    plt.xlabel('Índice de Lenguaje de Programación', fontsize=12)
    plt.ylabel('Popularidad (Quartiles)', fontsize=12)

    # Rotar las etiquetas de los lenguajes para mejorar la legibilidad
    plt.xticks(rotation=45)
    plt.xticks(ticks=np.arange(len(data)), labels=data['name'], rotation=45)

    # Agregar leyenda
    plt.legend()

    # Agregar barra de colores para mostrar la escala
    plt.colorbar(label='Popularidad')

    # Ajustar la disposición para evitar sobreposiciones
    plt.tight_layout()

    # Mostrar la gráfica
    plt.show()

except FileNotFoundError:
    print(f"Error: El archivo CSV no se encuentra en la ruta {ruta_csv}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Se ha producido un error: {e}")
