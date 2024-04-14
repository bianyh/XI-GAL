
import sys
import numpy as np
import cv2 as cv


def Forced_exit():
    print("Exiting program")
    sys.exit(0)


def addWeightedSmallImgToLargeImg(largeImg,alpha,smallImg,beta,gamma=0.0,regionTopLeftPos=(0,0)):
    #融合两个大小不一致的图片
    srcW, srcH = largeImg.shape[1::-1]
    refW, refH = smallImg.shape[1::-1]
    x,y =  regionTopLeftPos
    if (refW>srcW) or (refH>srcH):
        #raise ValueError("img2's size must less than or equal to img1")
        raise ValueError(f"img2's size {smallImg.shape[1::-1]} must less than or equal to img1's size {largeImg.shape[1::-1]}")
    else:
        if (x+refW)>srcW:
            x = srcW-refW
        if (y+refH)>srcH:
            y = srcH-refH
        destImg = np.array(largeImg)
        tmpSrcImg = destImg[y:y+refH,x:x+refW]
        tmpImg = cv.addWeighted(tmpSrcImg, alpha, smallImg, beta,gamma)
        destImg[y:y + refH, x:x + refW] = tmpImg
        return destImg









