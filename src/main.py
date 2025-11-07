"""
Módulo principal que coordina la generación del reporte
"""
import os
import pandas as pd
from datetime import datetime
from .procesador_csv import ProcesadorCSV
from .generador_excel import GeneradorExcel
from .configuracion import Configuracion

class ReporteVRAC:
    def __init__(self, config):
        self.config = config
        self.procesador = ProcesadorCSV(config)
        self.generador = GeneradorExcel(config)
    
    def generar_reporte(self):
        """Genera el reporte completo"""
        print("📖 Leyendo y procesando CSV...")
        datos_procesados = self.procesador.procesar_archivo()
        
        print("📊 Generando estructura de Excel...")
        archivo_salida = self.generador.crear_reporte_completo(datos_procesados)
        
        return archivo_salida

def generar_reporte_completo(config):
    """Función principal para generar el reporte"""
    reporte = ReporteVRAC(config)
    return reporte.generar_reporte()