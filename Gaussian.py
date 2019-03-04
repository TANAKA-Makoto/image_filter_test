#!/usr/bin/python3
import sys
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("img_path", type=str)
parser.add_argument("dst_path", type=str)
parser.add_argument("--windowX", type=int)
parser.add_argument("--windowY", type=int)
parser.add_argument("--sigmaX", type=int)
parser.add_argument("--sigmaY", type=int)


args = parser.parse_args()
img_path = args.img_path
dst_path = args.dst_path
windowX = args.windowX if args.windowX else 125
windowY = args.windowY if args.windowY else 125
sigmaX = args.sigmaX if args.sigmaX else 1000
sigmaY = args.sigmaY if args.sigmaY else 1000

window = (windowX,windowY)
print(f'window:{window}\nsigmaX:{sigmaX}\nsigmaY:{sigmaY}\n---start---')
img = cv2.imread(img_path)
print(f'{img_path} is loaded')

dst = cv2.GaussianBlur(img, window, sigmaX=sigmaX, sigmaY=sigmaY)
print('filter done')

dst = np.minimum(dst, img)
print('mixing done')

cv2.imwrite(dst_path, dst)
print(f'output to {dst_path}')
print('---end---')
