import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Cargar datos desde el archivo CSV
csv_data = """
Tecnología,Porcentaje
Node.js,40.8
React,39.5
jQuery,21.4
Next.js,17.9
Express,17.8
Angular,17.1
ASP.NET Core,16.9
Vue.js,15.4
Svelte,12.9
Pinia,12.9
Spring Boot,12.7
WordPress,12.3
Django,11.8
FastAPI,9.9
Laravel,7.9
"""

# Crear el DataFrame
from io import StringIO
data = pd.read_csv(StringIO(csv_data))

# Validar las columnas necesarias
columnas_requeridas = ['Tecnología', 'Porcentaje']
for col in columnas_requeridas:
    if col not in data.columns:
        raise ValueError(f"La columna '{col}' no existe en el DataFrame.")

# Convertir la columna 'Porcentaje' a valores numéricos y eliminar nulos
data['Porcentaje'] = pd.to_numeric(data['Porcentaje'], errors='coerce')
data = data.dropna(subset=['Porcentaje'])

# Crear índices numéricos para las tecnologías
x = np.arange(len(data)).reshape(-1, 1)  # Índices como valores de entrada (X)
y = data['Porcentaje'].values  # Porcentajes como valores objetivo (y)

# Ajustar un modelo lineal
model = LinearRegression()
model.fit(x, y)

# Predicciones del modelo lineal
x_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)  # Rango para línea de regresión
y_pred = model.predict(x_range)

# Graficar los datos y la línea de regresión
plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='blue', edgecolor='black', label='Datos originales')
plt.plot(x_range, y_pred, color='red', linestyle='--', label='Regresión lineal')

# Configuración de los ejes
plt.xticks(x.flatten(), data['Tecnología'], rotation=45)
plt.title('Correlación lineal entre Frameworks y Porcentajes')
plt.xlabel('Frameworks')
plt.ylabel('Porcentaje')

# Mostrar leyenda y gráfico
plt.legend()
plt.tight_layout()
plt.show()
