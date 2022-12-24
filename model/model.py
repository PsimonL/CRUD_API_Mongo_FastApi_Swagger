# from schematics.models import Model
from pydantic import BaseModel


class DataTemplate(BaseModel):
    country: str
    city: str
    name: str
    net_worth: int
