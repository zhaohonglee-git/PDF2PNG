import PySimpleGUI as sg

"""
    Demo - Changing your window's theme at runtime
    * Create your window using a "window create function"
    * When your window's theme changes, close the window, call the "window create function"
    
    Copyright 2021 PySimpleGUI
"""

theme_list = ['Dark', 'Reddit']


# ------------------- Create the window -------------------
def make_window(theme=None):
    if theme:
        sg.theme(theme)
    # -----  Layout & Window Create  -----
    layout = [
        [sg.T('This is your layout')],
        [sg.Button('Ok'), sg.Button('Change Theme'), sg.Button('Exit')],
        [
            sg.Button(
                button_text="切换主题",
                key='-TOGGLE-GRAPHIC-',
                border_width=0,
                metadata=False,
            ),
        ],
    ]

    return sg.Window('Pattern for changing theme', layout)


def toggle_theme_index(index):
    if index == 0:
        return 1
    else:
        return 0


# ------------------- Main Program and Event Loop -------------------
def main():
    temp = toggle_theme_index(1)
    window = make_window(theme_list[temp])

    while True:
        event, values = window.read()
        temp = toggle_theme_index(temp)

        # image_data = toggle_btn_image(image_data)
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        if (
            event == 'Change Theme'
        ):  # Theme button clicked, so get new theme and restart window
            event, values = sg.Window(
                'Choose Theme',
                [
                    [
                        sg.Combo(sg.theme_list(), readonly=True, k='-THEME LIST-'),
                        sg.OK(),
                        sg.Cancel(),
                    ]
                ],
            ).read(close=True)
            print(event, values)
            if event == 'OK':
                window.close()
                window = make_window(values['-THEME LIST-'])

        if event == '-TOGGLE-GRAPHIC-':
            # if the graphical button that changes images
            window['-TOGGLE-GRAPHIC-'].metadata = not window[
                '-TOGGLE-GRAPHIC-'
            ].metadata

            # 切换主题颜色
            if window['-TOGGLE-GRAPHIC-'].metadata:
                window.close()
                window = make_window(theme_list[temp])

            else:
                window.close()
                window = make_window(theme_list[temp])
    window.close()


if __name__ == '__main__':
    main()
