from app import get_options_for_key
from common.consts import *
from static import test_data


def test_prereqs_no_model3_for_40():
    context = {CAPACITY_OPTION_KEY: "40 kWh"}

    options, _ = get_options_for_key(
        WHEELS_OPTION_KEY,
        context,
        test_data.options_prices,
        test_data.options_restrictions,
        test_data.get_default_context(),
    )

    assert options == [
        {"label": "Model 1", "value": "Model 1"},
        {"label": "Model 2", "value": "Model 2"},
    ]


def test_prereqs_model3_for_60():
    context = {CAPACITY_OPTION_KEY: "60 kWh"}

    options, _ = get_options_for_key(
        WHEELS_OPTION_KEY,
        context,
        test_data.options_prices,
        test_data.options_restrictions,
        test_data.get_default_context(),
    )

    assert options == [
        {"label": "Model 1", "value": "Model 1"},
        {"label": "Model 2", "value": "Model 2"},
        {"label": "Model 3", "value": "Model 3"},
    ]


def test_prereqs_model3_for_80():
    context = {CAPACITY_OPTION_KEY: "80 kWh"}

    options, _ = get_options_for_key(
        WHEELS_OPTION_KEY,
        context,
        test_data.options_prices,
        test_data.options_restrictions,
        test_data.get_default_context(),
    )

    assert options == [
        {"label": "Model 1", "value": "Model 1"},
        {"label": "Model 2", "value": "Model 2"},
        {"label": "Model 3", "value": "Model 3"},
    ]


def test_prereqs_only_eco_for_model_1():
    context = {WHEELS_OPTION_KEY: "Model 1"}

    options, _ = get_options_for_key(
        TIRES_OPTION_KEY,
        context,
        test_data.options_prices,
        test_data.options_restrictions,
        test_data.get_default_context(),
    )

    assert options == [{"label": "Eco", "value": "Eco"}]


def test_prereqs_no_racing_for_model_2():
    context = {WHEELS_OPTION_KEY: "Model 2"}

    options, _ = get_options_for_key(
        TIRES_OPTION_KEY,
        context,
        test_data.options_prices,
        test_data.options_restrictions,
        test_data.get_default_context(),
    )

    assert options == [
        {"label": "Eco", "value": "Eco"},
        {"label": "Performance", "value": "Performance"},
    ]


def test_prereqs_racing_for_model_3():
    context = {WHEELS_OPTION_KEY: "Model 3"}

    options, _ = get_options_for_key(
        TIRES_OPTION_KEY,
        context,
        test_data.options_prices,
        test_data.options_restrictions,
        test_data.get_default_context(),
    )

    assert options == [
        {"label": "Eco", "value": "Eco"},
        {"label": "Performance", "value": "Performance"},
        {"label": "Racing", "value": "Racing"},
    ]
