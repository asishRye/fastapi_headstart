from fastapi import APIRouter

router = APIRouter()


@router.get("/websocket_index", tags=["websockets"])
def socket_index():
    return {"message": "Websocket routing works"}
