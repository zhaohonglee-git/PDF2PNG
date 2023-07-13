from PIL import Image
from os import listdir
import os

'''
cut_images_path_dir 待拼接图片存放路径
result_path_dir  图片存放目标路径
long_image_name 图片命名以数字按序增加
'''


def joint_images(
    cut_images_path_dir, result_path_dir, long_image_name, remove_single_image=False
):
    cut_pictures = cut_images_path_dir
    result_path_target = result_path_dir
    long_image_name = long_image_name
    remove_single_image = remove_single_image

    if os.path.isdir(cut_images_path_dir) and os.path.isdir(result_path_dir):
        ims = [
            Image.open(cut_pictures + '\\' + fn)
            for fn in listdir(cut_pictures)
            if fn.endswith(".png")
        ]  #  打开路径下的所有图片

        if len(ims) > 0:
            width, height = ims[0].size  # 获取拼接图片的宽和高
            # print(ims)
            result = Image.new(ims[0].mode, (width, height * len(ims)))
            for j, im in enumerate(ims):
                result.paste(im, box=(0, j * height))
                print(j)

            # 删除原始单张图片
            if remove_single_image:
                for item in listdir(cut_pictures):
                    if item.endswith('.png'):
                        os.remove(cut_pictures + '/' + item)

            result.save(result_path_target + '\\' + long_image_name + '.png')

        else:
            print("未找到需要拼接的照片")
    else:
        print("请检查图片存放路径是否正确")


if __name__ == '__main__':
    joint_images('./path/image', './path/image', 'long_image')
