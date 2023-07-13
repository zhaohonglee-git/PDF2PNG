import PySimpleGUI as sg
import os


theme_list = ['Dark', 'Reddit']


# theme_toggle_col = sg.Column(
#     [
#         [
#             sg.Button(
#                 button_text="切换主题",
#                 key='-TOGGLE-GRAPHIC-',
#                 border_width=0,
#                 metadata=False,
#             ),
#         ]
#     ],
#     justification='right',
# )


# ------------------- Create the window -------------------
def make_window(theme=None):
    if theme:
        sg.theme(theme)

    # layout0 = [[theme_toggle_col]]
    layout0 = [
        [
            sg.Button(
                button_text="切换主题",
                key='-TOGGLE-GRAPHIC-',
                border_width=0,
                metadata=False,
            ),
        ],
    ]

    return sg.Window(
        "PDF转图片工具",
        layout0,
        size=(1000, 650),
        font=('Arial Consolas Hybrid', 20),
    )


def toggle_theme_index(index):
    if index == 0:
        return 1
    else:
        return 0


def main():
    temp = toggle_theme_index(0)
    window = make_window(theme_list[temp])

    while True:
        event, values = window.read()
        temp = toggle_theme_index(temp)

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

        if event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == "__main__":
    main()
