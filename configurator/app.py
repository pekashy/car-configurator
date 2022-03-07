import dash
import dash_bootstrap_components as dbc
import flask
from dash import dcc, html, Input, Output, State, callback
from common.consts import *
from request import send_configuration, count_processed
from configurator_elements import configurator_layout, create_configuration_layout_options

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
dcc.Store(id="intermediate-value")
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(
    Output(component_id="configuration-layout", component_property="children"),
    Input(component_id="capacity_radio", component_property="value"),
    Input(component_id="wheels_radio", component_property="value"),
    Input(component_id="tires_radio", component_property="value"),
)
def update_output_div(capacity_option, wheels_option, tires_option):
    context = {
        CAPACITY_OPTION_KEY: capacity_option,
        WHEELS_OPTION_KEY: wheels_option,
        TIRES_OPTION_KEY: tires_option,
    }
    return create_configuration_layout_options(context)


@app.callback(
    Output(component_id="submit_result", component_property="children"),
    State(component_id="capacity_radio", component_property="value"),
    State(component_id="wheels_radio", component_property="value"),
    State(component_id="tires_radio", component_property="value"),
    State(component_id="name_input", component_property="value"),
    Input(component_id="order_submit", component_property="n_clicks"),
)
def update_output_div(
        capacity_option, wheels_option, tires_option, name_input, n_clicks
):
    if not n_clicks or n_clicks == 0 or not name_input:
        return "Choose your configuration, enter your name and press Order"
    request_data = {
        CAPACITY_OPTION_KEY: capacity_option,
        WHEELS_OPTION_KEY: wheels_option,
        TIRES_OPTION_KEY: tires_option,
        "name": name_input,
    }
    return send_configuration(request_data)


@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/configure":
        return configurator_layout()
    if pathname == "/report":
        return count_processed()
    return pathname


if __name__ == "__main__":
    import os

    debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True
    app.run_server(host="0.0.0.0", port=8050, debug=debug)
