import dash
from dash import html, dcc, Output, Input, State, ctx
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
    ]
)

# ---------- Helper functions ----------
def expense_form(idx):
    """Create one expense card"""
    return dbc.Card(
        dbc.CardBody([
            html.H5(f"Expense #{idx+1}", className="card-title"),
            dbc.Row([
                dbc.Col(
                    dbc.Input(type="text", placeholder="Expense Type",
                              id={"type": "exp-type", "index": idx}),
                    md=6
                ),
                dbc.Col(
                    dbc.Input(type="number", placeholder="Monthly Cost",
                              id={"type": "exp-cost", "index": idx}),
                    md=6
                ),
            ], className="mb-2"),
        ]),
        className="mb-3"
    )


def liability_form(idx):
    """Create one liability card"""
    return dbc.Card(
        dbc.CardBody([
            html.H5(f"Liability #{idx+1}", className="card-title"),
            dbc.Row([
                dbc.Col(
                    dbc.Input(type="text", placeholder="Liability Type",
                              id={"type": "liab-type", "index": idx}),
                    md=6
                ),
                dbc.Col(
                    dbc.Input(type="number", placeholder="Outstanding Balance",
                              id={"type": "liab-balance", "index": idx}),
                    md=6
                ),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col(
                    dbc.Input(type="number", placeholder="Interest Rate (%)",
                              id={"type": "liab-rate", "index": idx}),
                    md=6
                ),
                dbc.Col(
                    dbc.Input(type="number", placeholder="Monthly Payment",
                              id={"type": "liab-payment", "index": idx}),
                    md=6
                ),
            ]),
        ]),
        className="mb-3"
    )


# ---------- Main layout ----------
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


# ---------- Top-level tab rendering ----------
@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "value")
)
def render_tab(tab):
    if tab == "information":
        # Vertical sub-tabs for Information
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


# ---------- Sub-tab rendering ----------
@app.callback(
    Output("info-sub-content", "children"),
    Input("info-sub-tabs", "value")
)
def render_info_subtab(subtab):
    if subtab == "personal":
        return html.Div("Personal Info Section")

    elif subtab == "children":
        return html.Div("Children Section")

    elif subtab == "income":
        return html.Div("Income Section")

    elif subtab == "assets":
        return html.Div("Assets Section")

    elif subtab == "expenses":
        # Show choice between liabilities and expenses
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
                                    "cursor": "pointer",
                                    "border": "1px solid #ccc",
                                    "border-radius": "8px",
                                    "padding": "20px",
                                    "textAlign": "center",
                                    "backgroundColor": "white"
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
                                    "cursor": "pointer",
                                    "border": "1px solid #ccc",
                                    "border-radius": "8px",
                                    "padding": "20px",
                                    "textAlign": "center",
                                    "backgroundColor": "white"
                                }
                            ),
                            width=6
                        ),
                    ],
                    justify="center",
                    className="mb-4"
                ),
                dbc.Button("Add Row", id="add-exp-liab", color="secondary",
                           className="d-block mx-auto mb-3", style={"display": "none"}),
                html.Div(id="expenses-liabilities-details")
            ]
        )


# ---------- Dynamic expense/liability forms ----------
@app.callback(
    Output("expenses-liabilities-details", "children"),
    Output("add-exp-liab", "style"),
    Input("liabilities-card", "n_clicks"),
    Input("expenses-card", "n_clicks"),
    State("expenses-liabilities-details", "children"),
    prevent_initial_call=True
)
def show_expenses_liabilities(liab_click, exp_click, current_children):
    button_id = ctx.triggered_id
    if button_id == "liabilities-card":
        return [liability_form(0)], {"display": "block"}
    elif button_id == "expenses-card":
        return [expense_form(0)], {"display": "block"}
    return dash.no_update


@app.callback(
    Output("expenses-liabilities-details", "children", allow_duplicate=True),
    Input("add-exp-liab", "n_clicks"),
    State("expenses-liabilities-details", "children"),
    prevent_initial_call=True
)
def add_exp_liab_row(n, current_children):
    if current_children is None:
        return [expense_form(0)]
    count = len(current_children)
    # detect whether we are adding expenses or liabilities based on first child
    if "Expense" in current_children[0]["props"]["children"][0]["props"]["children"]:
        return current_children + [expense_form(count)]
    else:
        return current_children + [liability_form(count)]


# ---------- Run ----------
if __name__ == "__main__":
    app.run(debug=True)
