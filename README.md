# 🚀 API resumidor de texto

Esta aplicación es una API REST desarrollada con **FastAPI** que utiliza la inteligencia artificial de **Google Gemini** para generar resúmenes de textos, ademas se tiene implementado un sistema de almacenamiento de historial asíncrono en **Google BigQuery**.

Proyecto realizado como parte del Challenge.

## 📋 Características

* **API REST:** Construida con FastAPI.
* **IA Generativa:** Integración con Google Gemini.
* **Data:** Guardado de historial en BigQuery.
* **Performance:** Ejecución asíncrona (`async/await`) y Tareas en Segundo Plano (`BackgroundTasks`).
* **DevOps:** Contenerizada con Docker y CI/CD con GitHub Actions a Cloud Run.
* **Calidad:** Validación de datos con Pydantic y manejo robusto de errores.

---

## 🛠️ Requisitos previos para ejecutar localmente con Docker

Para ejecutar este proyecto necesitas:

* Docker instalado
* Python 3.12.1 (solo si es para ejecución local sin Docker)
* Una API Key de Google AI Studio
* (Opcional) Credenciales de Google Cloud con acceso a BigQuery

---

## ⚙️ Configuración del Entorno

1. Clona el repositorio:
   ```bash
   git clone https://github.com/DavidDG21/prueba_tecnica_tottus.git
   cd prueba_tecnica_tottus

2. Crea un archivo .env en la raíz del proyecto, de esta manera:
    ```bash
   # .env
    API_KEY_GEMINI=tu_api_key_aqui (obligatorio)
    ID_GOOGLE_CLOUD_PROJECT=id_de_tu_proyecto_gcp (opcional, dejarlo vacio)

---

## 💻 Ejecución Local sin Docker (Python)

Correr la aplicación directamente en local:

1. Instalar dependencias:
    ```bash
    pip install -r requirements.txt

2. Iniciar el servidor:
    ```bash
    uvicorn app.main:app --reload

3. Verificar: La API estará disponible en: http://127.0.0.1:8000 y la documentación: http://127.0.0.1:8000/docs

## Ejecución con Docker
1. Construir la imagen con el siguiente comando:
    ```bash
    docker build -t prueba_tecnica_tottus .

2. Correr el contenedor
    ```bash
    docker run -d -p 8080:8080 \
    -e API_KEY_GEMINI="tu_api_key" \
    -e ID_GOOGLE_CLOUD_PROJECT="" \
    --name prueba_tecnica_tottus \
    prueba_tecnica_tottus

3. Acceder: Ve a http://localhost:8080/docs en tu navegador

## Como usar la API

**Endpoint: Generar Resumen**
* **URL:** http://localhost:8080/api/v1/resumen
* **Método:** POST

**Ejemplo de uso, en una terminal de bash:**
Para evitar problemas con caracteres especiales y comillas en la terminal (especialmente en Windows), se recomienda usar el archivo `input.json` incluido:

    ```bash
    curl -X POST http://localhost:8080/api/v1/resumen \
     -H "Content-Type: application/json" \
     -d @input.json

## Ejemplos de peticiones y respuestas

### 1. Petición exitosa (200 OK)
**Cuerpo de la Petición (`POST /api/v1/resumen`):**

```json
{
  "text": "Donald Trump quiere que Estados Unidos posea Groenlandia y este sábado anunció aranceles contra 8 países europeos que se han mostrado contrarios a sus ambiciones y han enviado en los últimos días tropas a la isla del Ártico. El mandatario estadounidense insiste en que su país necesita Groenlandia por motivos de seguridad nacional y no ha descartado incluso tomarla por la fuerza. No es la primera vez que Estados Unidos busca anexionarse un territorio danés. Hace más de 100 años, lejos del frío polar de Groenlandia, en el calor del Caribe, unas pequeñas islas iban a pasar de pertenecer a Dinamarca a convertirse en una posesión de Estados Unidos."
}
```
**Respuesta Exitosa:**

```json
{
  "summary": "Aquí tienes un resumen conciso y estructurado del texto:\n\nDonald Trump busca la anexión de **Groenlandia** a EE. UU. por razones de seguridad nacional, sin descartar el uso de la fuerza. Ante la oposición de **ocho países europeos** que han enviado tropas al Ártico, el mandatario anunció la imposición de **aranceles** contra dichas naciones. El texto destaca que esta ambición tiene un **precedente histórico**, pues hace un siglo Estados Unidos ya adquirió territorios daneses en el Caribe.",
  "original_length": 651
}
```

### 2. Error de Validación (422)
Ocurre cuando el texto enviado no cumple con el mínimo de 30 caracteres o si viene vacío.

**Cuerpo de la Petición:**
```json
{
  "text": "Texto muy corto"
}
```

**Respuesta de Error:**
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "text"],
      "msg": "String should have at least 30 characters",
      "input": "Texto muy corto"
    }
  ]
}
```

### 3. Error de Servicio (500 Internal Server Error)
Ocurre si hay un problema con la API key o con la API de gemini

**Respuesta de Error:**
```json
{
  "detail": "La API de Gemini devolvió una respuesta vacía o fue bloqueada por filtros de seguridad."
}
```

## 📂 Estructura del Proyecto

```text
prueba_tecnica_tottus/
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
│       └── api_v1.py           # Definición de endpoints (POST /resumen)
|__ .github/
│   └── workflows
|       └── deploy-prod.yml     # Pipeline CI/CD para build y despliegue a Cloud Run
├── .dockerignore               
├── .env                        # Variables de entorno para local
├── .gitignore                  
├── Dockerfile                  # Definición del contenedor
├── input.json                  # Datos de prueba para validación rápida
├── README.md
└── requirements.txt            # Dependencias del proyecto
```