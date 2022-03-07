import datetime
from app import get_default_price
from static import test_data


def test_ordinary_day():
    date = datetime.datetime(2001, 1, 1, tzinfo=test_data.tzinfo)

    default_price = get_default_price(date, test_data.DEFAULT_PRICE)

    assert default_price == test_data.DEFAULT_PRICE


def test_last_friday_day():
    date = datetime.datetime(2021, 6, 25, tzinfo=test_data.tzinfo)

    default_price = get_default_price(date, test_data.DEFAULT_PRICE)

    assert default_price == test_data.DEFAULT_PRICE - 2000
