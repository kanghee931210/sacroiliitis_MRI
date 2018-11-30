import cv2
import numpy as np
import os

from matplotlib import pyplot as plt
from os import listdir

img_path = r"/home/kanghee/Desktop/MRIfile/originalfile/patient"
save_path = r"/home/kanghee/Desktop/MRIfile/histogram/patient/"

def img_equal(_path,_save_path):
    img_list = listdir(_path)
    for i in range(len(img_list)):
        img_name = _path+ "/" + img_list[i]
        img = cv2.imread(img_name, 0)
        img2 = cv2.equalizeHist(img)  # equalize
        save_name = _path.split('/')
        file_name = save_name[-1]
        tmppath = _save_path+ img_list[i]
        output = cv2.imwrite(tmppath, img2)
    return output


img_equal(img_path,save_path)
