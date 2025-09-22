import dash
from dash import html, dcc, Output, Input, State, dash_table
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
    ]
)

# Main layout with top tabs
app.layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            dbc.Col(html.H2("🐄 Swiss Cows 🐄", className="text-center text-white p-3"),
                    style={"backgroundColor": "#0d6efd"})
        ),

        dcc.Tabs(
            id="tabs",
            value="information",
            children=[
                dcc.Tab(label="Information", value="information"),
                dcc.Tab(label="Planning", value="planning"),
                dcc.Tab(label="Snapshot", value="snapshot")
            ],
        ),

        html.Div(id="tab-content", className="p-4"),
    ],
)


@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "value")
)
def render_tab(tab):
    if tab == "information":
        return dbc.Row(
            [
                dbc.Col(
                    dcc.Tabs(
                        id="info-sub-tabs",
                        value="personal",
                        vertical=True,
                        children=[
                            dcc.Tab(label="Personal Info", value="personal"),
                            dcc.Tab(label="Children", value="children"),
                            dcc.Tab(label="Income", value="income"),
                            dcc.Tab(label="Assets", value="assets"),
                            dcc.Tab(label="Expenses/Liabilities", value="expenses"),
                        ],
                    ),
                    width=2
                ),
                dbc.Col(
                    html.Div(id="info-sub-content"),
                    width=10
                )
            ]
        )
    elif tab == "planning":
        return html.Div([html.H3("Planning Page", className="text-center")])
    elif tab == "snapshot":
        return html.Div([html.H3("Snapshot Page", className="text-center")])


# Render sub-tab content
@app.callback(
    Output("info-sub-content", "children"),
    Input("info-sub-tabs", "value")
)
def render_info_subtab(subtab):
    if subtab == "personal":
        return dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            html.Div(html.I(className="fa-solid fa-person fa-6x text-primary"),
                                     className="text-center mb-3"),
                            html.H5("You", className="text-center mb-2"),
                            dcc.Input(id="user-age", type="number", placeholder="Age", min=0, max=120, step=1,
                                      className="form-control text-center"),
                            dcc.Dropdown(
                                id="user-gender",
                                options=[{"label": "Male", "value": "Male"}, {"label": "Female", "value": "Female"}],
                                placeholder="Select Gender"
                            )
                        ],
                        body=True,
                        className="p-4 text-center"
                    ),
                    width=6
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            html.Div(html.I(className="fa-solid fa-person-dress fa-6x text-danger"),
                                     className="text-center mb-3"),
                            html.H5("Spouse", className="text-center mb-2"),
                            dcc.Input(id="spouse-age", type="number", placeholder="Age", min=0, max=120, step=1,
                                      className="form-control text-center"),
                            dcc.Dropdown(
                                id="spouse-gender",
                                options=[{"label": "Male", "value": "Male"}, {"label": "Female", "value": "Female"}],
                                placeholder="Select Gender"
                            )
                        ],
                        body=True,
                        className="p-4 text-center"
                    ),
                    width=6
                ),
                dbc.Col(
                    dbc.Button("Next", id="personal-next", color="primary", className="d-block mx-auto mt-3"),
                    width=12
                )
            ]
        )
    elif subtab == "children":
        return html.Div(
            [
                html.H4("How many children do you have?", className="text-center mb-3"),
                html.Div(html.I(className="fa-solid fa-child fa-4x text-info"), className="text-center mb-3"),
                dcc.Input(id="num-children", type="number", placeholder="0", min=0, step=1,
                          className="form-control text-center", style={"width": "120px", "margin": "0 auto"}),
                html.Div(id="children-output", className="text-center mt-3 text-primary fw-bold")
            ]
        )
    elif subtab == "income":
        return html.Div(
            [
                html.H4("Enter sources of income", className="text-center mb-3"),
                dash_table.DataTable(
                    id='income-table',
                    columns=[
                        {"name": "Annual Income", "id": "income", "type": "numeric", "editable": True},
                        {"name": "Description", "id": "description", "type": "text", "editable": True},
                        {"name": "Passive or Active?", "id": "type", "type": "text", "editable": True},
                    ],
                    data=[{"income": 0, "description": "", "type": ""}],
                    editable=True,
                    row_deletable=True,
                    style_table={"margin": "0 auto", "width": "70%"},
                ),
                dbc.Button("Add Row", id="add-row", color="secondary", className="d-block mx-auto mt-3")
            ]
        )
    elif subtab == "assets":
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div(html.I(className="fa-solid fa-house fa-5x text-primary"),
                                             className="text-center mb-2"),
                                    html.H5("Home", className="text-center")
                                ],
                                id="asset-home",
                                n_clicks=0,
                                style={
                                    "border": "1px solid #ddd",
                                    "border-radius": "8px",
                                    "padding": "20px",
                                    "cursor": "pointer",
                                    "text-align": "center",
                                    "background-color": "#f8f9fa"
                                }
                            ),
                            width=4
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div(html.I(className="fa-solid fa-chart-line fa-5x text-success"),
                                             className="text-center mb-2"),
                                    html.H5("Stocks & Bonds", className="text-center")
                                ],
                                id="asset-stocks",
                                n_clicks=0,
                                style={
                                    "border": "1px solid #ddd",
                                    "border-radius": "8px",
                                    "padding": "20px",
                                    "cursor": "pointer",
                                    "text-align": "center",
                                    "background-color": "#f8f9fa"
                                }
                            ),
                            width=4
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div(html.I(className="fa-solid fa-gem fa-5x text-warning"),
                                             className="text-center mb-2"),
                                    html.H5("Unconventional", className="text-center")
                                ],
                                id="asset-unconventional",
                                n_clicks=0,
                                style={
                                    "border": "1px solid #ddd",
                                    "border-radius": "8px",
                                    "padding": "20px",
                                    "cursor": "pointer",
                                    "text-align": "center",
                                    "background-color": "#f8f9fa"
                                }
                            ),
                            width=4
                        ),
                    ],
                    justify="center"
                ),
                html.Div(id="asset-details", className="mt-4")
            ]
        )
    elif subtab == "expenses":
        return html.Div(
            [
                html.H4("Select a category", className="text-center mb-4"),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div(html.I(className="fa-solid fa-file-invoice-dollar fa-5x text-danger"),
                                             className="text-center mb-2"),
                                    html.H5("Liabilities", className="text-center")
                                ],
                                id="liabilities-card",
                                n_clicks=0,
                                style={
                                    "border": "1px solid #ddd",
                                    "border-radius": "8px",
                                    "padding": "20px",
                                    "cursor": "pointer",
                                    "text-align": "center",
                                    "background-color": "#f8f9fa"
                                }
                            ),
                            width=6
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div(html.I(className="fa-solid fa-wallet fa-5x text-primary"),
                                             className="text-center mb-2"),
                                    html.H5("Expenses", className="text-center")
                                ],
                                id="expenses-card",
                                n_clicks=0,
                                style={
                                    "border": "1px solid #ddd",
                                    "border-radius": "8px",
                                    "padding": "20px",
                                    "cursor": "pointer",
                                    "text-align": "center",
                                    "background-color": "#f8f9fa"
                                }
                            ),
                            width=6
                        ),
                    ],
                    justify="center",
                    className="mb-4"
                ),
                html.Div(id="expenses-liabilities-details")
            ]
        )


