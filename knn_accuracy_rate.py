#!/usr/bin/python
# -*- coding:utf-8 -*-
# __Author__: VVzv

import os
import joblib
import numpy as np

from PIL import Image
# from sklearn.externals import joblib


LETTERS = ['0', '7', 'r', 'g', '6', 'q', 'f', 'u', '3', '2', 'b', '4', 'j', '5', '1', 'x', '9', 'e', 's', 'z', 'o', 't', 'w', 'i', 'm', 'k', 'y', 'v', '8', 'p', 'n', 'c', 'd', 'l', 'a', 'h']
base_path = './test_data/'
letters_file = os.listdir(base_path)
if '.DS_Store' in letters_file:
    letters_file = letters_file[1:]
letters_path = [ base_path + letter for letter in letters_file]
for letter_path in letters_path:
    letter_imgs_name = os.listdir(letter_path)
    if '.DS_Store' in letter_imgs_name:
        letter_imgs_name = letter_imgs_name[1:]

def getDataDict():
    num_letter_dict = {}
    for letter in LETTERS:
        letter_img_name = os.listdir(base_path+letter)
        num_letter_dict.update({letter: letter_img_name})
    return num_letter_dict

def loadDataset():
    X = []
    y = []
    img_letter_dict = getDataDict()
    for ks,vs in img_letter_dict.items():
        for v in vs:
            path = base_path + ks + '/' + v
            pix = np.asarray(Image.open(path).convert("L"))
            X.append(pix.reshape(48*22))
            y.append(ks)
    return np.asarray(X), np.asarray(y)


if __name__ == '__main__':
    X, y = loadDataset()
    ver_knn = joblib.load('./models/train_01.model')
    score = ver_knn.score(X, y)
    print('\033[35m数据集精度为：{:.3f}%\033[0m'.format(score))

