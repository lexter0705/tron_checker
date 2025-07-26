from pydantic import BaseModel


class Config(BaseModel):
    database_url: str
    tron_api_endpoint: str
    tron_api_key: str
