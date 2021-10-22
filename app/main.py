from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "2020"
    },
    2: {
        "name": "Doe",
        "age": 18,
        "class": "2021"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"message": "This is the index page"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, gt=0)):
    if student_id not in students:
        return {"error": "Student with provided id does not exist"}
    else:
        return students[student_id]


@app.get("/get-student-name")
def get_student_name(name: Optional[str] = None):
    for student in students:
        if students[student]["name"] == name:
            return students[student]
    return {"message": "Student not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "Student exists with given id"}

    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "Student with provided id does not exist"}
    else:
        if student.name is not None:
            students[student_id].name = student.name
        if student.age is not None:
            students[student_id].age = student.age
        if student.year is not None:
            students[student_id].year = student.year

        return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student with provided id does not exist"}
    else:
        del students[student_id]
        return {"message": "Student with provided id deleted"}
