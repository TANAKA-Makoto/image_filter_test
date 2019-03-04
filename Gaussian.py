#!/usr/bin/python3
import cv2
import numpy as np

img_path = './img/map_1_scan_allpoint_50m_cleaned.png'
dst_path = 'map_1_scan_allpoint_50m_cost125_1000_new.png'
img = cv2.imread(img_path)
print(f'{img_path} is loaded')

dst = cv2.GaussianBlur(img, (125, 125), sigmaX=1000, sigmaY=1000)
print('filter done')

dst = np.minimum(dst, img)
print('mixing done')

cv2.imwrite(dst_path, dst)
print(f'output to {dst_path}')
