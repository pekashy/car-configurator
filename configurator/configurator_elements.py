from datetime import datetime
from typing import List, Dict, Any

from dash import dcc, html
from common.consts import *
from static import business_data
from calendar import monthrange


def is_forbidden(key, option, context, options_restrictions):
    option_restrictions = options_restrictions.get(key, {}).get(option, {})
    for restriction_key in options_keys:
        if restriction_key == key:
            continue
        context_val = context.get(restriction_key)
        options_restrictions_for_key = option_restrictions.get(restriction_key, {})
        if context_val in options_restrictions_for_key:
            return True

    return False


def get_options_for_key(
        key, context, options_prices, options_restrictions, default_options
) -> (List[Dict[str, Any]], str):
    available_options = [
        {"label": option, "value": option}
        for option in options_prices[key]
        if not is_forbidden(key, option, context, options_restrictions)
    ]
    if context.get(key) not in set(
            [option.get("label") for option in available_options]
    ):
        context[key] = default_options.get(key)
    return available_options, context.get(key)


def get_default_price(date, default_price) -> int:
    weekday = date.weekday()
    day = date.day
    days_left = day - monthrange(date.year, date.month)[1]
    if weekday == 4 and days_left < 7:
        return default_price - 2000
    return default_price


def calculate_price(context, options_prices):
    wheels_option = context[WHEELS_OPTION_KEY]
    wheels_price = options_prices[WHEELS_OPTION_KEY][wheels_option]
    tires_option = context[TIRES_OPTION_KEY]
    tires_price = options_prices[TIRES_OPTION_KEY][tires_option]
    capacity_option = context[CAPACITY_OPTION_KEY]
    capacity_price = options_prices[CAPACITY_OPTION_KEY][capacity_option]
    return (
            get_default_price(
                datetime.now(business_data.tzinfo), business_data.DEFAULT_PRICE
            )
            + wheels_price
            + tires_price
            + capacity_price
    )


def create_configuration_layout_options(context) -> []:
    default_options = business_data.get_default_context()
    capacity_options, current_capacity_option = get_options_for_key(
        CAPACITY_OPTION_KEY,
        context,
        business_data.options_prices,
        business_data.options_restrictions,
        default_options,
    )
    wheel_options, current_wheel_option = get_options_for_key(
        WHEELS_OPTION_KEY,
        context,
        business_data.options_prices,
        business_data.options_restrictions,
        default_options,
    )
    tires_options, current_tires_option = get_options_for_key(
        TIRES_OPTION_KEY,
        context,
        business_data.options_prices,
        business_data.options_restrictions,
        default_options,
    )
    price = calculate_price(context, business_data.options_prices)
    return [
        html.Div(children="""Total price: {}""".format(price)),
        dcc.RadioItems(
            id="capacity_radio", options=capacity_options, value=current_capacity_option
        ),
        dcc.RadioItems(
            id="wheels_radio", options=wheel_options, value=current_wheel_option
        ),
        dcc.RadioItems(
            id="tires_radio", options=tires_options, value=current_tires_option
        ),
        dcc.Input(id="name_input", type="text", placeholder="", debounce=True),
        html.Button("Order", id="order_submit"),
        html.Div(
            id="submit_result",
            children="Choose your configuration, enter your name and press Submit",
        ),
    ]


def configurator_layout():
    context = business_data.get_default_context()
    configuration_layout_options = create_configuration_layout_options(context)
    return html.Div(children=configuration_layout_options, id="configuration-layout")
