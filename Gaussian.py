import cv2
import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread('map_1_scan_allpoint_50m_cleaned.png')

dst = cv2.GaussianBlur(img,(125,125),sigmaX=1000,sigmaY=1000)
# dst = cv2.GaussianBlur(img,(35,35),sigmaX=500,sigmaY=500)


#plt.subplot(121),plt.imshow(img),plt.title('Original')
#plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(dst),plt.title('Gaussian')
#plt.xticks([]), plt.yticks([])

#plt.show()

print('Writing...')

# for i in range(dst.shape[0]):
#     for j in range(dst.shape[1]):
#         for k in range(dst.shape[2]):
#             dst[i][j][k] = min(dst[i][j][k],img[i][j][k])
dst = np.minimum(dst,img)

cv2.imwrite('map_1_scan_allpoint_50m_cost125_1000_new.png', dst)
