from pydantic import BaseModel, Field, validator


class UserSchema(BaseModel):
    phone: str = Field('89099099090')  # в строке могут быть только цифры и длина должна быть 11 символов
    address: str

    @validator('phone')
    def validate_phone(cls, phone):
        if not phone.isdigit() or len(phone) != 11:
            raise ValueError('Неверно заполнено поле phone')
        return phone
