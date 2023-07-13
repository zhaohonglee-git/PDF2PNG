import PySimpleGUI as sg
import os

theme_list = ['Dark', 'Reddit']


# ------------------- Create the window -------------------
def make_window(theme=None):
    if theme != None:
        sg.theme(theme)

    theme_toggle_col = sg.Column(
        [
            [
                sg.Button(
                    button_text="切换主题",
                    key='-TOGGLE-GRAPHIC-',
                    border_width=1,
                    metadata=False,
                    font=("Microsoft Yahei", 10),
                ),
            ]
        ],
        justification='right',
    )

    first_col = sg.Column(
        [
            [
                sg.InputText(
                    size=(75, 1),
                    enable_events=True,
                    key="-FILENAME-",
                    justification='left',
                    font=("Microsoft Yahei", 13),
                    tooltip='请选取需要转换的PDF文件',
                ),
                sg.FileBrowse(
                    '1. 选取PDF文件',
                    button_color=('LightYellow', '#3F7FBF'),
                    size=(25, 1),
                    font=("Microsoft Yahei", 13),
                    key="-CHOOSE-",
                    file_types=(("PDF FILES", "*.pdf"),),
                ),
            ],
        ],
    )
    second_col = sg.Column(
        [
            [
                sg.Radio(
                    '一般',
                    group_id="RADIO1",
                    default=True,
                    size=(20, 1),
                    font=("Microsoft Yahei", 13),
                    pad=(60, 1),
                    key="-NORMAL-",
                    enable_events=True,
                ),
                sg.Radio(
                    '高清',
                    group_id="RADIO1",
                    size=(20, 1),
                    font=("Microsoft Yahei", 13),
                    pad=(60, 1),
                    key="-HD-",
                    enable_events=True,
                    text_color='#48A3FF',
                ),
                sg.Radio(
                    '超清',
                    group_id="RADIO1",
                    size=(20, 1),
                    font=("Microsoft Yahei", 13),
                    pad=(60, 1),
                    key="-UHD-",
                    enable_events=True,
                    text_color='#CB2619',
                ),
            ],
        ],
        key="-LEVELSELECTED-",
    )

    third_col = sg.Column(
        [
            [
                sg.Radio(
                    '单张图片模式',
                    "RADIO2",
                    size=(25, 1),
                    font=("Microsoft Yahei", 13),
                    pad=(30, 1),
                    key="-SINGLEIMAGE-",
                    enable_events=True,
                ),
                sg.Radio(
                    '长图模式',
                    "RADIO2",
                    size=(25, 1),
                    default=True,
                    font=("Microsoft Yahei", 13),
                    pad=(30, 1),
                    key="-LONGIMAGE-",
                    enable_events=True,
                ),
                sg.Radio(
                    '单张+长图模式',
                    "RADIO2",
                    size=(25, 1),
                    font=("Microsoft Yahei", 13),
                    pad=(30, 1),
                    key="-ALLIMAGE-",
                    enable_events=True,
                ),
            ],
        ],
        key="-LEVELSELECTED-",
    )

    fourth_col = sg.Column(
        [
            [
                sg.In(
                    size=(75, 1),
                    enable_events=True,
                    key="-FILEDIR-",
                    justification='left',
                    font=("Microsoft Yahei", 13),
                    tooltip='选取图片存储路径',
                ),
                sg.FolderBrowse(
                    '2. 选取图片存储路径',
                    button_color=('LightYellow', '#3F7FBF'),
                    size=(25, 1),
                    font=("Microsoft Yahei", 13),
                ),
            ],
        ],
    )

    layout1 = [
        [
            sg.Text(
                "***PDF文件 ---> 图片***",
                text_color='#3F7FBF',
                justification='center',
                size=(1000, 1),
                font=("Microsoft Yahei", 25),
            )
        ],
        [
            [theme_toggle_col],
        ],
        [
            sg.Frame(
                layout=[
                    [first_col],
                ],
                title="*****第一步: 选取需要转换的PDF文件******",
                font=('Arial Microsoft Yahei Hybrid', 13),
                relief=sg.RELIEF_GROOVE,
                size=(1000, 80),
                pad=(10, 20),
            )
        ],
        [
            sg.Frame(
                layout=[
                    [second_col],
                ],
                title="*****第二步: 请选取生成图片质量等级******",
                font=('Arial Microsoft Yahei Hybrid', 13),
                relief=sg.RELIEF_GROOVE,
                size=(1000, 80),
                pad=(10, 20),
            )
        ],
        [
            sg.Frame(
                layout=[
                    [third_col],
                ],
                title="*****第三步: 请选择图片模式******",
                font=('Arial Microsoft Yahei Hybrid', 13),
                relief=sg.RELIEF_GROOVE,
                size=(1000, 80),
                pad=(10, 20),
            )
        ],
        [
            sg.Frame(
                layout=[
                    [fourth_col],
                ],
                title="*****第四步: 请选择图片存储路径******",
                font=('Arial Microsoft Yahei Hybrid', 13),
                relief=sg.RELIEF_GROOVE,
                size=(1000, 80),
                pad=(10, 20),
            )
        ],
        [
            sg.Button(
                '3. 生成图片',
                button_color=('LightYellow', '#3F7FBF'),
                size=(100, 1),
                font=("Microsoft Yahei", 13),
                pad=(200, 10),
                key="-SUBMIT-",
            )
        ],
    ]

    return sg.Window(
        "PDF转图片工具",
        layout1,
        size=(1000, 650),
        font=('Arial Microsoft Yahei Hybrid', 20),
    )


def toggle_theme_index(index):
    if index == 0:
        return 1
    else:
        return 0


def main():
    temp = 0
    window = make_window(theme_list[0])

    while True:
        event, values = window.read()
        temp = toggle_theme_index(temp)

        def submit():
            pdf_file = ''
            image_dir = ''
            level = '-NORMAL-'
            image_output_model = '-SINGLEIMAGE-'
            errors = [
                '请检查需要转换的pdf是否存在',
                '请检查图片存储路径是否正确',
                '发生未知错误,请联系开发者.Email:296222105@qq.com',
            ]

            if event == "-SUBMIT-":
                if window['-NORMAL-'].Get():
                    level = '-NORMAL-'
                elif window['-HD-'].Get():
                    level = '-HD-'
                elif window['-UHD-'].Get():
                    level = '-UHD-'
                elif window['-SINGLEIMAGE-'].Get():
                    image_output_model = '-SINGLEIMAGE-'
                elif window['-LONGIMAGE-'].Get():
                    image_output_model = '-LONGIMAGE-'
                elif window['-ALLIMAGE-'].Get():
                    image_output_model = '-ALLIMAGE-'

                if '.pdf' in window['-FILENAME-'].Get() and os.path.isfile(
                    window['-FILENAME-'].Get()
                ):
                    pdf_file = window['-FILENAME-'].Get()
                else:
                    print(errors[0])

                if os.path.isdir(window['-FILEDIR-'].Get()):
                    image_dir = window['-FILEDIR-'].Get()
                else:
                    print(errors[1])

                if pdf_file != '' and image_dir != '':
                    print('目标PDF文件路径为: ' + pdf_file)
                    print('选择的清晰度等级为： ' + level)
                    print('选择的图片输出模式为： ' + image_output_model)
                    print('图片存储路径为： ' + image_dir)
                    print('***提交***')

        submit()

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
