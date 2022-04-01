from fastapi import FastAPI


app = FastAPI(title="New FastAPI app",
	swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)


@app.get("/")
async def index():
    return {"ok":True}
