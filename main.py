from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import router
from config import get_config

config = get_config()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
