from typing import Any

from fastapi import HTTPException
from pydantic import BaseModel, field_validator, Field, ValidationError , validator, model_validator
from datetime import date, datetime
from ..settings import settings



class Deposit(BaseModel):
    st_date: date = Field(alias='date', examples=["13.01.1998"])
    period: int = Field(alias='period', examples=[1, 60])
    amount: float = Field(alias='amount', examples=[10000, 1000000])
    rate: float = Field(alias='rate', examples=[6, 8])

    @staticmethod
    def _range_validator(v:int|float, min_value:int|float, max_value:int|float, message:str):
        if v < min_value or v > max_value:
            raise ValueError(message)
        return v

    @model_validator(mode='before')
    def check_card_number_omitted(cls, data: Any) -> Any:
        err=[]
        if  not isinstance(data, dict) or len(data.keys())==0 :
            raise ValueError('Данные отсутствуют')

        if data.get('date') is None:
            err.append('Дата отсутствует')

        if data.get('period') is None:
            err.append('Период отсутствует')
        elif not isinstance(data.get('period'), int):
            err.append('Период должен быть целым числом')

        if data.get('amount') is None:
            err.append('Вклад отсутствует')
        elif not isinstance(data.get('amount'), (int, float)):
            err.append('Вклад должен быть числом')

        if data.get('rate') is None:
            err.append('Ставка отсутствует')
        elif not isinstance(data.get('rate'), (int, float)):
            err.append('Ставка должна быть числом')

        if len(err) == 1:
            raise ValueError(err[0])
        if len(err) >1:
            raise ValueError(' | '.join(err))
        return data



    @field_validator('st_date',mode='before')
    def date_validator(cls, v):
        try:
            return datetime.strptime(v, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError('Некоректная дата')


    @field_validator('period')
    def period_validator(cls, v):
        return cls._range_validator(v, settings.deposits_settings.min_period, settings.deposits_settings.max_period,
                                    f'Периуд должен быть от {settings.deposits_settings.min_period } '
                                    f'до {settings.deposits_settings.max_period } месяцев')

    @field_validator('amount')
    def amount_validator(cls, v):
        return cls._range_validator(v, settings.deposits_settings.min_amount, settings.deposits_settings.max_amount,
                                    f'Вклад должен быть от {settings.deposits_settings.min_amount} '
                                    f'до {settings.deposits_settings.max_amount}')



    @field_validator('rate')
    def rate_validator(cls, v):
        return cls._range_validator(v, settings.deposits_settings.min_rate, settings.deposits_settings.max_rate,
                                    f'Процентная ставка должна быть от {settings.deposits_settings.min_rate} '
                                    f'до {settings.deposits_settings.max_rate}'
                                    )
