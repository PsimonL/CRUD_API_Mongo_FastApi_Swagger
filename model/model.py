# from schematics.models import Model
from pydantic import BaseModel


class DataTemplate(BaseModel):
    id: int
    name: str
    counter: int