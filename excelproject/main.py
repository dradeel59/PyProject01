# This program wil let you convert excel files to csv files

from pathlib import Path # helps to open files from different paths

import PySimpleGUI as sg
import pandas as pd # lets you manipulate files

def convert_to_csv(excel_file_path, output_folder, sheet_name, separator, decimal):
    df = pd.read_excel(excel_file_path, sheet_name) # getting the actual file
    filename = Path(excel_file_path).stem #.stem and Path are functions used to only get the filename
    outputfile = Path(output_folder) / f"{filename}.csv" # this is used to change the filename
    df.to_csv(outputfile, sep=separator, decimal=decimal, index=False) # this is used to actually convert whats in the file
    sg.popup_no_titlebar("File converted!") # pop-up that appears after the conversion has been completed


# layout of the program
layout = [
    [sg.Text("Input File:"), sg.Input(key="-IN-"), sg.FileBrowse(file_types=(("Excel Files", "*.xls*"),))], #label, file type
    [sg.Text("Output Folder:"), sg.Input(key="-OUT-"), sg.FolderBrowse()], 
    [sg.Exit(), sg.Button("Convert to CSV")],
]

# creating a window

window = sg.Window("Excel to CSV Converter", layout)

# while the program is happening these things will be happening non-stop
while True: 
    # this makes it so so that the window will constnatly be monitoring/"reading" the events and values
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"): # makes exit button work by linking the "sg.WINDOW_CLOSED" function to it
        break 
    if event == "Convert to CSV": # adds function to the convert to CSV button
        convert_to_csv(
            excel_file_path = values["-IN-"],
            output_folder = values["-OUT-"],
            sheet_name = "Sheet1", #hard-coded for now, will change later
            separator = "|",
            decimal = ".",
        )
window.close() # makes the X button word

# next make a file displayer button
# stopped at 9:10 https://www.youtube.com/watch?v=LzCfNanQ_9c