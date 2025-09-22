from nicegui import ui

# ─────────────── HEADER ───────────────
with ui.header().style(
    'display: flex; justify-content: center; align-items: center; background-color: #0d6efd; padding: 10px; color: white;'
):
    ui.image('https://upload.wikimedia.org/wikipedia/commons/a/ab/Logo_TV_2015.png').style('height: 40px; margin-right: 10px')
    ui.label('Retirement Planning App').classes('text-h5')

# ─────────────── MAIN LAYOUT ───────────────
with ui.row().style('height: 100vh; width: 100vw; margin: 0;'):

    # Sidebar with vertical tabs - fixed width
    with ui.column().style('width: 220px; background-color: #f0f0f0; padding: 10px; height: 100%;'):
        tab_buttons = []
        tabs = ['Getting Started', 'Household', 'Financial Snapshot', 'Help']
        for tab_name in tabs:
            btn = ui.button(
                tab_name
            ).style('width: 100%; text-align: left; background: none; box-shadow: none; margin-bottom: 5px;')
            tab_buttons.append(btn)

    # Content area fills remaining space, scrollable if content overflows
    content = ui.column().style('flex: 1; padding: 20px; overflow-y: auto; height: 100%;')

# ─────────────── Stepwise questionnaire for Getting Started ───────────────
questions = [
    'Are you Male or Female?',
    'What is your current salary?',
    'What is your current age?',
    'Please list your retirement and bank accounts',
    'What are your monthly expenses?'
]

answers = {}

def show_getting_started():
    content.clear()
    current_question_index = 0

    def show_question(idx):
        content.clear()
        question = questions[idx]
        ui.label(question).classes('text-h5 mb-4')

        input_widget = None

        def on_next_click():
            value = None
            # Check type of widget and get its value
            if isinstance(input_widget, ui.Select):
                value = input_widget.value
            elif isinstance(input_widget, (ui.NumberInput, ui.Input, ui.Textarea)):
                value = input_widget.value

            if value is None or value == '':
                ui.notify('Please provide an answer before continuing.', color='red')
                return

            answers[question] = value
            next_idx = idx + 1
            if next_idx < len(questions):
                show_question(next_idx)
            else:
                show_summary()

        if idx == 0:
            input_widget = ui.select(['Male', 'Female'], label='Select Gender')
        elif idx == 1:
            input_widget = ui.number(label='Current Salary ($)', min=0, format='%.2f')
        elif idx == 2:
            input_widget = ui.number(label='Current Age', min=0, max=120, step=1)
        elif idx == 3:
            input_widget = ui.textarea(label='Retirement and Bank Accounts Summary')
        elif idx == 4:
            input_widget = ui.number(label='Monthly Expenses ($)', min=0, format='%.2f')

        ui.button('Next', on_click=on_next_click, color='primary').style('margin-top: 20px')

    def show_summary():
        content.clear()
        ui.label('Summary of your answers:').classes('text-h4 mb-4')
        for q, a in answers.items():
            ui.label(f'{q} → {a}').classes('mb-2')
        ui.label('Thank you! You can proceed with the rest of the app.')

    show_question(current_question_index)

# ─────────────── Other tabs ───────────────
def show_household():
    content.clear()
    with content:
        ui.label('Household Information').classes('text-h4')

def show_financial_snapshot():
    content.clear()
    with content:
        ui.label('Financial Snapshot').classes('text-h4')

def show_help():
    content.clear()
    with content:
        ui.label('Help & Support').classes('text-h4')

# ─────────────── Tab button callbacks ───────────────
tab_functions = [show_getting_started, show_household, show_financial_snapshot, show_help]

for btn, func in zip(tab_buttons, tab_functions):
    btn.on('click', func)

# Show first tab by default
show_getting_started()

# ─────────────── RUN APP ───────────────
ui.run()
