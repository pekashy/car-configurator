from datetime import timezone, timedelta

from common.consts import *
from typing import Dict


"""
    In real application I wold store this data somewhere in DB and make an interface for PMs/Managers to edit it.
"""


DEFAULT_PRICE = 12000

__capacity_prices = {
    "40 kWh": 0,
    "60 kWh": 2500,
    "80 kWh": 6000,
}

__wheel_prices = {
    "Model 1": 0,
    "Model 2": 150,
    "Model 3": 350,
}

__tires_prices = {
    "Eco": 0,
    "Performance": 80,
    "Racing": 150,
}

__capacity_restrictions = {}

__wheel_restrictions = {"Model 3": {CAPACITY_OPTION_KEY: {"40 kWh"}}}

__tires_restrictions = {
    "Performance": {WHEELS_OPTION_KEY: {"Model 1"}},
    "Racing": {WHEELS_OPTION_KEY: {"Model 1", "Model 2"}},
}

options_prices = {
    CAPACITY_OPTION_KEY: __capacity_prices,
    WHEELS_OPTION_KEY: __wheel_prices,
    TIRES_OPTION_KEY: __tires_prices,
}

options_restrictions = {
    CAPACITY_OPTION_KEY: __capacity_restrictions,
    TIRES_OPTION_KEY: __tires_restrictions,
    WHEELS_OPTION_KEY: __wheel_restrictions,
}


def get_default_context() -> Dict[str, str]:
    return {
        CAPACITY_OPTION_KEY: "40 kWh",
        WHEELS_OPTION_KEY: "Model 1",
        TIRES_OPTION_KEY: "Eco",
    }


__timezone_offset = 1  # Berlin
tzinfo = timezone(timedelta(hours=__timezone_offset))
