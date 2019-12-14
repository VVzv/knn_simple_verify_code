#!/usr/bin/python
# -*- coding:utf-8 -*-
# __Author__: VVzv

import os
import joblib
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
from get_code_dict import getDataDict


LETTERS = ['0', '7', 'r', 'g', '6', 'q', 'f', 'u', '3', '2', 'b', '4', 'j', '5', '1', 'x', '9', 'e', 's', 'z', 'o', 't', 'w', 'i', 'm', 'k', 'y', 'v', '8', 'p', 'n', 'c', 'd', 'l', 'a', 'h']

base_path = './train_data/'
letters_file = os.listdir(base_path)
if '.DS_Store' in letters_file:
    letters_file = letters_file[1:]
letters_path = [ base_path + letter for letter in letters_file]
for letter_path in letters_path:
    letter_imgs_name = os.listdir(letter_path)
    if '.DS_Store' in letter_imgs_name:
        letter_imgs_name = letter_imgs_name[1:]
    # print(letter_imgs_name)
    # break
# print(letters_path)

def loadDataset():
    X = []
    y = []
    img_letter_dict = getDataDict()
    for ks,vs in img_letter_dict.items():
        # print(ks, vs)
        for v in vs:
            path = base_path + ks + '/' + v
            pix = np.asarray(Image.open(path).convert("L"))
            X.append(pix.reshape(48*22))
            y.append(ks)
        # break
    return np.asarray(X), np.asarray(y)

if __name__ == '__main__':
    X, y = loadDataset()
    knn = KNeighborsClassifier()
    knn.fit(X, y)
    score = knn.score(X, y)
    print('\033[35m训练数据精确率为：{:0.3f}%\033[0m'.format(score))
    joblib.dump(knn, './models/train_01.model')
    print('~~~OK!~~~~')

