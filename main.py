from fastapi import FastAPI

from app.router import router

app = FastAPI(name='API')


app.include_router(router, prefix='/api', tags=['/api'])
