import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Ruta del archivo CSV
ruta_csv = r'C:\Users\Angie\OneDrive\Documentos\complementario-3125033\sesion-5\Graficos_csv\HerramientasSoftware\herramientasSoftware.csv'

# Intentar leer el archivo CSV
try:
    df = pd.read_csv(ruta_csv)
    print("DataFrame leído correctamente:")
    print(df.head())  # Muestra las primeras filas del DataFrame para verificar la lectura
    
    # Verifica si las columnas necesarias están en el DataFrame
    columnas_requeridas = ['Herramienta', 'Deseada', 'Admirada']  # Columnas necesarias
    for col in columnas_requeridas:
        if col not in df.columns:
            print(f"Error: La columna '{col}' no existe en el archivo.")
            raise ValueError(f"La columna '{col}' no existe en el archivo CSV.")
    
    # Filtra las columnas necesarias
    data = df[['Herramienta', 'Deseada', 'Admirada']]

    # Verifica si las columnas 'Deseada' y 'Admirada' contienen valores numéricos
    data[['Deseada', 'Admirada']] = data[['Deseada', 'Admirada']].apply(pd.to_numeric, errors='coerce')

    # Eliminar filas con valores nulos o no numéricos
    data = data.dropna()

    # Configurar el estilo de la gráfica con 'ggplot'
    plt.style.use('ggplot')  # Estilo de matplotlib similar a 'seaborn-whitegrid'

    # Graficar con colores para cada Herramienta
    plt.figure(figsize=(10, 6))  # Tamaño más grande de la gráfica
    
    # Asignar un color diferente a cada Herramienta
    Herramienta = data['Herramienta'].unique()
    colores = plt.cm.get_cmap('tab10', len(Herramienta))  # Usamos una paleta de colores

    # Graficar cada Herramienta con su color único
    for idx, Herramienta in enumerate(Herramienta):
        subset = data[data['Herramienta'] == Herramienta]
        plt.scatter(subset['Deseada'], subset['Admirada'], label=Herramienta, color=colores(idx), edgecolor='black', alpha=0.7)

    # Ajuste polinómico de segundo grado (curvado) entre 'Deseada' y 'Admirada'
    # Usamos polyfit para ajustar un polinomio de segundo grado (parabólica)
    p = np.polyfit(data['Deseada'], data['Admirada'], 2)
    poly = np.poly1d(p)

    # Crear valores de x para la línea de ajuste (usamos el rango de 'Deseada')
    x_range = np.linspace(data['Deseada'].min(), data['Deseada'].max(), 100)
    y_range = poly(x_range)

    # Graficar la línea de ajuste polinómico
    plt.plot(x_range, y_range, color='black', label='Ajuste polinómico (grado 2)', linestyle='--', linewidth=2)

    # Títulos y etiquetas
    plt.title('Correlación ranking Herramientas de software', fontsize=14)
    plt.xlabel('Deseada', fontsize=12)
    plt.ylabel('Admirada', fontsize=12)
    
    # Agregar leyenda
    plt.legend(title='Herramienta', fontsize=10)
    
    # Ajuste de la disposición para evitar sobreposiciones
    plt.tight_layout()

    # Mostrar la gráfica
    plt.show()

except FileNotFoundError:
    print(f"Error: El archivo CSV no se encuentra en la ruta {ruta_csv}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Se ha producido un error: {e}")
