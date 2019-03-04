#!/usr/bin/python3
import sys
import cv2
import numpy as np

name = sys.argv[0]
img_path = sys.argv[1]
dst_path = sys.argv[2]

img = cv2.imread(img_path)
print(f'{img_path} is loaded')

dst = cv2.GaussianBlur(img, (125, 125), sigmaX=1000, sigmaY=1000)
print('filter done')

dst = np.minimum(dst, img)
print('mixing done')

cv2.imwrite(dst_path, dst)
print(f'output to {dst_path}')
