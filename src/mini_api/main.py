from fastapi import FastAPI

app = FastAPI(title="Mini API DevSecOps", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Return the service health status."""
    return {"status": "ok"}


@app.get("/api/v1/sum")
def add(a: int, b: int) -> dict[str, int]:
    """Add two integers."""
    return {"result": a + b}

