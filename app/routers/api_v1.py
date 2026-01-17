from fastapi import APIRouter, HTTPException, status, BackgroundTasks
from app.schemas.summary import SummaryRequest, SummaryResponse
from app.services.gemini_service import gemini_service
from app.services.bigquery_service import bigquery_service

# Creamos un router para agrupar endpoints
router = APIRouter()

@router.post(
    "/summarize",
    response_model = SummaryResponse, 
    status_code = status.HTTP_200_OK,
    summary = "Generar resumen de texto",
    description = "Recibe un texto y devuelve un resumen generado por IA"
)
async def summarize_text(request: SummaryRequest, background_tasks: BackgroundTasks):
    """
    Endpoint principal.
    Primer se valida el input automáticamente gracias a Pydantic
    Llama al servicio de IA de forma asíncrona
    Maneja errores y devuelve JSON
    """
    try:
        # Llamamos al servicio
        summary_text = await gemini_service.generate_summary(request.text)

        # Guardamos el resumen en BigQuery de forma asíncrona
        background_tasks.add_task(
            bigquery_service.save_summary, 
            text=request.text, 
            summary=summary_text
        )
        
        # Construimos la respuesta
        return SummaryResponse(
            summary = summary_text,
            original_length = len(request.text)
        )
        
    except ValueError as ve:
        # Errores de validación
        raise HTTPException(
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail = str(ve)
        )
    except Exception as e:
        # Errores generales
        raise HTTPException(
            status_code = status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail = "Error conectando con el servicio de IA, intente más tarde"
        )