'''
Módulo de esquemas para las peticiones y respuestas del Resumidor Gemini y se define los modelos Pydantic usados en la API
'''
from pydantic import BaseModel, Field

class SummaryRequest(BaseModel):
    """
    Modelo para el cuerpo de la petición, es el input.
    """
    text: str = Field(
        ..., 
        min_length=30, 
        max_length=10000, 
        description="El texto que desea resumir debe tener entre 30 y 10000 caracteres."
    )
    
    # Ejemplo para la documentación automática de FastAPI
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": '''Una nueva generación de memorias RAM parece estar avistándose en el horizonte tecnológico. ¿La novedad? Recuerda los datos almacenados evitando así aquellas situaciones en las que la luz se va y nos deja a algunos con esa cara de incrédula consternación. A diferencia de las memorias RAM, que son las que en caso de apagón nos pueden dejar en la estacada, existen otras llamadas ReRam que son "no volátiles", es decir, que retienen datos sin necesidad de energía. Son ese tipo de memorias que usamos en dispositivos USB o en discos duros externos. Aunque estas memorias son más rápidas que el disco duro del computador, hasta el momento eran significativamente más lentas que la memoria RAM convencional, especialmente cuando se trata de escribir datos. Es por esta razón que este tipo de memorias no se utiliza para hacer funcionar varios tipos de programas y, por ende, se usan memorias electrónicas como la RAM, que necesitan un suministro de energía constante para "refrescar" contenidos y evitar que se pierdan.'''
                }
            ]
        }
    }

class SummaryResponse(BaseModel):
    """
    Modelo para la respuesta de la API es el Output.
    """
    summary: str
    original_length: int | None = None
