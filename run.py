#!/usr/bin/env python3
"""
Script principal para generar el Reporte VRAC Campus Central
"""
import os
import sys
from src.main import generar_reporte_completo
from src.configuracion import Configuracion

def main():
    print("🚀 INICIANDO GENERACIÓN DE REPORTE VRAC")
    print("=" * 50)
    
    # Cargar configuración
    config = Configuracion()
    
    try:
        # Generar reporte
        archivo_salida = generar_reporte_completo(config)
        
        print(f"✅ REPORTE GENERADO EXITOSAMENTE")
        print(f"📁 Archivo: {archivo_salida}")
        print(f"📊 Ubicación: {os.path.abspath(archivo_salida)}")
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()