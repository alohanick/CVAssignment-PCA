import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
        
        
Top, Bottom, Left, Right = 100, 100, 0, 500
LeftImage = cv.imread('London_Left.jpg')
RightImage = cv.imread('London_Right.jpg')
LeftArrray = cv.copyMakeBorder(LeftImage, Top, Bottom, Left, Right, cv.BORDER_CONSTANT, value=(0, 0, 0))
RightArray = cv.copyMakeBorder(RightImage, Top, Bottom, Left, Right, cv.BORDER_CONSTANT, value=(0, 0, 0))
LeftImageGray = cv.cvtColor(LeftArrray, cv.COLOR_BGR2GRAY)
RightImageGray = cv.cvtColor(RightArray, cv.COLOR_BGR2GRAY)
Shift = cv.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = Shift.detectAndCompute(LeftImageGray, None)
kp2, des2 = Shift.detectAndCompute(RightImageGray, None)
# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0, 0] for i in range(len(matches))]


# ratio test as per Lowe's paper
Good = []
for i, (m, n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        Good.append(m)
        matchesMask[i] = [1, 0]

draw_params = dict(matchColor=(0, 255, 0),singlePointColor=(255, 0, 0),matchesMask=matchesMask,flags=0)

OverImageRegion = cv.drawMatchesKnn(LeftImageGray, kp1, RightImageGray, kp2, matches, None, **draw_params)
plt.imshow(OverImageRegion,), plt.title('Capturing the overlapping region'), plt.show()

rows, cols = LeftArrray.shape[:2]
#MIN_MATCH_COUNT = 10

src_pts = np.float32([kp1[m.queryIdx].pt for m in Good]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in Good]).reshape(-1, 1, 2)
M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
warpImg = cv.warpPerspective(RightArray, np.array(M), (RightArray.shape[1], RightArray.shape[0]), flags=cv.WARP_INVERSE_MAP)

for col in range(0, cols):
    if LeftArrray[:, col].any() and warpImg[:, col].any():
        left = col
        break
for col in range(cols-1, 0, -1):
    if LeftArrray[:, col].any() and warpImg[:, col].any():
        right = col
        break

ReconstructedArray = np.zeros([rows, cols, 3], np.uint8)
for row in range(0, rows):
    for col in range(0, cols):
        if not LeftArrray[row, col].any():
            ReconstructedArray[row, col] = warpImg[row, col]
        elif not warpImg[row, col].any():
            ReconstructedArray[row, col] = LeftArrray[row, col]
        else:
            LeftImgLen = float(abs(col - left))
            RightImgLen = float(abs(col - right))
            Ratio = LeftImgLen / (LeftImgLen + RightImgLen)
            ReconstructedArray[row, col] = np.clip(LeftArrray[row, col] * (1-Ratio) + warpImg[row, col] * Ratio, 0, 255)

# opencv is bgr, matplotlib is rgb
ReconstructedImage = cv.cvtColor(ReconstructedArray, cv.COLOR_BGR2RGB)
# show the result
plt.figure()
plt.imshow(ReconstructedImage)
plt.title('Reconstructed Image')
plt.show()

        
