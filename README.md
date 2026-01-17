# prueba_tecnica_tottus
Este es un proyecto para resolver el challenge para el puesto de Machine Learning Engineer 


gemini-summarizer/
├── app/                        # Código fuente principal
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada (inicializa FastAPI)
│   ├── core/                   # Configuraciones globales
│   │   ├── __init__.py
│   │   └── config.py           # Manejo de variables de entorno (API Keys, Settings)
│   ├── schemas/                # Modelos de datos (Pydantic) - Input/Output
│   │   ├── __init__.py
│   │   └── summary.py          # Definición del JSON de entrada y respuesta
│   ├── services/               # Lógica de negocio externa (Integraciones)
│   │   ├── __init__.py
│   │   ├── gemini_service.py   # Lógica para llamar a Google Gemini
│   │   └── bigquery_service.py # Lógica para guardar en BigQuery
│   └── routers/                # Rutas / Endpoints de la API
│       ├── __init__.py
│       └── api_v1.py           # Definición de endpoints (POST /summarize)
├── tests/                      # Pruebas unitarias e integración
│   ├── __init__.py
│   └── test_main.py
├── .dockerignore               
├── .env                        # Variables de entorno
├── .gitignore                  
├── cloudbuild.yaml             # Para CI/CD en GCP
├── Dockerfile                  # Definición del contenedor
├── README.md
└── requirements.txt            # Dependencias del proyecto