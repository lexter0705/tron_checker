from pydantic import BaseModel, constr


class RequestInfo(BaseModel):
    id: int
    ip_address: str
    port: int
    address: constr(min_length=34, max_length=34)
