from fastapi import FastAPI
from api.apis import routers


def create_app():
    app = FastAPI()
    return app


app = create_app()
app.include_router(routers)
