"""####################### import requirement library ########################"""

import os
import re
import cv2


class Alignmentor:
    def __init__(self, image_list, save_root):
        self.image_list = image_list
        self.save_root = save_root

    def get_annotation_line(self):
        pass

    def crop(self):
        pass

    def get_ratio(self):
        pass

    def save_aligment_image(self):
        pass

    @staticmethod
    def find_threshold_pixel(_image):
        green_result = []
        red_result = []
        shape = _image.shape

        for y in range(shape[0]):
            for x in range(shape[1]):
                b = _image[y, x, 0]
                g = _image[y, x, 1]
                r = _image[y, x, 2]

                if b < 90 and g > 100 and r < 90:
                    green_result.append([x, y])

                if b < 90 and g < 90 and r > 100:
                    red_result.append([x, y])
        """
        result = {}
        if green_result:
            green_result = np.asarray(green_result)

            gx_min, gx_max, gy_min, gy_max = \
                min(green_result[:, 0]) + shape[1] * _is_right_side, max(green_result[:, 0]) + shape[
                    1] * _is_right_side, \
                min(green_result[:, 1]), max(green_result[:, 1])

            result['g'] = [(gx_min, gy_min), (gx_max, gy_max)]

        if red_result:
            red_result = np.asarray(red_result)
            rx_min, rx_max, ry_min, ry_max = \
                min(red_result[:, 0]) + shape[1] * _is_right_side, max(red_result[:, 0]) + shape[1] * _is_right_side, \
                min(red_result[:, 1]), max(red_result[:, 1])

            result['r'] = [(rx_min, ry_min), (rx_max, ry_max)]
        """
        return green_result, red_result

#  A  A
# (‘ㅅ‘=)
# J.M.Seo
