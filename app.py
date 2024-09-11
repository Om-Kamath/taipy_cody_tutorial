from taipy import Gui
from pages.root.root import root_md
from pages.home.home import home_md
from pages.meds.med import Medicine
from api import Cody

symptoms = ""  # Initialize as an empty string
response = ""

def button_handler(id=None):
    return f"""
<|part|
<|Can my cat have this?|button|on_action=on_button_action|id={id}|>
|>
"""

def input_handler():
    return """
<|part|
<|{symptoms}|input|label=Tell us your cat's symptoms|>
|>
"""

def prompt_chef(symptoms, medicine):
    print(symptoms)
    return f"My cat is suffering from {symptoms}. Can my cat take {medicine}?"

def display_response():
    return """
<|part|
<|{response}|text|class_name=response-text|>
|>
"""

def on_button_action(state, id=None):
    pookie = Cody()
    if state.symptoms:
        if id == '1':
            state.response = pookie.get_response(prompt_chef(state.symptoms, 'Catspirin'))
        elif id == '2':
            state.response = pookie.get_response(prompt_chef(state.symptoms, 'Whiskerprofen'))
        elif id == '3':
            state.response = pookie.get_response(prompt_chef(state.symptoms, 'Meowtamin C'))
    else:
        state.response = "Please enter your cat's symptoms first."

pages = {
    '/': root_md,
    'home': home_md,
    'catspirin': Medicine('Catspirin', "It's aspirin for cats.").render() + input_handler() + button_handler(1) + display_response(),
    'whiskerprofen': Medicine('Whiskerprofen', 'For curing zoomies').render() + input_handler() + button_handler(2) + display_response(),
    'meowtamin-c': Medicine('Meowtamin C', 'For boosting immune system and better fur.').render() + input_handler() + button_handler(3) + display_response(),
}

if __name__ == '__main__':
    gui = Gui(pages=pages)
    gui.run(debug=True, use_reloader=True, port=8000)