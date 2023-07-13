import sys
import PySimpleGUI as sg

sg.theme("Light Blue 2")

l_col = sg.Column(
    [
        [
            sg.Text("First parameter", size=(15, 1)),
            sg.InputText(default_text="2", size=(3, 1)),
        ],
        [
            sg.Text("Second parameter", size=(15, 1)),
            sg.InputText(default_text="8", size=(3, 1)),
        ],
    ]
)
r_col = sg.Column(
    [[sg.Submit("A nice button", size=(23, 1))]],
    element_justification="right",
    vertical_alignment="bottom",
    expand_x=True,
)

layout = [
    [
        sg.Text("Target folder", size=(9, 1)),
        sg.InputText(default_text="Choose a folder...", size=(59, 1)),
        sg.FolderBrowse(),
    ],
    [
        sg.Frame(
            layout=[
                [l_col, r_col],
                [sg.ProgressBar(1, orientation="h", size=(50, 20))],
            ],
            title="Cool subpanel",
            relief=sg.RELIEF_GROOVE,
        )
    ],
]
window = sg.Window("Test window", layout)

while True:
    event, values = window.read()
    if event == "Cancel" or event is None:
        sys.exit()
