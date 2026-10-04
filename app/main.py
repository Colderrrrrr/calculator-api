import math
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


VERSION = (Path(__file__).resolve().parent.parent / "VERSION").read_text().strip()


app = FastAPI(
    title="Calculator API",
    description="REST API калькулятор",
    version=VERSION
)


@app.exception_handler(RequestValidationError)
async def validation_error(request: Request, exc: RequestValidationError):
    # стандартный обработчик возвращает присланное значение обратно
    errors = [
        {"loc": [str(part) for part in error["loc"]], "msg": error["msg"]}
        for error in exc.errors()
    ]

    return JSONResponse(status_code=422, content={"detail": errors})


class CalculationRequest(BaseModel):
    # без allow_inf_nan=False значение 1e400 становится inf
    a: float = Field(allow_inf_nan=False)
    b: float = Field(allow_inf_nan=False)
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

    try:
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

    except ZeroDivisionError:
        # 0 ** -1
        raise HTTPException(
            status_code=400,
            detail="Division by zero is not allowed"
        )

    except OverflowError:
        # 1e308 ** 2
        raise HTTPException(
            status_code=400,
            detail="Result is too large"
        )

    if isinstance(result, complex) or not math.isfinite(result):
        raise HTTPException(
            status_code=400,
            detail="Result is not a finite real number"
        )

    return {
        "result": result
    }
