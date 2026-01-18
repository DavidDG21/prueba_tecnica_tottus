'''
Módulo principal de la aplicación FastAPI para el Resumidor Gemini
Configura la aplicación, incluye routers y define el endpoint de salud

'''

from fastapi import FastAPI
from app.core.config import settings
from app.routers import api_v1

# Inicializamos la aplicación con metadatos
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API para resumir textos usando la IA de Google Gemini 3 flash preview",
)
# añadimos el router de la versión 1 de la API,
# la ruta es /api/v1/resumen
app.include_router(api_v1.router, prefix="/api/v1", tags=["Resumidor de Textos"])

@app.get("/", tags=["Health Check"])
async def root():
    """
    Endpoint para verificar que el servicio está vivo.
    """
    return {"message": "Resumidor Gemini está en ejecución", "version": settings.VERSION}

# Bloque para ejecución directa
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)
    