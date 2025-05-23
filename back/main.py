from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API personagens de tvd")

# CORS settings para permitir chamadas do front-end

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo as rotas da API
app.include_router(api_router, prefix=settings.API_V1_STR)

# Isso garante que funcione tanto com `python main.py` quanto com `uvicorn main:app --reload`
#if __name__ == "__main__":
   # import uvicorn
   # uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="info", reload=True)


