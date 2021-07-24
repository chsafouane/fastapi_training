from typing import Optional
import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get("/")
def index():
    body = """
    <html>
    <p>Welcome to my first API using FastAPI</p>
    <p>To use the calculator, try:
    http://127.0.0.1:8000/api/calculate?x=2&y=3
    </html>
    """
    return fastapi.responses.HTMLResponse(
        content=body,
        status_code=200
    )

@api.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.responses.JSONResponse(
            content = {"error": "Error: z cannot be zero"},
            status_code = 400
        )


    value = x + y
    if z is not None:
        value /= z

    return {
        "x": x,
        "y": y,
        "z": z,
        "value": value
    }


uvicorn.run(api)