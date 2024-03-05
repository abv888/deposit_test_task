from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from decimal import *


class DepositsSettings (BaseModel):
    max_period: int = 60
    min_period: int = 1
    max_amount: float = 1000000
    min_amount: float = 10000
    max_rate: float = 8
    min_rate: float = 1


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000

    deposits_settings: DepositsSettings = DepositsSettings()




    model_config = SettingsConfigDict(env_prefix='main_', env_nested_delimiter='__')
settings = Settings()
