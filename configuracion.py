# configuracion.py
from datetime import datetime

class Configuracion:
    # Mapeo de columnas del CSV al formato VRAC
    # ¡AJUSTA ESTOS NOMBRES SEGÚN TU CSV!
    MAPEO_COLUMNAS_CSV = {
        'facultad': 'FACULTAD',           # Columna de facultad en tu CSV
        'carrera': 'CARRERA',             # Columna de carrera en tu CSV  
        'jornada': 'JORNADA',             # Columna de jornada en tu CSV
        'evaluados_2025': 'EVAL_2025',    # Evaluados generación 2025
        'evaluados_2026': 'EVAL_2026',    # Evaluados generación 2026
        'admitidos_2025': 'ADMIT_2025',   # Admitidos generación 2025
        'admitidos_2026': 'ADMIT_2026',   # Admitidos generación 2026
        'matriculados_2025': 'MAT_2025',  # Matriculados generación 2025
        'matriculados_2026': 'MAT_2026',  # Matriculados generación 2026
        'asignados_2025': 'ASIG_2025',    # Asignados generación 2025
        'asignados_2026': 'ASIG_2026',    # Asignados generación 2026
        'meta_2026': 'META_2026'          # Meta 2026
    }
    
    # Metas por carrera (puedes ajustar estos valores)
    METAS_CARRERAS = {
        'LICENCIATURA EN ARQUITECTURA': 135,
        'LICENCIATURA EN DISEÑO GRÁFICO': 110,
        'LICENCIATURA EN DISEÑO INDUSTRIAL': 40,
        'LICENCIATURA EN MEDICINA': 200,
        'LICENCIATURA EN NUTRICIÓN': 80,
        # ... añade más carreras según necesites
    }
    
    @staticmethod
    def obtener_fecha_actual():
        return datetime.now().strftime("%d_%m_%Y")
    
    @staticmethod
    def obtener_encabezados_vrac():
        return [
            'FACULTAD', 'CARRERA', '', '', 'JORNADA', '', '',
            'EVALUADOS *', '', 'DIFERENCIA', '% DIFERENCIA', '',
            'ADMITIDOS **', '', 'DIFERENCIA', '% DIFERENCIA', '', 
            'MATRICULADOS', '', 'DIFERENCIA', '% DIFERENCIA', '',
            'ASIGNADOS', '', 'DIFERENCIA', '% DIFERENCIA', '',
            'META 2026', '', 'CUMPLIMIENTO META'
        ]