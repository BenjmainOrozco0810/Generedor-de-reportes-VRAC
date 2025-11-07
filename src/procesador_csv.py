"""
Módulo para procesar el archivo CSV de entrada
"""
import pandas as pd
import re
from .utils import limpiar_texto, convertir_numero

class ProcesadorCSV:
    def __init__(self, config):
        self.config = config
        self.columnas_mapeo = self._definir_mapeo_columnas()
    
    def _definir_mapeo_columnas(self):
        """Define el mapeo de columnas del CSV a nombres legibles"""
        return {
            0: 'facultad',
            1: 'carrera', 
            2: 'jornada',
            3: 'evaluados_2025',
            4: 'evaluados_2026',
            5: 'diff_evaluados',
            6: 'porc_diff_evaluados',
            7: 'admitidos_2025',
            8: 'admitidos_2026',
            9: 'diff_admitidos',
            10: 'porc_diff_admitidos',
            11: 'matriculados_2025',
            12: 'matriculados_2026',
            13: 'diff_matriculados',
            14: 'porc_diff_matriculados',
            # ... continuar con el mapeo completo
        }
    
    def procesar_archivo(self):
        """Procesa el archivo CSV y retorna datos limpios"""
        # Leer CSV
        ruta_csv = self.config.ruta_csv_entrada
        df = pd.read_csv(ruta_csv, encoding='utf-8', skiprows=2, header=None)
        
        # Renombrar columnas
        columnas_usar = {k: v for k, v in self.columnas_mapeo.items() if k < len(df.columns)}
        df = df.rename(columns=columnas_usar)
        
        # Filtrar solo filas de carreras (no totales)
        df_carreras = df[~df['carrera'].str.contains('TOTAL', na=False)].copy()
        
        # Limpiar datos
        df_limpio = self._limpiar_datos(df_carreras)
        
        return df_limpio
    
    def _limpiar_datos(self, df):
        """Limpia y normaliza los datos"""
        # Limpiar textos
        for col in ['facultad', 'carrera', 'jornada']:
            df[col] = df[col].apply(limpiar_texto)
        
        # Convertir números
        columnas_numericas = [
            'evaluados_2025', 'evaluados_2026', 'diff_evaluados',
            'admitidos_2025', 'admitidos_2026', 'diff_admitidos',
            'matriculados_2025', 'matriculados_2026', 'diff_matriculados'
        ]
        
        for col in columnas_numericas:
            if col in df.columns:
                df[col] = df[col].apply(convertir_numero)
        
        return df