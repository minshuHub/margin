# import os
# import random
#
# trainval_percent = 0.1
# train_percent = 0.9
# xmlfilepath = 'D:/Model/YOLOX-main/datasets/VOC/VOCdevkit/VOC2007/Annotations'
# txtsavepath = 'D:/Model/YOLOX-main/datasets/VOC/VOCdevkit/VOC2007/ImageSets'
# total_xml = os.listdir(xmlfilepath)
#
# num = len(total_xml)
# list = range(num)
# tv = int(num * trainval_percent)
# tr = int(tv * train_percent)
# trainval = random.sample(list, tv)
# train = random.sample(trainval, tr)
#
# ftest = open('D:/Model/YOLOX-main/datasets/VOC/VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w')
# ftrain = open('D:/Model/YOLOX-main/datasets/VOC/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt', 'w')
#
# for i in list:
#     name = total_xml[i][:-4] + '\n'
#     if i in trainval:
#         ftest.write(name)
#     else:
#         ftrain.write(name)
#
# ftrain.close()
# ftest.close()

from PIL import Image
import os

# 设置需要转换的图片目录
img_dir = r"D:\Model\YOLOX-main\datasets\VOC\VOCdevkit\VOC2007\JPEGImages"  # 改1

# 遍历目录下所有文件
for filename in os.listdir(img_dir):
    # 判断文件是否为png格式
    if filename.endswith(".tif"):  # 改2
        # 构造新的文件名，将后缀改为jpg
        new_filename = os.path.splitext(filename)[0] + ".jpg"
        # 打开图片
        img = Image.open(os.path.join(img_dir, filename))
        # 如果图片是RGBA模式，转换为RGB模式
        if img.mode == "RGBA":
            img = img.convert("RGB")
        # 如果图片是P模式，转换为RGB模式
        if img.mode == "P":
            img = img.convert("RGB")
        # 保存为新的jpg格式图片
        img.save(os.path.join(img_dir, new_filename))
        # 关闭图片
        img.close()
        # 删除原来的png格式图片
        os.remove(os.path.join(img_dir, filename))
