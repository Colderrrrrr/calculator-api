from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


with open("VERSION") as f:
    VERSION = f.read().strip()


app = FastAPI(
    title="Calculator API",
    description="REST API калькулятор",
    version=VERSION
)


class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: str


class CalculationResponse(BaseModel):
    result: float


@app.get("/")
def root():
    return {
        "name": "Calculator API",
        "version": VERSION
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/calculate", response_model=CalculationResponse)
def calculate(request: CalculationRequest):

    if request.operation == "+":
        result = request.a + request.b

    elif request.operation == "-":
        result = request.a - request.b

    elif request.operation == "*":
        result = request.a * request.b

    elif request.operation == "/":
        if request.b == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed"
            )

        result = request.a / request.b

    elif request.operation == "**":
        result = request.a ** request.b

    else:
        raise HTTPException(
            status_code=400,
            detail="Unsupported operation"
        )

    return {
        "result": result
    }
