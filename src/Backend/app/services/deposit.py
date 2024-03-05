
from ..models.deposit import Deposit
from dateutil.relativedelta import relativedelta
def calculate_deposit(deposit_data: Deposit)-> dict[str, float]:
    """
    Calculate deposit
    :param deposit_data: Deposit
    :return: map[str][int]
    """
    current_deposit_amount = deposit_data.amount
    result = {}
    for i in range(deposit_data.period):
        current_deposit_amount *= (1 + deposit_data.rate / 100 / 12)
        result[str((deposit_data.st_date + relativedelta(months=i+1)).strftime("%d.%m.%Y"))] = round(current_deposit_amount, 2)
    return result


