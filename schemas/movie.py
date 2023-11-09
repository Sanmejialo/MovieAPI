from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le= 2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)

    model_config = {
        "json_schema_extra":{
            "example": {
            "id": 1,
            "title": "Nueva Pelicula",
            "overview": "Descipción nueva pelicula",
            "year": 2023,
            "rating": 9.7,
            "category": "Accion"
            }
        }
    }