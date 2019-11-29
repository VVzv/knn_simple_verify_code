#!/usr/bin/python
# -*- coding:utf-8 -*-
# __Author__: VVzv

import sys
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

def verify(path):
    ver_knn = joblib.load('./mode_job/test1.job')
    letters = splitLetter(path)
    pre = ver_knn.predict(letters)
    code_letter = ''
    for p in pre:
        code_letter += p
    return code_letter


if __name__ == '__main__':
    try:
        path = sys.argv[1]
        print("验证码识别为：\033[35m%s\033[0m" %verify(path))
    except Exception as e:
        print()
        print('\033[31m ERROR: %s\033[0m' %str(e))
