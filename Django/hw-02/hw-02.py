from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator


class Address(BaseModel):
    city: str = Field(..., min_length=2)
    street: str = Field(..., min_length=3)
    house_number: int = Field(..., gt=0)


class User(BaseModel):
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=0, lte=120)
    email: EmailStr
    is_employed: bool = True
    address: Address

    @field_validator('name')
    def validate_name(cls, value):
        if not value.isalpha():
            raise ValueError('Name must contain only letters')
        return value

    @field_validator('age')
    def validate_employment_age(cls, age):
        if 'is_employed' and not (18 <= age <= 65):
            raise ValueError('Employed users must be between 18 and 65 years old')
        return age


def process_user_registration(json_data: str):
    try:
        users = User.parse_raw(json_data)
        return users
    except ValidationError as err:
        return f"Validation error: {err}"


json_string = """
{
    "name": "Alice",
    "age": 20,
    "email": "alice@example.com",
    "is_employed": "True",
    "address": {
        "city": "Los Angeles",
        "street": "Sunset Boulevard",
        "house_number": 456
    }
}
"""

result = process_user_registration(json_string)
print(result)
