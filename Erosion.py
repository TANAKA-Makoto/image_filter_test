#!/usr/bin/python3
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("img_path", type=str)
parser.add_argument("dst_path", type=str)
parser.add_argument("--kernelX", type=int)
parser.add_argument("--kernelY", type=int)
parser.add_argument("--sigmaX", type=int)
parser.add_argument("--sigmaY", type=int)


args = parser.parse_args()
img_path = args.img_path
dst_path = args.dst_path
if args.kernelX:
    kernelX = args.kernelX
else:
    kernelX = 5
if args.kernelY:
    kernelY = args.kernelY
else:
    kernelY = 5

kernel_in = (kernelX,kernelY)
print(f'window:{kernel_in}\n---start---')
img = cv2.imread(img_path)
print(f'{img_path} is loaded')
kernel = np.ones(kernel_in, np.uint8)
dst = cv2.erode(img, kernel, iterations=1)
print('filter done')

cv2.imwrite(dst_path, dst)
print(f'output to {dst_path}')
print('---end---')
