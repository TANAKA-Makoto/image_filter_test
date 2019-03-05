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
parser.add_argument("window", type=int)
parser.add_argument("sigma", type=int)
group.add_argument("--append_dst", type=str)
group.add_argument("--normal_dst", type=str)
parser.add_argument("--cmd", help="optional", action="store_false")
parser.add_argument("--windowX", type=int)
parser.add_argument("--windowY", type=int)
parser.add_argument("--sigmaX", type=int)
parser.add_argument("--sigmaY", type=int)


args = parser.parse_args()
if hasattr(args, 'img_path'):
    img_path = args.img_path
else:
    img_path = sys.stdin.readline()[:-1]

windowX = windowY = args.window
windowX = args.windowX if args.windowX else windowX
windowY = args.windowY if args.windowY else windowY
sigmaX = sigmaY = args.sigma
sigmaX = args.sigmaX if args.sigmaX else sigmaX
sigmaY = args.sigmaY if args.sigmaY else sigmaY

cmd = bool(args.cmd)
if args.normal_dst:
    dst_path = args.normal_dst
else:
    dst_name = os.path.basename(img_path)
    dst_folder = args.append_dst
    namelist = dst_name.split(".")
    dst_name = f'{namelist[0]}-G({windowX},{windowY},{sigmaX},{sigmaY}).{namelist[1]}'
    dst_path = dst_folder + dst_name


def stdout(msg, isinfo=True):
    if (cmd or isinfo) and not (cmd and isinfo):
        pass
    else:
        print(msg)


def main():
    stdout(dst_path)
    window = (windowX,windowY)
    stdout(f'window:{window}\nsigmaX:{sigmaX}\nsigmaY:{sigmaY}\n---start---')
    img = cv2.imread(img_path)
    stdout(f'{img_path} is loaded')

    dst = cv2.GaussianBlur(img, window, sigmaX=sigmaX, sigmaY=sigmaY)
    stdout('filter done')

    dst = np.minimum(dst, img)
    stdout('mixing done')

    cv2.imwrite(dst_path, dst)
    stdout(f'output to {dst_path}')
    stdout('---end---')
    stdout(dst_path, False)


if __name__ == '__main__':
    main()
