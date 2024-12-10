import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Cargar datos desde el archivo CSV
csv_data = """
Herramienta,Porcentaje
ChatGPT,82.1
GitHub Copilot,41.2
Google Gemini,23.9
Bing AI,15.8
Visual Studio Intellicode,13.6
Claude,8.1
Codeium,6.1
WolframAlpha,5.6
Perplexity AI,5.3
Tabnine,5
Meta AI,3.8
Phind,3.2
Amazon Q,2.6
You.com,1.4
Cody,1.3
"""

# Crear el DataFrame
from io import StringIO
data = pd.read_csv(StringIO(csv_data))

# Verificar las columnas requeridas
columnas_requeridas = ['Herramienta', 'Porcentaje']
for col in columnas_requeridas:
    if col not in data.columns:
        raise ValueError(f"La columna '{col}' no existe en el DataFrame.")

# Convertir la columna 'Porcentaje' a valores numéricos y eliminar los nulos
data['Porcentaje'] = pd.to_numeric(data['Porcentaje'], errors='coerce')
data = data.dropna(subset=['Porcentaje'])

# Crear índices numéricos para las herramientas
x = np.arange(len(data)).reshape(-1, 1)  # Índices como valores de entrada (X)
y = data['Porcentaje'].values  # Porcentajes como valores objetivo (y)

# Ajustar un modelo lineal
model = LinearRegression()
model.fit(x, y)

# Predicciones del modelo lineal
x_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)  # Rango para la línea de regresión
y_pred = model.predict(x_range)

# Graficar los datos y la línea de regresión
plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='blue', edgecolor='black', label='Datos originales')
plt.plot(x_range, y_pred, color='red', linestyle='--', label='Regresión lineal')

# Configuración de los ejes
plt.xticks(x.flatten(), data['Herramienta'], rotation=45)
plt.title('Correlación lineal entre Herramientas y Porcentajes')
plt.xlabel('Herramienta')
plt.ylabel('Porcentaje')

# Mostrar leyenda y gráfico
plt.legend()
plt.tight_layout()
plt.show()
