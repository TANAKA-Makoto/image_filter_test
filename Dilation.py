#!/usr/bin/python3
import os
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("img_path", type=str)
group.add_argument("--append_dst", type=str)
group.add_argument("--normal_dst", type=str)
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
if args.normal_dst:
    dst_path = args.normal_dst
else:
    dst_name = os.path.basename(img_path)
    dst_folder = args.append_dst
    namelist = dst_name.split(".")
    dst_name = f'{namelist[0]}-D({kernelX},{kernelY}).{namelist[1]}'
    dst_path = dst_folder + dst_name

kernel_in = (kernelX,kernelY)
print(f'kernel:{kernel_in}\n---start---')
img = cv2.imread(img_path)
print(f'{img_path} is loaded')
kernel = np.ones(kernel_in, np.uint8)
dst = cv2.dilate(img, kernel, iterations=1)
print('filter done')

cv2.imwrite(dst_path, dst)
print(f'output to {dst_path}')
print('---end---')
