
import pytest
from src.Backend.app.models.deposit import Deposit
from datetime import date

class TestDTODepositCorrect:
    def test_data(self):
        deposit = Deposit(date="01.01.2021", period=4, amount=15000, rate=6)
        assert deposit.st_date ==  date.fromisoformat("2021-01-01")
        assert deposit.period == 4
        assert deposit.amount == 15000
        assert deposit.rate == 6

    def test_min_amount(self):
        deposit = Deposit(date="01.01.2021", period=4, amount=10000, rate=6)
        assert deposit.st_date ==  date.fromisoformat("2021-01-01")
        assert deposit.period == 4
        assert deposit.amount == 10000
        assert deposit.rate == 6

    def test_max_amount(self):
        deposit = Deposit(date="01.01.2021", period=4, amount=1000000, rate=6)
        assert deposit.st_date ==  date.fromisoformat("2021-01-01")
        assert deposit.period == 4
        assert deposit.amount == 1000000
        assert deposit.rate == 6

    def test_min_period(self):
        deposit = Deposit(date="01.01.2021", period=1, amount=15000, rate=6)
        assert deposit.st_date ==  date.fromisoformat("2021-01-01")
        assert deposit.period == 1
        assert deposit.amount == 15000
        assert deposit.rate == 6

    def test_max_period(self):
        deposit = Deposit(date="01.01.2021", period=60, amount=15000, rate=6)
        assert deposit.st_date ==  date.fromisoformat("2021-01-01")
        assert deposit.period == 60
        assert deposit.amount == 15000
        assert deposit.rate == 6

    def test_min_rate(self):
        deposit = Deposit(date="01.01.2021", period=4, amount=15000, rate=1)
        assert deposit.st_date ==  date.fromisoformat("2021-01-01")
        assert deposit.period == 4
        assert deposit.amount == 15000
        assert deposit.rate == 1

    def test_max_rate(self):
        deposit = Deposit(date="01.01.2021", period=4, amount=15000, rate=8)
        assert deposit.st_date ==  date.fromisoformat("2021-01-01")
        assert deposit.period == 4
        assert deposit.amount == 15000
        assert deposit.rate == 8

class TestDTODepositIncorrect:
    def test_less_min_amount(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="01.01.2021", period=4, amount=9999, rate=6)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Вклад должен быть от 10000 до 1000000'

    def test_more_max_amount(self):
        with pytest.raises(ValueError)  as ex:
            deposit = Deposit(date="01.01.2021", period=4, amount=1000001, rate=6)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Вклад должен быть от 10000 до 1000000'

    def test_less_min_period(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="01.01.2021", period=0, amount=15000, rate=6)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Периуд должен быть от 1 до 60 месяцев'

    def test_more_max_period(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="01.01.2021", period=61, amount=15000, rate=6)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Периуд должен быть от 1 до 60 месяцев'

    def test_less_min_rate(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="01.01.2021", period=4, amount=15000, rate=0)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Процентная ставка должна быть от 1 до 8'

    def test_more_max_rate(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="01.01.2021", period=4, amount=15000, rate=9)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Процентная ставка должна быть от 1 до 8'

    def test_date_bad_day(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="31.02.2021", period=4, amount=15000, rate=6)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Некоректная дата'

    def test_date_bad_format(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="2021-01-01", period=4, amount=15000, rate=6)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Некоректная дата'

    def test_multi_error(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="2021-01-01", period=61, amount=9999, rate=9)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Некоректная дата'
        assert str(ex.value.errors()[1]['msg']) == 'Value error, Периуд должен быть от 1 до 60 месяцев'
        assert str(ex.value.errors()[2]['msg']) ==  'Value error, Вклад должен быть от 10000 до 1000000'
        assert str(ex.value.errors()[3]['msg']) == 'Value error, Процентная ставка должна быть от 1 до 8'

    def test_loss_data(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit()
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Данные отсутствуют'

    def test_loss_date(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(period=30, amount=11000, rate=4)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Дата отсутствует'

    def test_loss_period(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="31.02.2021", amount=11000, rate=4)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Период отсутствует'


    def test_loss_amount(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="31.02.2021", period=30, rate=4)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Вклад отсутствует'


    def test_loss_rate(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="31.02.2021", period=30, amount=11000)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Ставка отсутствует'

    def test_loss_two_data(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="31.02.2021", period=30)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Вклад отсутствует | Ставка отсутствует'

    def test_loss_three_data(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="31.02.2021")
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Период отсутствует | Вклад отсутствует | Ставка отсутствует'

    def test_bad_period(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="31.02.2021", period='3', amount=11000, rate=4)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Период должен быть целым числом'

    def test_bad_amount(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="31.02.2021", period=30, amount='11000', rate=4)
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Вклад должен быть числом'

    def test_bad_rate(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="31.02.2021", period=30, amount=11000, rate='4')
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Ставка должна быть числом'

    def test_bad_all(self):
        with pytest.raises(ValueError) as ex:
            deposit = Deposit(date="31.02.2021", period='3', amount='11000', rate='4')
        assert str(ex.value.errors()[0]['msg']) == 'Value error, Период должен быть целым числом | Вклад должен быть числом | Ставка должна быть числом'