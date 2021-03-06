import numpy as np
import cv2

img1 = cv2.imread('lcntest1.png', 0)   # 0 for grey scaling
img2 = cv2.imread('lcn13.png', 0)

## Resize images
image = img1
height, width = image.shape[:2]
res = cv2.resize(image,(width/10, height/10), interpolation = cv2.INTER_CUBIC)
#img1 =res

image = img2
height, width = image.shape[:2]
res = cv2.resize(image,(width/10, height/10), interpolation = cv2.INTER_CUBIC)
#img2 = res


#img1 = cv2.equalizeHist(img1)
#img2 = cv2.equalizeHist(img2)


# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(10, 10))
img1 = clahe.apply(img1)
img2 = clahe.apply(img2)
cv2.imwrite('lcn11_cleah.png', img1)
cv2.imwrite('lcn13_cleah.png', img2)


fgbg = cv2.createBackgroundSubtractorMOG2()
fgmask = fgbg.apply(img1)
fgmask = fgbg.apply(img2)
cv2.imwrite('lcn13_fgmask.png', fgmask)

cv2.imwrite('lcn13_matsub.png', np.absolute(img1 - img2))

