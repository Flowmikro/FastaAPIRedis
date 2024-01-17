import redis
from fastapi import APIRouter, HTTPException

from .schemas import AddressSchema


redis_client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
router = APIRouter()


@router.get("/check_data")
def check_data(phone: str) -> dict:
    address = redis_client.get(phone)
    if address:
        return {"phone": phone, "address": address}
    else:
        raise HTTPException(status_code=404, detail="Номер не найден")


@router.post("/write_data")
def write_data(address: AddressSchema) -> AddressSchema:
    redis_client.set(address.phone, address.address)
    return address


@router.put("/write_data")
def update_data(address: AddressSchema) -> dict:
    if redis_client.exists(address.phone):
        redis_client.set(address.phone, address.address)
        return {"message": "Данные успешно обновлены"}
    else:
        raise HTTPException(status_code=404, detail="Номер телефона не найден")
