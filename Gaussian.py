#!/usr/bin/python3
import sys
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("img_path", type=str)
parser.add_argument("dst_path", type=str)
parser.add_argument("--window", type=tuple)
parser.add_argument("--sigmaX", type=int)
parser.add_argument("--sigmaY", type=int)


args = parser.parse_args()
img_path = args.img_path
dst_path = args.dst_path
if args.window:
    window = args.window
else:
    window = (125, 125)

if args.sigmaX:
    sigmaX = args.sigmaX
else:
    sigmaX = 1000

if args.sigmaY:
    sigmaY = args.sigmaY
else:
    sigmaY = 1000

img = cv2.imread(img_path)
print(f'{img_path} is loaded')

dst = cv2.GaussianBlur(img, (125, 125), sigmaX=1000, sigmaY=1000)
print('filter done')

dst = np.minimum(dst, img)
print('mixing done')

cv2.imwrite(dst_path, dst)
print(f'output to {dst_path}')
