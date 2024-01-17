from pydantic import BaseModel, Field, validator


class AddressSchema(BaseModel):
    phone: str = Field('89099099090')
    address: str

    @validator('phone')
    def validate_phone(cls, phone):
        if not phone.isdigit() or len(phone) != 11:
            raise ValueError('Неверно заполнено поле phone')
        return phone
