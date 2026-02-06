from pydantic import BaseModel

class ApiResponse(BaseModel):
    ok: bool
    time_taken: float | None = None
    data: dict | None = None
    error: str | None = None
