from configs.database import SessionLocal, engine
from api.router import app
from loader import loader

# uvicorn main:app --host 192.168.0.18 --port 8001 --reload
