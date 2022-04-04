from fastapi import FastAPI

from endpoints.websites import websites_endpoint
from endpoints.categories import categories_endpoint

app = FastAPI(title="API for UpChecker",
              swagger_ui_parameters={"defaultModelsExpandDepth": -1},
              openapi_url="/api/openapi.json",
              docs_url="/api/docs",
              redoc_url=None
              )


app.include_router(websites_endpoint, prefix="/api/websites")
app.include_router(categories_endpoint, prefix="/api/categories")
