import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Ruta del archivo CSV
ruta_csv = r'C:\Users\Angie\OneDrive\Documentos\complementario-3125033\sesion-5\Graficos_csv\tecnologiasIntegrada\ClaMP_Integrated-5184.csv'

# Intentar leer el archivo CSV
try:
    df = pd.read_csv(ruta_csv)
    print("DataFrame leído correctamente:")
    print(df.head())  # Muestra las primeras filas del DataFrame para verificar la lectura
    
    # Verifica si las columnas necesarias están en el DataFrame
    columnas_requeridas = ['Tecnología', 'Deseada', 'Admirada']  # Columnas necesarias
    for col in columnas_requeridas:
        if col not in df.columns:
            print(f"Error: La columna '{col}' no existe en el archivo.")
            raise ValueError(f"La columna '{col}' no existe en el archivo CSV.")
    
    # Filtra las columnas necesarias
    data = df[['Tecnología', 'Deseada', 'Admirada']]

    # Verifica si las columnas 'Deseada' y 'Admirada' contienen valores numéricos
    data[['Deseada', 'Admirada']] = data[['Deseada', 'Admirada']].apply(pd.to_numeric, errors='coerce')

    # Eliminar filas con valores nulos o no numéricos
    data = data.dropna()

    # Graficar con colores para cada Tecnología
    plt.figure(figsize=(8, 6))
    
    # Asignar un color diferente a cada Tecnología
    Tecnología = data['Tecnología'].unique()
    colores = plt.cm.get_cmap('tab10', len(Tecnología))  # Usamos una paleta de colores

    for idx, Tecnología in enumerate(Tecnología):
        subset = data[data['Tecnología'] == Tecnología]
        plt.scatter(subset['Deseada'], subset['Admirada'], label=Tecnología, color=colores(idx))

    # Ajuste polinómico de segundo grado (curvado) entre 'Deseada' y 'Admirada'
    # Usamos polyfit para ajustar un polinomio de segundo grado (parabólica)
    p = np.polyfit(data['Deseada'], data['Admirada'], 2)
    poly = np.poly1d(p)

    # Crear valores de x para la línea de ajuste (usamos el rango de 'Deseada')
    x_range = np.linspace(data['Deseada'].min(), data['Deseada'].max(), 100)
    y_range = poly(x_range)

    # Graficar la línea de ajuste polinómico
    plt.plot(x_range, y_range, color='black', label='Ajuste polinómico (grado 2)', linestyle='--')

    # Títulos y etiquetas
    plt.title('Correlación ranking Tecnología de programación')
    plt.xlabel('Deseada')
    plt.ylabel('Admirada')
    
    # Agregar leyenda
    plt.legend(title='Tecnología')
    
    # Mostrar la gráfica
    plt.show()

except FileNotFoundError:
    print(f"Error: El archivo CSV no se encuentra en la ruta {ruta_csv}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Se ha producido un error: {e}")
