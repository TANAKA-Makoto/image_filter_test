#!/usr/bin/python3
import os
import sys
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
if sys.stdin.isatty():
    parser.add_argument("img_path", type=str)
parser.add_argument("angle", type=float)
parser.add_argument("--cmd", help="optional", action="store_false")
group.add_argument("--append_dst", type=str)
group.add_argument("--normal_dst", type=str)

args = parser.parse_args()
if hasattr(args, 'img_path'):
    img_path = args.img_path
else:
    img_path = sys.stdin.readline()[:-1]

angle = args.angle
cmd = bool(args.cmd)
if args.normal_dst:
    dst_path = args.normal_dst
else:
    dst_name = os.path.basename(img_path)
    dst_folder = args.append_dst
    namelist = dst_name.split(".")
    dst_name = f'{".".join(namelist[0:-1])}-R({angle}).{namelist[-1]}'
    dst_path = dst_folder + dst_name


def stdout(msg, isinfo=True):
    if (cmd or isinfo) and not (cmd and isinfo):
        pass
    else:
        print(msg)


def main():
    stdout(dst_path)
    stdout(f'angle:{angle}\n---start---')
    # 画像読み込み
    img_src = cv2.imread(img_path)
    stdout(f'{img_path} is loaded')
    # 画像サイズの取得(横, 縦)
    size = tuple([img_src.shape[1], img_src.shape[0]])
    stdout(f'size:{size}')
    # 画像の中心位置(x, y)
    center = tuple([int(size[0]/2), int(size[1]/2)])
    stdout(f'center:{center}')
    # 拡大比率
    scale = 1.0
    
    # 回転変換行列の算出
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    
    # アフィン変換
    dst = cv2.warpAffine(img_src, rotation_matrix, size, flags=cv2.INTER_CUBIC)
    stdout('filter done')
    
    cv2.imwrite(dst_path, dst)
    stdout(f'output to {dst_path}')
    stdout('---end---')
    stdout(dst_path, False)


if __name__ == '__main__':
    main()
