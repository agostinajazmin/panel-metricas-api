from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configura CORS para permitir todas las orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/metricas")
def get_metrics():
    return {
        "marketing": {
            "clics": 1250,
            "impresiones": 25000,
            "conversiones": 85,
            "roi": 3.45
        }
    }