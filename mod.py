from pydantic import BaseModel
from typing import Dict

class Student(BaseModel):
    name: str
    sbj_scores: Dict[str, float]
    average: float = 0.0
    grade: str = ""