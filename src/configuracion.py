"""
Módulo de configuración del proyecto
"""
import json
import os

class Configuracion:
    def __init__(self, archivo_config="config.json"):
        self.archivo_config = archivo_config
        self.config = self._cargar_configuracion()
    
    def _cargar_configuracion(self):
        """Carga la configuración desde archivo JSON"""
        config_default = {
            "rutas": {
                "entrada": "data/input",
                "salida": "data/output", 
                "config": "data/config"
            },
            "archivos": {
                "csv_entrada": "datos_admision.csv",
                "metas": "metas_carreras.csv"
            },
            "columnas_csv": {
                "skip_rows": 2,
                "encoding": "utf-8"
            }
        }
        
        try:
            with open(self.archivo_config, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Crear archivo de configuración por defecto
            with open(self.archivo_config, 'w', encoding='utf-8') as f:
                json.dump(config_default, f, indent=4, ensure_ascii=False)
            return config_default
    
    @property
    def ruta_csv_entrada(self):
        return os.path.join(
            self.config["rutas"]["entrada"],
            self.config["archivos"]["csv_entrada"]
        )
    
    @property
    def ruta_salida(self):
        return self.config["rutas"]["salida"]
    
    @property
    def ruta_metas(self):
        return os.path.join(
            self.config["rutas"]["config"],
            self.config["archivos"]["metas"]
        )