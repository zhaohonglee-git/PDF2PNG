### 将PDF文档保存为单页png图片，并将所有单页图片合成为一张长图

- PDF文档需要以demo的名字进行存储
- PDF文档的路径有要求，在./path 路径下
- 输出的单页的图片的分辨率可以设置，软件默认的为缩放2.3倍，分辨率越高，文件占用空间越大
- 输出的长图名字为999.png
- 首先执行脚本 pdf2images.py
- 其次执行脚本joint_images.py
- 依赖的包为：pymupdf  pip install PyMuPDF

- 后续考虑优化的问题
    1. 将文件路径等改为动态的，以UI界面的形式让客户自己上传
    2. 转出的长图可以自定义位置及文件名，以UI界面的形式让客户自己选择
    3. 输出的图片清晰程度可以让客户选择，以UI界面的形式让客户自己选择



### PDF2PNG工具介绍
- PDF2PNG支持将PDF文件转换为PNG格式的图片，不受PDF页码限制
- 转换的PNG图片可以支持：单张图片模式、长图模式、单张+长图模式三种模式
- 转换的PNG图片支持选择质量等级（分辨率）
- 为了不干扰使用者的原始文件且保持转换后图片的存储路径及图片命名清晰，工具软件默认将转换后的图片存放到单独的新建的文件夹内，且图片均以源PDF文件名称+数字形式存储
- 因为开发者本人技术能力有限，打包后的exe文件较大，后续本人会根据自己的时间情况决定是否对其优化
- 因该工具软件为免费开元版，测试难免不够充分，使用过程难免会有bug。欢迎各位使用者发现问题与我沟通：Email:296222105@qq.com




#### 开发笔记
- PySimpleGUI 是一个在其余python GUI库基础上做的封装，比较简洁好用，易于上手
- python -m pip install psgdemos 这里有很多demo可以进行参考
- Once installed, launch the demo browser by typing psgdemos from the command line"
- sg.In 为sg.InputText的简写形式
- sg.FileBrowse可以限制特定类型的文件，采用file_types=(("PDF FILES", "*.pdf")) 这个属性进行限制
- 相关的学习网站https://www.w3schools.cn/pysimplegui/pysimplegui_radio_element.html
- 对于radio控件，group_id="RADIO1",  实现对一组radio控件的组合
- 入坑问题：总是报错，重新创建window的时候说layout需要清除。问题是需要将layout的变量存在方法内部，成为局部变量即可。不要做全局变量，否则一直报错
- 打包使用pyinstaller 如果包体积过大，配合使用upx,--exclude-module排除不需要的包
- 如果没有下载过upx，那我们每次使用pyinstaller把python文件打包成exe可执行程序时都能看到下面这句提示，UPX is not available，也就是upx不可用。
- 踩坑，打包的ext程序图标不更新，貌似缓存未清理干净导致的，其实是windows系统查看图片的缓存导致的，切换一下图片显示方式，即可恢复正常
- pyinstaller -F --clean -i pdf1.ico -w gui.py -p pdf2images.py -p joint_images.py
- 如果需要打包静态文件，需要加入 --add-data './file.pdf;.' 命令，且程序在引用该静态文件时需要用os.path.join()的方式寻址
- 最终的打包命令如下： pyinstaller --clean -F --add-data './pdf1.ico;.' -i pdf1.ico --onefile -w gui.py -p pdf2images.py -p joint_images.py
- pyinstaller --clean -D --add-data './pdf1.ico;.' -i pdf1.ico -w gui.py -p pdf2images.py -p joint_images.py


{'-FILE-': 'E:/智能制造事业部/1.新产品研发/0AMES二次开发/MES二次开发设计资料/unity操作Excell动态链接库/excel的dll/EPPlus.dll', '1. 选取PDF文件': 'E:/智能制造事业部/1.新产品研发/0AMES二次开发/MES二次开发设计资料/unity操作Excell动态链接库/excel的dll/EPPlus.dll', 0: True, 1: False, 2: False, '-FILE-0': 'E:/智能制造事业部/1.新产品研发/0AMES二次开发/MES二次开发设计资料/unity操作Excell动态链接库', '2. 选取图片存储位置': 'E:/智能制造事业部/1.新产品研发/0AMES二次开发/MES二次开发设计 资料/unity操作Excell动态链接库'}