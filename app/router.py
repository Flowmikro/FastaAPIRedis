import redis
from fastapi import APIRouter, HTTPException

from .schemas import UserSchema


redis_client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
router = APIRouter()


@router.get("/check_data")
def check_data(phone: str) -> dict:
    """
    Выводит значение по ключу phone
    """
    address = redis_client.get(phone)
    if address:
        return {"phone": phone, "address": address}
    else:
        raise HTTPException(status_code=404, detail="Номер не найден")


@router.post("/write_data")
def write_data(user: UserSchema) -> UserSchema:
    """
    Создает запись в Redis
    """
    redis_client.set(user.phone, user.address)
    return user


@router.put("/write_data")
def update_data(user: UserSchema) -> dict:
    """
    Обновляет значение по ключу phone
    """
    if redis_client.exists(user.phone):
        redis_client.set(user.phone, user.address)
        return {"message": "Данные успешно обновлены"}
    else:
        raise HTTPException(status_code=404, detail="Номер телефона не найден")
