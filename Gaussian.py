#!/usr/bin/python3
import os
import sys
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("img_path", type=str)
group.add_argument("--append_dst", type=str)
group.add_argument("--normal_dst", type=str)
parser.add_argument("--window", type=int)
parser.add_argument("--windowX", type=int)
parser.add_argument("--windowY", type=int)
parser.add_argument("--sigma", type=int)
parser.add_argument("--sigmaX", type=int)
parser.add_argument("--sigmaY", type=int)


args = parser.parse_args()
img_path = args.img_path
windowX = windowY = args.window if args.window else None
windowX = args.windowX if args.windowX else windowX
windowY = args.windowY if args.windowY else windowY
sigmaX = sigmaY = args.sigma if args.sigma else None
sigmaX = args.sigmaX if args.sigmaX else sigmaX
sigmaY = args.sigmaY if args.sigmaY else sigmaY

windowX = windowX if windowX is not None else 101
windowY = windowY if windowY is not None else 101
sigmaX = sigmaX if sigmaX is not None else 20
sigmaY = sigmaY if sigmaY is not None else 20
if args.normal_dst:
    dst_path = args.normal_dst
else:
    dst_name = os.path.basename(img_path)
    dst_folder = args.append_dst
    namelist = dst_name.split(".")
    dst_name = f'{namelist[0]}-G({windowX},{windowY},{sigmaX},{sigmaY}).{namelist[1]}'
    dst_path = dst_folder + dst_name

print(dst_path)
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
