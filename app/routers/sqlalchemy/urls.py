from fastapi import APIRouter, Request
from . import utils

router = APIRouter()


@router.get("/fetch", tags=["sqlalchemy"])
def get_records():
    utils.get_records()
    return {"message": "records fetched"}


@router.post("/insert", tags=["sqlalchemy"])
async def insert_records(request: Request):
    json_body = await request.json()
    utils.write_records(json_body)
    return {"message": "records inserted"}
