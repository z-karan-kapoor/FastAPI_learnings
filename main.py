from fastapi import FastAPI
from src.configs.meta_data import MetaData
from src.routes import user_routes,item_routes,login
from src.templates import items_template,users_template,auth
from fastapi.staticfiles import StaticFiles

tags = [{"name": "user"},{"name": "items"},{"name": "database"}]

app = FastAPI(
    title=MetaData.settings['TITLE'],
    version=MetaData.settings['VERSION'],
    description=MetaData.settings['DESCRIPTION'],
    openapi_tags=tags,
    openapi_url="/api/v1/openapi.json",
    contact={
        "name": MetaData.settings['NAME'],
        "email": MetaData.settings['EMAIL']
    },
    # redoc_url=None 
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(user_routes.router)
app.include_router(item_routes.router)
app.include_router(login.router)
app.include_router(items_template.router)
app.include_router(users_template.router)
app.include_router(auth.router)


