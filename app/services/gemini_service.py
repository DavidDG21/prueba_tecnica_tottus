from google import genai
from app.core.config import settings

class GeminiService:
    """
    Servicio para interactuar con la API de Google Gemini 2.5 flash preview.
    """
    def __init__(self):

        # Configuramos la API Key al instanciar el servicio      
        self.client = genai.Client(api_key=settings.API_KEY_GEMINI)
        # Usamos un modelo específico de google genai
        self.model_name = "gemini-3-flash-preview"

    async def generate_summary(self, text: str) -> str:
        """
        Envía el texto a Gemini y retorna el resumen de forma asíncrona.
        """
        try:
            # Damos la instruccion de resumen al modelo
            prompt = f"Genera un resumen conciso y bien estructurado del siguiente texto: {text}"
            
            # Realizamos una llamada asíncrona a la API de Gemini
            response = await self.client.aio.models.generate_content(
            model=self.model_name,
            contents=prompt
            )
            
            # Verificamos si la respuesta fue bloqueada por seguridad o está vacía
            if not response.text:
                raise ValueError("La API de Gemini devolvió una respuesta vacía o fue bloqueada por filtros de seguridad.")
                
            return response.text

        except Exception as e:
            print(f"Error conectando con la API de Gemini: {e}")
            # Re-lanzamos el error para que el Router decida qué código HTTP devolver (500, 503, etc.)
            raise e

# Instanciamos el servicio para usarlo en los routers
gemini_service = GeminiService()