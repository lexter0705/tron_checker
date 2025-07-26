from pydantic import BaseModel, conint, confloat, constr


class WalletInfo(BaseModel):
    address: constr(min_length=34, max_length=34)
    balance: confloat(ge=0)
    bandwidth: conint(ge=0)
    energy: conint(ge=0)
