from fastapi import FastAPI, HTTPException
from mod import Student
from utils import read_records, save_records, calc_average_and_grade

app = FastAPI()

@app.post("/students/")
def add_student(student: Student):
    try:
        records = read_records()
        if student.name in records:
            raise HTTPException(status_code=400, detail="Student already exists")
        
        average, grade = calc_average_and_grade(student.subject_scores)
        student.average = average
        student.grade = grade
        
        records[student.name] = student.dict()
        save_records(records)
        
        return {"message": "Student added successfully", "student": student}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/students/{name}")
def get_student(name: str):
    try:
        records = read_records()
        if name not in records:
            raise HTTPException(status_code=404, detail="Student not found")
        
        student_data = records[name]
        return {"student": student_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/students/")
def get_all_students():
    try:
        records = read_records()
        return records
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))