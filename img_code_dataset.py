#!/usr/bin/python
# -*- coding:utf-8 -*-
# __Author__: VVzv

import os
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image


LETTERS = ['0', '7', 'r', 'g', '6', 'q', 'f', 'u', '3', '2', 'b', '4', 'j', '5', '1', 'x', '9', 'e', 's', 'z', 'o', 't', 'w', 'i', 'm', 'k', 'y', 'v', '8', 'p', 'n', 'c', 'd', 'l', 'a', 'h']
BASE_PATH = './source_imgs/'
TRAIN_BASE_PATH = './train_data/'
imgs_name = os.listdir(BASE_PATH)
imgs_path = [BASE_PATH + img_name for img_name in imgs_name]
letter_to_path = [ TRAIN_BASE_PATH + l for l in LETTERS ]
source_img_path = []
source_imgs_name = []
for img_path in imgs_path:
    if 'DS_Store' not in img_path:
        source_img_path.append(img_path)
for im_name in imgs_name:
    if 'DS_Store' not in im_name:
        source_imgs_name.append(im_name)
# print(source_imgs_name)

def letterdir():
    for letter in LETTERS:
        os.mkdir(TRAIN_BASE_PATH + letter)
        print(TRAIN_BASE_PATH + letter)

def letterToImg():
    n = 0
    for img_name in source_imgs_name:
        print(BASE_PATH + img_name)
        img = np.asarray(Image.open(BASE_PATH + img_name).convert('L'))
        img_binary = (img > 135) * 255
        img_letters = [
                    img_binary[:, 11: 33],
                    img_binary[:, 36: 58],
                    img_binary[:, 62: 84],
                    img_binary[:, 88: 110]
                    ]
        num = 0
        # 查看加载的图像，寻找最优切割点
        # plt.imshow(img_binary, cmap='gray')
        # plt.show()
        # break
        for img_letter in img_letters:
            # 查看切割完图像的宽度是否合理
            # print(img_letter.shape)
            # plt.imshow(img_letter, cmap='gray')
            # plt.show() 
            img_str = img_name.split('.')[0][num].lower()
            for letter_path in letter_to_path:
                if img_str == letter_path.split('/')[-1]:
                    img_n = '%s.png' % (n)
                    split_img_path = letter_path+'/'+img_n
                    print(split_img_path)
                    # print(img_letter)
                    plt.imsave(split_img_path, arr=img_letter, cmap='gray')
                    n += 1
            num += 1

if __name__ == '__main__':
    print('starting...')
    letterdir()  #创建0-z文件夹
    letterToImg() #将切割的图像放入0-z中

