from pydantic import BaseModel
from typing import Dict

class Student(BaseModel):
    name: str
    subject_scores: dict[str, float]
    average: float = 0.0
    grade: str = ""