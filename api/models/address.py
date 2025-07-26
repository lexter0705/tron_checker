from pydantic import BaseModel, constr


class Address(BaseModel):
    address: constr(min_length=34, max_length=34)