# Callbacks
@app.callback(
    Output('income-table', 'data'),
    Input('add-row', 'n_clicks'),
    State('income-table', 'data'),
    prevent_initial_call=True
)
def add_row(n, rows):
    rows.append({"income": 0, "description": "", "type": ""})
    return rows


@app.callback(
    Output("asset-details", "children"),
    Input("asset-home", "n_clicks"),
    Input("asset-stocks", "n_clicks"),
    Input("asset-unconventional", "n_clicks"),
    prevent_initial_call=True
)
def show_asset_details(home_click, stocks_click, unconventional_click):
    ctx = dash.callback_context
    if not ctx.triggered:
        return ""
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "asset-home":
        return dash_table.DataTable(
            id="home-table",
            columns=[
                {"name": "Home Type", "id": "home_type", "type": "text", "editable": True},
                {"name": "FMV", "id": "fmv", "type": "numeric", "editable": True},
                {"name": "Purchase Price", "id": "purchase_price", "type": "numeric", "editable": True},
                {"name": "Mortgage", "id": "mortgage", "type": "numeric", "editable": True},
                {"name": "Annual Property Tax", "id": "property_tax", "type": "numeric", "editable": True},
            ],
            data=[{"home_type": "", "fmv": 0, "purchase_price": 0, "mortgage": 0, "property_tax": 0}],
            editable=True,
            row_deletable=True,
            style_table={"margin": "0 auto", "width": "80%"},
        )
    elif button_id == "asset-stocks":
        return dash_table.DataTable(
            id="stocks-table",
            columns=[
                {"name": "Stock Name", "id": "stock_name", "type": "text", "editable": True},
                {"name": "Purchase Date", "id": "purchase_date", "type": "text", "editable": True},
                {"name": "Price", "id": "price", "type": "numeric", "editable": True},
                {"name": "FMV", "id": "fmv", "type": "numeric", "editable": True},
            ],
            data=[{"stock_name": "", "purchase_date": "", "price": 0, "fmv": 0}],
            editable=True,
            row_deletable=True,
            style_table={"margin": "0 auto", "width": "80%"},
        )
    elif button_id == "asset-unconventional":
        return html.Div("No input needed for unconventional assets.", className="text-center")


@app.callback(
    Output("expenses-liabilities-details", "children"),
    Input("liabilities-card", "n_clicks"),
    Input("expenses-card", "n_clicks"),
    prevent_initial_call=True
)
def show_expenses_liabilities(liab_click, exp_click):
    ctx = dash.callback_context
    if not ctx.triggered:
        return ""
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "liabilities-card":
        return dash_table.DataTable(
            id="liabilities-table",
            columns=[
                {"name": "Liability Type", "id": "type", "type": "text", "editable": True},
                {"name": "Outstanding Balance", "id": "balance", "type": "numeric", "editable": True},
                {"name": "Interest Rate (%)", "id": "rate", "type": "numeric", "editable": True},
                {"name": "Monthly Payment", "id": "payment", "type": "numeric", "editable": True},
            ],
            data=[{"type": "", "balance": 0, "rate": 0, "payment": 0}],
            editable=True,
            row_deletable=True,
            style_table={"margin": "0 auto", "width": "80%"},
        )
    elif button_id == "expenses-card":
        return dash_table.DataTable(
            id="expenses-table",
            columns=[
                {"name": "Expense Type", "id": "type", "type": "text", "editable": True},
                {"name": "Monthly Cost", "id": "cost", "type": "numeric", "editable": True},
            ],
            data=[{"type": "", "cost": 0}],
            editable=True,
            row_deletable=True,
            style_table={"margin": "0 auto", "width": "70%"},
        )


if __name__ == "__main__":
    app.run(debug=True)
