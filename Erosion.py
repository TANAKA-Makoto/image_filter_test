#!/usr/bin/python3
import os
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("img_path", type=str)
parser.add_argument("--dst_path", type=str)
parser.add_argument("--kernel", type=int)
parser.add_argument("--kernelX", type=int)
parser.add_argument("--kernelY", type=int)

args = parser.parse_args()
img_path = args.img_path
kernelX = kernelY = args.kernel if args.kernel else None
kernelX = args.kernelX if args.kernelX else kernelX
kernelY = args.kernelY if args.kernelY else kernelY
kernelX = kernelX if kernelX is not None else 5
kernelY = kernelY if kernelY is not None else 5
if args.dst_path:
    dst_path = args.dst_path
else:
    dst_name = os.path.basename(img_path)
    dst_folder = os.path.dirname(img_path)
    namelist = dst_name.split(".")
    dst_name = f'{namelist[0]}-E({kernelX},{kernelY}).{namelist[1]}'
    dst_path = dst_folder + "/" + dst_name
    dst_path = dst_path[1:] if dst_path[0] == "." and "/" not in dst_path else dst_path

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
