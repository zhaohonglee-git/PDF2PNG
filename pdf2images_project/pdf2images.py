import sys, fitz
import os
import datetime


'''
该程序实现将pdf文件转换为单张的png图片
pdf_file 待转换的pdf文件
image_path_dir  图片存放目标路径
'''


def pyMuPDF_fitz(pdf_file, image_path_dir, image_quality_level=0):
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    #  图片清晰度等级 0  1  2
    image_quality_level = image_quality_level
    image_quality_level_list = [1.3, 2.3, 3.3]

    print("image_path_dir=" + image_path_dir)
    if os.path.isfile(pdf_file) and '.pdf' in pdf_file:
        dir_str, ext = os.path.splitext(pdf_file)
        pdf_file_name = dir_str.split("/")[-1]
        pdfDoc = fitz.open(pdf_file)

        new_path_dir = image_path_dir + '/' + pdf_file_name + '_temp'
        if not os.path.exists(new_path_dir):
            os.makedirs(new_path_dir)

        for pg in range(pdfDoc.page_count):
            page = pdfDoc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
            # 此处若是不做设置，默认图片大小为：792X612, dpi=72
            # (1.33333333-->1056x816)   (2-->1584x1224)
            zoom_x = image_quality_level_list[image_quality_level]
            zoom_y = image_quality_level_list[image_quality_level]
            mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)

            pix = page.get_pixmap(matrix=mat, alpha=False)

            if not os.path.exists(image_path_dir):  # 判断存放图片的文件夹是否存在
                os.makedirs(image_path_dir)  # 若图片文件夹不存在就创建

            pix.save(
                new_path_dir + '/' + pdf_file_name + '_%s.png' % pg
            )  # 将图片写入指定的文件夹内

        endTime_pdf2img = datetime.datetime.now()  # 结束时间
        print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)
    else:
        print('请检查要转换的pdf文件是否存在')


if __name__ == "__main__":
    pdf_file = './path/demo.pdf'
    image_path_dir = './path/image'
    pyMuPDF_fitz(pdf_file, image_path_dir)
