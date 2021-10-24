from fastapi import APIRouter, Request
from . import utils

router = APIRouter()


@router.get("/fetch/{id}", tags=["sqlalchemy"])
def get_records(id: int):
    db_results = utils.get_records(id)
    res = {
        "name": db_results.name,
        "age": db_results.age,
        "id": db_results.id,
        "grade": db_results.grade
    }
    return res


@router.post("/insert", tags=["sqlalchemy"])
async def insert_records(request: Request):
    json_body = await request.json()
    utils.write_records(json_body)
    return {"message": "records inserted"}
