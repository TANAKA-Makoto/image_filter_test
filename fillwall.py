#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import cv2
import numpy as np

img_path = sys.argv[1]
dst_path = sys.argv[2]

img = cv2.imread(img_path)
bgrLower = np.array([5, 5, 5])    # 抽出する色の下限(BGR)
bgrUpper = np.array([230, 230, 230])    # 抽出する色の上限(BGR)
img_mask = cv2.bitwise_not(cv2.inRange(img, bgrLower, bgrUpper))  # BGRからマスクを作成
result = cv2.bitwise_and(img, img, mask=img_mask)  # 元画像とマスクを合成

cv2.imwrite(dst_path, result)
