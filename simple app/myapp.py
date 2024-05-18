import PySimpleGUI as pg

# Theme
pg.theme("Black2")

# Layout
layout = [
    [pg.Text("Enter Age")],
    [pg.InputText(key='-I-')],
    [pg.Button("Continue"), pg.Button("Clear Text")]
]

# window
window = pg.Window("Growth Calculator", layout)

# event loop
while True:
    event, values = window.read()
    if event == "Clear Text":
        window['-I-']('')
    if event == "Continue":
        print(window["-I-"].get())
        if window["-I-"].get() == "2":
            pg.popup_ok("You are a toddler!")
    if event == pg.WIN_CLOSED:
        break
    

# close window
window.close()