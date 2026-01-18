'''
Módulo de servicio para interactuar con Google BigQuery, hacemos la inserción de resúmenes generados
'''
from google.cloud import bigquery
from app.core.config import settings
from datetime import datetime
from zoneinfo import ZoneInfo
import logging

class BigQueryService:
    '''
    Servicio para interactuar con Google BigQuery, hacemos la inserción de resúmenes generados
    '''
    def __init__(self):
        # Solo lo inicializamos si hay un proyecto configurado y se usara las credenciales de Cloud Run
        self.client = None
        if settings.ID_GOOGLE_CLOUD_PROJECT:
            try:
                self.client = bigquery.Client(project=settings.ID_GOOGLE_CLOUD_PROJECT)
                # Definimos la tabla destino
                self.table_id = f"{settings.ID_GOOGLE_CLOUD_PROJECT}.resumen_app.historia"
            except Exception as e:
                logging.error(f"No se pudo inicializar BigQuery: {e}")

    async def save_summary(self, text: str, summary: str):
        """
        Inserta el registro en BigQuery de forma asíncrona
        """
        if not self.client:
            logging.warning("BigQuery client no inicializado, no se guardará el resumen.")
            return
        # Preparamos los datos a insertar
        fecha_actual = datetime.now(ZoneInfo("America/Lima")).replace(microsecond=0)
        rows_to_insert = [
            {
                "fecha": fecha_actual.isoformat(),
                "texto_original": text,
                "texto_resumido": summary,
            }
        ]

        try:
            # Insertamos el registro en BigQuery
            errors = self.client.insert_rows_json(self.table_id, rows_to_insert)
            if errors:
                logging.error(f"Errores al insertar en BQ: {errors}")
            else:
                logging.info("Registro guardado en BigQuery exitosamente.")
        except Exception as e:
            logging.error(f"Error crítico guardando en BigQuery: {e}")

bigquery_service = BigQueryService()
