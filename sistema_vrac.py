# sistema_vrac.py
import os
import sys
from procesador_csv import ProcesadorCSV
from generador_excel import GeneradorExcel
from configuracion import Configuracion

class SistemaVRAC:
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        self.config = Configuracion()
        self.procesador_csv = ProcesadorCSV(ruta_csv)
        self.generador_excel = GeneradorExcel()
    
    def ejecutar(self):
        """Ejecuta el flujo completo del sistema"""
        print("🚀 INICIANDO SISTEMA AUTOMATIZADO VRAC")
        print("=" * 50)
        
        # Paso 1: Procesar CSV
        print("📂 Paso 1: Procesando archivo CSV...")
        datos_estructurados = self.procesador_csv.procesar_csv()
        
        if not datos_estructurados:
            print("❌ No se pudieron procesar los datos. Verifica el archivo CSV.")
            return None
        
        # Mostrar estadísticas
        estadisticas = self.procesador_csv.obtener_estadisticas(datos_estructurados)
        print(estadisticas)
        
        # Paso 2: Generar Excel
        print("\n📊 Paso 2: Generando reporte Excel...")
        archivo_generado = self.generador_excel.crear_reporte_completo(datos_estructurados)
        
        if archivo_generado:
            print(f"🎉 PROCESO COMPLETADO EXITOSAMENTE!")
            print(f"📁 Reporte generado: {archivo_generado}")
            print(f"📏 Tamaño: {os.path.getsize(archivo_generado) / 1024:.2f} KB")
        else:
            print("❌ Error generando el reporte Excel")
        
        return archivo_generado

def main():
    """Función principal del sistema"""
    if len(sys.argv) != 2:
        print("💡 Uso: python sistema_vrac.py <ruta_al_archivo_csv>")
        print("   Ejemplo: python sistema_vrac.py datos/datos_coa.csv")
        return
    
    ruta_csv = sys.argv[1]
    
    if not os.path.exists(ruta_csv):
        print(f"❌ El archivo no existe: {ruta_csv}")
        return
    
    # Ejecutar sistema
    sistema = SistemaVRAC(ruta_csv)
    sistema.ejecutar()

if __name__ == "__main__":
    main()