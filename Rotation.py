#!/usr/bin/python3
import os
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("img_path", type=str)
parser.add_argument("angle", type=int)
parser.add_argument("--dst_path", type=str)

args = parser.parse_args()
img_path = args.img_path
angle = args.angle
if args.dst_path:
    dst_path = args.dst_path
else:
    dst_name = os.path.basename(img_path)
    dst_folder = os.path.dirname(img_path)
    namelist = dst_name.split(".")
    dst_name = f'{namelist[0]}-R({angle}).{namelist[1]}'
    dst_path = dst_folder + "/" + dst_name
    dst_path = dst_path[1:] if dst_path[0] == "." and "/" not in dst_path else dst_path

print(dst_path)
print(f'angle:{angle}\n---start---')
# 画像読み込み
img_src = cv2.imread(img_path)
print(f'{img_path} is loaded')
# 画像サイズの取得(横, 縦)
size = tuple([img_src.shape[1], img_src.shape[0]])
print(f'size:{size}')
# 画像の中心位置(x, y)
center = tuple([int(size[0]/2), int(size[1]/2)])
print(f'center:{center}')
# 拡大比率
scale = 1.0

# 回転変換行列の算出
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# アフィン変換
dst = cv2.warpAffine(img_src, rotation_matrix, size, flags=cv2.INTER_CUBIC)
print('filter done')

cv2.imwrite(dst_path, dst)
print(f'output to {dst_path}')
print('---end---')
