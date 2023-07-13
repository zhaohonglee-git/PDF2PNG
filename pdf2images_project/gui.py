import PySimpleGUI as sg
import os
import pdf2images
import joint_images

icon_base64_data = b''


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
        key="-LEVELSELECTED0-",
    )

    third_col = sg.Column(
        [
            [
                sg.Radio(
                    '单张图片模式',
                    group_id="RADIO2",
                    size=(25, 1),
                    font=("Microsoft Yahei", 13),
                    pad=(30, 1),
                    key="-SINGLEIMAGE-",
                    enable_events=True,
                ),
                sg.Radio(
                    '长图模式',
                    group_id="RADIO2",
                    size=(25, 1),
                    font=("Microsoft Yahei", 13),
                    pad=(30, 1),
                    key="-LONGIMAGE-",
                    enable_events=True,
                ),
                sg.Radio(
                    '单张+长图模式',
                    group_id="RADIO2",
                    default=True,
                    size=(25, 1),
                    font=("Microsoft Yahei", 13),
                    pad=(30, 1),
                    key="-ALLIMAGE-",
                    enable_events=True,
                ),
            ],
        ],
        key="-LEVELSELECTED1-",
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
        # icon='./pdf1.ico',
        icon=os.path.join(os.path.dirname(__file__), 'pdf1.ico'),
    )


def toggle_theme_index(index):
    if index == 0:
        return 1
    else:
        return 0


def pdf2images_gui():
    theme_list = ['Dark', 'Reddit']
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
            result = False
            submit_message = []

            if event == "-SUBMIT-":
                if values['-NORMAL-']:
                    level = '-NORMAL-'
                elif window['-HD-'].Get():
                    level = '-HD-'
                elif window['-UHD-'].Get():
                    level = '-UHD-'

                if values['-SINGLEIMAGE-']:
                    image_output_model = '-SINGLEIMAGE-'
                elif values['-LONGIMAGE-']:
                    image_output_model = '-LONGIMAGE-'
                elif values['-ALLIMAGE-']:
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
                    submit_message = [
                        pdf_file,
                        level,
                        image_output_model,
                        image_dir,
                        result,
                    ]

                    print(submit_message)

                    dir_str, ext = os.path.splitext(submit_message[0])
                    pdf_file_name = dir_str.split("/")[-1]
                    output_model = 2

                    # 转换的图片清晰度设置
                    if submit_message[1] == '-HD-':
                        image_quality_level = 1
                    elif submit_message[1] == '-UHD-':
                        image_quality_level = 2
                    else:
                        image_quality_level = 0

                    # 转换模式设置（单图、长图、单图+长图）
                    if submit_message[2] == '-SINGLEIMAGE-':
                        output_model = 0
                    elif submit_message[2] == '-LONGIMAGE-':
                        output_model = 1

                    # 执行所有业务
                    if output_model != 0:
                        # 判断图片输出模式 1-长图  2- 单图+长图
                        remove_single_image = False
                        if output_model == 1:
                            remove_single_image = True
                        else:
                            remove_single_image = False

                        pdf2images.pyMuPDF_fitz(
                            submit_message[0], submit_message[3], image_quality_level
                        )

                        new_path_dir = submit_message[3] + '/' + pdf_file_name + '_temp'
                        joint_images.joint_images(
                            cut_images_path_dir=new_path_dir,
                            result_path_dir=new_path_dir,
                            long_image_name=pdf_file_name + "_joint_image",
                            remove_single_image=remove_single_image,
                        )
                    else:
                        # 判断图片输出模式 单图模式
                        pdf2images.pyMuPDF_fitz(
                            submit_message[0], submit_message[3], image_quality_level
                        )

                    submit_message[4] = True

                    return submit_message

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
    pdf2images_gui()
