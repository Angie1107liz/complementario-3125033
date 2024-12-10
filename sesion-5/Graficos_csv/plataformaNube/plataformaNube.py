import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Ruta del archivo CSV
ruta_csv = r'C:\Users\Angie\OneDrive\Documentos\complementario-3125033\sesion-5\Graficos_csv\plataformaNube\plataformaNube.csv'

# Intentar leer el archivo CSV
try:
    df = pd.read_csv(ruta_csv)
    print("DataFrame leído correctamente:")
    print(df.head())  # Muestra las primeras filas del DataFrame para verificar la lectura
    
    # Verifica si las columnas necesarias están en el DataFrame
    columnas_requeridas = ['Plataforma', 'Deseado', 'Admirado']  # Columnas necesarias
    for col in columnas_requeridas:
        if col not in df.columns:
            print(f"Error: La columna '{col}' no existe en el archivo.")
            raise ValueError(f"La columna '{col}' no existe en el archivo CSV.")
    
    # Filtra las columnas necesarias
    data = df[['Plataforma', 'Deseado', 'Admirado']]

    # Verifica si las columnas 'Deseado' y 'Admirado' contienen valores numéricos
    data[['Deseado', 'Admirado']] = data[['Deseado', 'Admirado']].apply(pd.to_numeric, errors='coerce')

    # Eliminar filas con valores nulos o no numéricos
    data = data.dropna()

    # Graficar con colores únicos para cada punto
    plt.figure(figsize=(8, 6))

    # Generar un color único para cada punto
    colores = plt.cm.get_cmap('viridis', len(data))  # Escoger un colormap
    for idx in range(len(data)):
        fila = data.iloc[idx]
        plt.scatter(
            fila['Deseado'],
            fila['Admirado'],
            label=f"{fila['Plataforma']}",
            color=colores(idx),
            edgecolor='black'
        )

    # Ajuste de regresión lineal entre 'Deseado' y 'Admirado'
    X = data[['Deseado']]  # Variable independiente
    y = data['Admirado']   # Variable dependiente

    # Crear el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X, y)

    # Obtener los valores predichos de la regresión lineal
    y_pred = model.predict(X)

    # Graficar la línea de regresión lineal
    plt.plot(data['Deseado'], y_pred, color='black', label='Ajuste lineal', linestyle='--')

    # Títulos y etiquetas
    plt.title('Correlación entre Deseado y Admirado de Plataformas', fontsize=14)
    plt.xlabel('Deseado', fontsize=12)
    plt.ylabel('Admirado', fontsize=12)
    
    # Agregar leyenda
    plt.legend(title='Plataforma', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
    plt.tight_layout()
    
    # Mostrar la gráfica
    plt.show()

except FileNotFoundError:
    print(f"Error: El archivo CSV no se encuentra en la ruta {ruta_csv}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Se ha producido un error: {e}")
