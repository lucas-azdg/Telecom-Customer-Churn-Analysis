import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. CARGAR EL ARCHIVO (Aquí es donde se crea 'df')
# Asegúrate de que el nombre del archivo sea exactamente el que tienes en tu carpeta
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 2. LIMPIEZA RÁPIDA (Para que el heatmap no falle)
# Convertimos Churn a número y TotalCharges a numérico
df['Churn_Numeric'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()

# 3. SELECCIONAR COLUMNAS NUMÉRICAS
columnas_numericas = df.select_dtypes(include=['number'])

# 4. CREAR EL HEATMAP
plt.figure(figsize=(10, 8))
sns.heatmap(columnas_numericas.corr(), annot=True, cmap='coolwarm')
plt.title("Matriz de Correlación")
plt.show()