import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get("/api/calculate")
def calculate(x:int, y:int, z:int):
    value = (x+y)*z

    return {
        "value":value
    }

uvicorn.run(api)