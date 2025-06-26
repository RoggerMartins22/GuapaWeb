from fastapi import FastAPI
from routers import usuario, ping

app = FastAPI()


app.include_router(usuario.router)
app.include_router(ping.router)