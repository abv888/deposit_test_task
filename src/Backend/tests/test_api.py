import pytest
from conftest import client


class TestDepositAPI:
    def test_calculate_deposit_one_mont(self):
        response = client.post("/deposit", json={"date": "31.12.2021", "period": 1, "amount": 10000, "rate": 6})
        assert response.status_code == 200
        assert response.json() == {'31.01.2022': 10050.0}

    def test_calculate_deposit_two_mont(self):
        response = client.post("/deposit", json={"date": "31.01.2021", "period": 36, "amount": 10000, "rate": 6})
        assert response.status_code == 200
        assert response.json() == {
            '28.02.2021': 10050.0,
            '31.03.2021': 10100.25,
            '30.04.2021': 10150.75,
            '31.05.2021': 10201.51,
            '30.06.2021': 10252.51,
            '31.07.2021': 10303.78,
            '31.08.2021': 10355.29,
            '30.09.2021': 10407.07,
            '31.10.2021': 10459.11,
            '30.11.2021': 10511.4,
            '31.12.2021': 10563.96,
            '31.01.2022': 10616.78,
            '28.02.2022': 10669.86,
            '31.03.2022': 10723.21,
            '30.04.2022': 10776.83,
            '31.05.2022': 10830.71,
            '30.06.2022': 10884.87,
            '31.07.2022': 10939.29,
            '31.08.2022': 10993.99,
            '30.09.2022': 11048.96,
            '30.11.2022': 11159.72,
            '31.10.2022': 11104.2,
            '31.12.2022': 11215.52,
            '31.01.2023': 11271.6,
            '28.02.2023': 11327.96,
            '31.03.2023': 11384.6,
            '30.04.2023': 11441.52,
            '31.05.2023': 11498.73,
            '30.06.2023': 11556.22,
            '31.07.2023': 11614.0,
            '31.08.2023': 11672.07,
            '30.09.2023': 11730.43,
            '31.10.2023': 11789.08,
            '30.11.2023': 11848.03,
            '31.12.2023': 11907.27,
            '31.01.2024': 11966.81
        }

    def test_calculate_deposit_max_rate(self):
        response = client.post("/deposit", json={"date": "31.12.2021", "period": 1, "amount": 10000, "rate": 8})
        assert response.status_code == 200
        assert response.json() == {'31.01.2022': 10066.67}

    def test_calculate_deposit_min_rate(self):
        response = client.post("/deposit", json={"date": "31.12.2021", "period": 1, "amount": 10000, "rate": 1})
        assert response.status_code == 200
        assert response.json() == {'31.01.2022': 10008.33}

    def test_calculate_deposit_max_amount(self):
        response = client.post("/deposit", json={"date": "31.12.2021", "period": 1, "amount": 1000000, "rate": 6})
        assert response.status_code == 200
        assert response.json() == {'31.01.2022': 1005000.0}

    def test_calculate_deposit_min_amount(self):
        response = client.post("/deposit", json={"date": "31.12.2021", "period": 1, "amount": 10000, "rate": 6})
        assert response.status_code == 200
        assert response.json() == {'31.01.2022': 10050.0}

    def test_calculate_deposit_loss_data(self):
        response = client.post("/deposit", json={})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Данные отсутствуют'}

    def test_calculate_deposit_loss_date(self):
        response = client.post("/deposit", json={"period": 30, "amount": 11000, "rate": 4})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Дата отсутствует'}

    def test_calculate_deposit_loss_period(self):
        response = client.post("/deposit", json={"date": "31.02.2021", "amount": 11000, "rate": 4})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Период отсутствует'}

    def test_calculate_deposit_loss_amount(self):
        response = client.post("/deposit", json={"date": "31.02.2021", "period": 30, "rate": 4})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Вклад отсутствует'}

    def test_calculate_deposit_bad_day(self):
        response = client.post("/deposit", json={"date": "31.02.2021", "period": 4, "amount": 15000, "rate": 6})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Некоректная дата'}

    def test_calculate_deposit_multi_error(self):
        response = client.post("/deposit", json={"date": "2021-01-01", "period": 61, "amount": 9999, "rate": 9})
        assert response.status_code == 400
        assert response.json() == {
            'error': 'Value error, Некоректная дата | Value error, Периуд должен быть от 1 до 60 месяцев |'
                     ' Value error, Вклад должен быть от 10000 до 1000000 | '
                     'Value error, Процентная ставка должна быть от 1 до 8'}

    def test_calculate_deposit_less_min_period(self):
        response = client.post("/deposit", json={"date": "01.01.2021", "period": 0, "amount": 15000, "rate": 6})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Периуд должен быть от 1 до 60 месяцев'}

    def test_calculate_deposit_more_max_period(self):
        response = client.post("/deposit", json={"date": "01.01.2021", "period": 61, "amount": 15000, "rate": 6})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Периуд должен быть от 1 до 60 месяцев'}


    def test_calculate_deposit_less_min_rate(self):
        response = client.post("/deposit", json={"date": "01.01.2021", "period": 4, "amount": 15000, "rate": 0})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Процентная ставка должна быть от 1 до 8'}

    def test_calculate_deposit_more_max_rate(self):
        response = client.post("/deposit", json={"date": "01.01.2021", "period": 4, "amount": 15000, "rate": 9})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Процентная ставка должна быть от 1 до 8'}

    def test_calculate_deposit_less_min_amount(self):
        response = client.post("/deposit", json={"date": "01.01.2021", "period": 4, "amount": 9999, "rate": 6})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Вклад должен быть от 10000 до 1000000'}

    def test_calculate_deposit_more_max_amount(self):
        response = client.post("/deposit", json={"date": "01.01.2021", "period": 4, "amount": 1000001, "rate": 6})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Вклад должен быть от 10000 до 1000000'}


    def test_calculate_deposit_bad_period(self):
        response = client.post("/deposit", json={"date": "01.01.2021", "period": "4", "amount": 15000, "rate": 6})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Период должен быть целым числом'}

    def test_calculate_deposit_bad_amount(self):
        response = client.post("/deposit", json={"date": "01.01.2021", "period": 4, "amount": "15000", "rate": 6})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Вклад должен быть числом'}

    def test_calculate_deposit_bad_rate(self):
        response = client.post("/deposit", json={"date": "01.01.2021", "period": 4, "amount": 15000, "rate": "6"})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Ставка должна быть числом'}

    def test_calculate_deposit_bad_multi(self):
        response = client.post("/deposit", json={"date": "01.01.2021", "period": "4", "amount": "15000", "rate": "6"})
        assert response.status_code == 400
        assert response.json() == {'error': 'Value error, Период должен быть целым числом | Вклад должен быть числом | Ставка должна быть числом'}