"""
Utilidades generales para el proyecto
"""
import re
import pandas as pd

def limpiar_texto(texto):
    """Limpia y normaliza texto"""
    if pd.isna(texto):
        return ""
    return str(texto).strip()

def convertir_numero(valor):
    """Convierte un valor a número, manejando formatos especiales"""
    if pd.isna(valor):
        return 0
    
    texto = str(valor).strip()
    
    # Remover porcentajes y caracteres especiales
    texto = re.sub(r'[%,]', '', texto)
    
    # Convertir a número
    try:
        return float(texto) if texto else 0
    except ValueError:
        return 0

def obtener_meta_carrera(carrera, metas_df):
    """Obtiene la meta para una carrera específica"""
    if carrera in metas_df['carrera'].values:
        return metas_df[metas_df['carrera'] == carrera]['meta_2026'].iloc[0]
    
    # Meta por defecto basada en el tipo de carrera
    if 'MEDICINA' in carrera.upper():
        return 200
    elif 'ARQUITECTURA' in carrera.upper():
        return 135
    elif 'DISEÑO GRÁFICO' in carrera.upper():
        return 110
    else:
        return 50  # Meta por defecto