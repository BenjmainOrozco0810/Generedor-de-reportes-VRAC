# procesador_csv.py
import pandas as pd
import logging
from configuracion import Configuracion

class ProcesadorCSV:
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        self.config = Configuracion()
        self.logger = self._configurar_logger()
    
    def _configurar_logger(self):
        logger = logging.getLogger('ProcesadorCSV')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def procesar_csv(self):
        """Procesa el CSV y lo convierte al formato estructurado para VRAC"""
        try:
            self.logger.info(f"📂 Leyendo CSV desde: {self.ruta_csv}")
            
            # Leer el archivo CSV
            df = pd.read_csv(self.ruta_csv)
            
            self.logger.info(f"✅ CSV leído correctamente. Dimensiones: {df.shape}")
            self.logger.info("📊 Columnas encontradas en el CSV:")
            for i, columna in enumerate(df.columns):
                self.logger.info(f"   {i+1:2d}. {columna}")
            
            # Validar que tenemos las columnas necesarias
            columnas_requeridas = ['facultad', 'carrera', 'jornada']
            for col in columnas_requeridas:
                if self.config.MAPEO_COLUMNAS_CSV[col] not in df.columns:
                    self.logger.warning(f"⚠️  Columna '{self.config.MAPEO_COLUMNAS_CSV[col]}' no encontrada")
            
            # Procesar y estructurar los datos
            datos_estructurados = self._estructurar_datos(df)
            
            self.logger.info(f"🎯 Datos estructurados: {len(datos_estructurados)} facultades procesadas")
            
            return datos_estructurados
            
        except Exception as e:
            self.logger.error(f"❌ Error procesando CSV: {e}")
            return None
    
    def _estructurar_datos(self, df):
        """Convierte el DataFrame del CSV al formato estructurado del VRAC"""
        datos_vrac = {}
        
        for _, fila in df.iterrows():
            try:
                # Obtener valores usando el mapeo configurado
                facultad = fila.get(self.config.MAPEO_COLUMNAS_CSV['facultad'], '')
                carrera = fila.get(self.config.MAPEO_COLUMNAS_CSV['carrera'], '')
                jornada = fila.get(self.config.MAPEO_COLUMNAS_CSV['jornada'], '')
                
                # Saltar filas vacías o de totales
                if not facultad or not carrera or 'TOTAL' in str(facultad).upper():
                    continue
                
                # Inicializar facultad si no existe
                if facultad not in datos_vrac:
                    datos_vrac[facultad] = {}
                
                # Obtener valores numéricos (manejar valores NaN)
                def obtener_valor_numerico(columna_csv, default=0):
                    valor = fila.get(columna_csv, default)
                    return int(valor) if pd.notna(valor) else default
                
                # Estructurar datos de la carrera
                datos_vrac[facultad][carrera] = {
                    'jornada': jornada,
                    'evaluados_2025': obtener_valor_numerico(self.config.MAPEO_COLUMNAS_CSV['evaluados_2025']),
                    'evaluados_2026': obtener_valor_numerico(self.config.MAPEO_COLUMNAS_CSV['evaluados_2026']),
                    'admitidos_2025': obtener_valor_numerico(self.config.MAPEO_COLUMNAS_CSV['admitidos_2025']),
                    'admitidos_2026': obtener_valor_numerico(self.config.MAPEO_COLUMNAS_CSV['admitidos_2026']),
                    'matriculados_2025': obtener_valor_numerico(self.config.MAPEO_COLUMNAS_CSV['matriculados_2025']),
                    'matriculados_2026': obtener_valor_numerico(self.config.MAPEO_COLUMNAS_CSV['matriculados_2026']),
                    'asignados_2025': obtener_valor_numerico(self.config.MAPEO_COLUMNAS_CSV['asignados_2025']),
                    'asignados_2026': obtener_valor_numerico(self.config.MAPEO_COLUMNAS_CSV['asignados_2026']),
                    'meta_2026': self.config.METAS_CARRERAS.get(carrera, 0)  # Usar meta configurada
                }
                
            except Exception as e:
                self.logger.warning(f"⚠️  Error procesando fila: {e}")
                continue
        
        return datos_vrac
    
    def obtener_estadisticas(self, datos_estructurados):
        """Genera estadísticas del procesamiento"""
        if not datos_estructurados:
            return "No hay datos para generar estadísticas"
        
        total_facultades = len(datos_estructurados)
        total_carreras = sum(len(carreras) for carreras in datos_estructurados.values())
        
        estadisticas = f"""
        📈 ESTADÍSTICAS DEL PROCESAMIENTO:
        -----------------------------------
        • Facultades procesadas: {total_facultades}
        • Carreras procesadas: {total_carreras}
        • Archivo CSV: {self.ruta_csv}
        
        Facultades encontradas:
        """
        
        for facultad, carreras in datos_estructurados.items():
            estadisticas += f"   • {facultad}: {len(carreras)} carreras\n"
        
        return estadisticas