from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from app.painel_template.app import app_dash

app = FastAPI()

@app.get("/")
async def root():
    return {"Underberg mercado"}

# Now mount you dash server into main fastapi application
app.mount("/dash", WSGIMiddleware(app_dash.server))

