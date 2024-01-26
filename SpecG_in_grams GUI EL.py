# py simp GUI for specific gavity to volume calcs

import PySimpleGUI as sg


def valid_percent(percent_solute):
    if float(percent_solute) <= 100:
        return True
    sg.popup_error("The percent of solute being added (Vol/Vol)\n"
                   "must be less than or equal to 100 percent of\n"
                   "the total of the solution being created.\n")
    return False

# create the calculation explaination window
def calc_window():
    layout = [[sg.Text("\n"
        "End H2O volume = Total Volume - (Percent Vol/Vol * Total Volume)\n"
        "\n"
        "End Solute Volume = Total Volume - H2O Volume\n"
        "\n"
        "End Solute Weight = Specific Gravity of Solute * End Diluent Vol\n"
        "\n"
        "End Solution Weight = End H2O Volume + Solute Weight\n", 
        key="calc_win")]]
    window = sg.Window("Calculation Explaination", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

# create main window display layout
sg.theme("Topanga")

layout = [
    [sg.Text("Enter the specific gravity of the liquid you are diluting into H2O in g/mL:")],
    [sg.InputText(key="-SG-", size=(10,1))],

    [sg.Text("Enter the percent (Vol/Vol) of the above liquid in the solution:")],
    [sg.Input(key="-PV-", size=(10,1))],
    
    [sg.Text("Enter the total volume to be created in mL:")],
    [sg.InputText(key="-TV-", size=(10,1))],

    [sg.Button("Press to convert the entered values into volumes")],

    [sg.Text("The volume (mL) of H2O in the final solution is:")],
    [sg.Input(key="-WTV-", size=(10, 1))],

    [sg.Text("The volume (mL) of solute in the final solution is:")],
    [sg.Input(key="-DSV-", size=(10,1))],
    
    [sg.Text("The weight (grams) of the solute in the final solution is:")],
    [sg.Input(key="-DSW-", size=(10,1))],

    [sg.Text("The total weight (grams) of the final solution is:")],
    [sg.Input(key="-TSW-", size=(10,1))],

    [sg.Button("Press to view equations for the calculations used")],

    [sg.Exit()] 
]

# create the main window
window = sg.Window("Welcom to eBot's Specific Gravity Converter!", layout)
   
# create an event loop
while True:
    event, values = window.read()

    # end program if user closes window
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # convert inputs logic
    if event == "Press to convert the entered values into volumes":

        percent_solute = ["-PV-"]

        if (valid_percent(values["-PV-"])):

            try:
                window["-WTV-"].update((round((float((values["-TV-"]))-(((float(values["-PV-"]))/100)*(float(values["-TV-"])))),2)))
                window["-DSV-"].update(((round((float((values["-TV-"])))-(float(values["-TV-"]))-(-((float(values["-PV-"]))/100)*(float(values["-TV-"]))),2))))
                window["-DSW-"].update(((round(float((values["-SG-"]))*(((float(values["-TV-"])))-(float(values["-TV-"]))-(-((float(values["-PV-"]))/100)*(float(values["-TV-"])))),2))))
                window["-TSW-"].update(((round(float((values["-TV-"]))-(((float(values["-PV-"]))/100)*(float(values["-TV-"])))+(float(values["-SG-"]))*(((float(values["-TV-"])))-(float(values["-TV-"]))-(-((float(values["-PV-"]))/100)*(float(values["-TV-"])))),2))))
            except ValueError:
                sg.popup_error("Entry feild only accepts an integer or floating point number.")

    # display equations used for conversions    
    if event == "Press to view equations for the calculations used":
        calc_window()
    
window.close()