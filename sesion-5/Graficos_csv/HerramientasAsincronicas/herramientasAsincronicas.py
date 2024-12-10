import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ruta del archivo CSV
ruta_csv = r'C:\Users\Angie\OneDrive\Documentos\complementario-3125033\sesion-5\Graficos_csv\HerramientasAsincronicas\herramientaAsincronicas.csv'

# Intentar leer el archivo CSV
try:
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(ruta_csv)
    print("DataFrame leído correctamente:")
    print(df.head())  # Muestra las primeras filas del DataFrame para verificar la lectura
    
    # Validar las columnas necesarias
    columnas_requeridas = ['Herramienta', 'Deseada', 'Admirada']  # Columnas necesarias
    for col in columnas_requeridas:
        if col not in df.columns:
            raise ValueError(f"La columna '{col}' no existe en el archivo CSV.")
    
    # Filtrar las columnas necesarias
    data = df[['Herramienta', 'Deseada', 'Admirada']]
    
    # Convertir las columnas 'Deseada' y 'Admirada' a valores numéricos
    data[['Deseada', 'Admirada']] = data[['Deseada', 'Admirada']].apply(pd.to_numeric, errors='coerce')
    data = data.dropna()  # Eliminar filas con valores nulos
    
    # Preparar los datos para el modelo de regresión lineal
    x = data['Deseada'].values.reshape(-1, 1)  # Deseada como valores de entrada (X)
    y = data['Admirada'].values  # Admirada como valores objetivo (y)
    
    # Ajustar un modelo de regresión lineal
    model = np.polyfit(x.flatten(), y, 1)  # Ajuste lineal de grado 1
    poly = np.poly1d(model)  # Crear una función polinómica de grado 1

    # Crear valores de x para la línea de ajuste
    x_range = np.linspace(x.min(), x.max(), 100)
    y_range = poly(x_range)

    # Configurar la estética de la gráfica con un estilo disponible
    plt.style.use('ggplot')  # Estilo de matplotlib similar a 'seaborn-whitegrid'
    
    # Graficar los puntos con un color único
    plt.figure(figsize=(10, 6))  # Tamaño más grande de la gráfica
    for idx, row in data.iterrows():
        plt.scatter(row['Deseada'], row['Admirada'], label=row['Herramienta'], edgecolor='black', alpha=0.7)

    # Graficar la línea de ajuste lineal
    plt.plot(x_range, y_range, color='red', label='Ajuste lineal', linestyle='--', linewidth=2)

    # Configuración de la gráfica
    plt.title('Correlación entre Deseada y Admirada de Herramientas', fontsize=14)
    plt.xlabel('Deseada', fontsize=12)
    plt.ylabel('Admirada', fontsize=12)
    plt.legend(title='Herramienta', fontsize=10)
    plt.tight_layout()

    # Mostrar la gráfica
    plt.show()

except FileNotFoundError:
    print(f"Error: El archivo CSV no se encuentra en la ruta {ruta_csv}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Se ha producido un error: {e}")
