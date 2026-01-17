import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Metadatos de la API
    PROJECT_NAME: str = "Reto de un resumidor de textos con Gemini 2.5 flash preview"
    VERSION: str = "1.0.0"
    
    # Configuración de Entorno
    # Si no encuentra estas variables, lanzará un error al iniciar
    API_KEY_GEMINI: str
    ID_GOOGLE_CLOUD_PROJECT: str | None = None
    
    # Configuración de carga de archivo .env, esto solo para local development
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore"
    )
    
# Instanciamos la configuración para usar en toda la app
settings = Settings()