# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import imageio
import random

picData = imageio.imread("myPic.jpg")
picDim = picData.shape
print(picDim)


picData[41,50] = [255,250,250]
X, Y = np.ogrid[:picDim[0], :picDim[1]]
upperLip = np.logical_and( X > 63, Y > 38)
upperLip = np.logical_and(upperLip, Y < 64)
picData[np.logical_and(upperLip, (X-41) **2 + (Y-50) **2 < 600)] = [200,20,20]

lowerLip = (X-41) ** 2 + (Y - 50) **2 > 700
lowerLip = np.logical_and(lowerLip, (X - 46) ** 2 + (Y-50)**2 < 625)
lowerLip = np.logical_and(lowerLip, X > 67)
picData[lowerLip] = [200, 20, 20]

leftCheek = (X - 55) ** 2 + (Y - 72) **2 < 20
picData[leftCheek] = [255, 150, 127]

rightCheek = (X - 55) ** 2 + (Y -30) ** 2 < 20
picData[rightCheek] = [255, 150, 127]

plt.figure(figsize = (2,2))
plt.imshow(picData)

threshold = 80
picData = imageio.imread("myPic.jpg")
filter = np.logical_and(picData[:, :, 0 ] > threshold, picData[:, :, 1] > threshold)
filter = np.logical_and(filter, picData[:, :, 2] > threshold)
print(filter)
picData[filter] = 255
plt.figure(figsize = (2,2))
plt.imshow(picData)