#!/usr/bin/python
# -*- coding:utf-8 -*-
# __Author__: VVzv

import os
import joblib
import numpy as np

from PIL import Image
# from sklearn.externals import joblib


def splitLetter(path):
    img = np.asarray(Image.open(path).convert('L'))
    img_binary = (img > 135) * 255
    img_letters = [img_binary[:, 11: 33],
                   img_binary[:, 36: 58],
                   img_binary[:, 62: 84],
                   img_binary[:, 88: 110]]
    letters = []
    for part in img_letters:
        letters.append(part.reshape(48*22))

    return letters

def verify(file_name):
    ver_knn = joblib.load('./models/train_01.model')
    letters = splitLetter(file_name)
    pre = ver_knn.predict(letters)
    code_letter = ''
    for p in pre:
        code_letter += p
    return code_letter

def accuracyRate():
    path = './test_data/'
    imgs_name = os.listdir(path)
    right = []
    for img_name in imgs_name:
        code_pre = verify(path + img_name)
        # print('%s -> %s' % (img_name, verify(path + img_name)))
        if code_pre == img_name.split('.')[0].lower():
            right.append(img_name)
            print('\033[35m[+] %s -> %s\033[0m' %(img_name, code_pre))
        else:
            print('\033[31m[-] %s -> %s\033[0m' % (img_name, code_pre))
    rate = '{:.2f}%'.format(len(right) / len(imgs_name) * 100)
    return '识别率为：%s' %rate

if __name__ == '__main__':
    print(accuracyRate())
