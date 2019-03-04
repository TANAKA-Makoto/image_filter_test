#!/usr/bin/python3
import os
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("img_path", type=str)
parser.add_argument("angle", type=int)
group.add_argument("--append_dst", type=str)
group.add_argument("--normal_dst", type=str)

args = parser.parse_args()
img_path = args.img_path
angle = args.angle
if args.normal_dst:
    dst_path = args.normal_dst
else:
    dst_name = os.path.basename(img_path)
    dst_folder = args.append_dst
    namelist = dst_name.split(".")
    dst_name = f'{namelist[0]}-R({angle}).{namelist[1]}'
    dst_path = dst_folder + dst_name

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
