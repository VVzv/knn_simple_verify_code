#!/usr/bin/python
# -*- coding:utf-8 -*-
# __Author__: VVzv

import os


LETTERS = ['0', '7', 'r', 'g', '6', 'q', 'f', 'u', '3', '2', 'b', '4', 'j', '5', '1', 'x', '9', 'e', 's', 'z', 'o', 't', 'w', 'i', 'm', 'k', 'y', 'v', '8', 'p', 'n', 'c', 'd', 'l', 'a', 'h']

base_path = './train_data/'

def getDataDict():
    num_letter_dict = {}
    for letter in LETTERS:
        letter_img_name = os.listdir(base_path+letter)
        num_letter_dict.update({letter: letter_img_name})
    return num_letter_dict

if __name__ == '__main__':
    print(getDataDict())
