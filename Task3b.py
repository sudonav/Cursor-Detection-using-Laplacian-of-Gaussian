import cv2
import numpy as np

def matchTemplate(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

def resizeTemplate(template, x, y):
    return cv2.resize(template,None,fx=x, fy=y, interpolation = cv2.INTER_CUBIC)

positiveImageNames = ["t1_1","t1_2","t1_3","t1_4","t1_5","t1_6"]
negativeImageNames = ["neg_1","neg_2","neg_3","neg_4","neg_5","neg_6","neg_8", "neg_9", "neg_10", "neg_11", "neg_12"]

imageNameList = positiveImageNames
imageNameList.extend(negativeImageNames)

template = cv2.imread("Cursor1.jpg", 0)

threshold = 0.5
for imageName in imageNameList:
    max_val = 0.0
    readImagePath = imageName+".jpg"
    image = cv2.imread(readImagePath, 0)
    colorImage = cv2.imread(readImagePath, 1)
    gaussianImage = cv2.GaussianBlur(image, (3,3), 0)
    laplacianImage = cv2.Laplacian(gaussianImage,cv2.CV_8U)
    x = 1.0
    y = 1.0
    while(max_val < threshold):
        resizedTemplate = resizeTemplate(template, x, y)
        laplacianTemplate = cv2.Laplacian(resizedTemplate,cv2.CV_8U)
        matchedImage = matchTemplate(laplacianImage, laplacianTemplate)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matchedImage)
        if(x <= 2 and y <= 2):
            if(max_val >= threshold):
                top_left = max_loc
                bottom_right = (top_left[0] + len(resizedTemplate[0]), top_left[1] + len(resizedTemplate))
                top_left = (int(top_left[0] - (len(resizedTemplate[0])/2)),int(top_left[1] - (len(resizedTemplate)/2)))
                cv2.rectangle(colorImage, top_left, bottom_right, 255, 2)
            else:
                x = x + 0.05
                y = y + 0.05
        else:
            max_val = 1.0
    writeCursorFinalImagePath = "Cursor_"+imageName
    cv2.imwrite(writeCursorFinalImagePath+".png", colorImage)

positiveImageNames = ["t2_1","t2_2","t2_3","t2_4","t2_5","t2_6"]
negativeImageNames = ["neg_1","neg_2","neg_3","neg_4","neg_5","neg_6","neg_8", "neg_9", "neg_10","neg_11", "neg_12"]

imageNameList = positiveImageNames
imageNameList.extend(negativeImageNames)

template = cv2.imread("Cursor2.jpg", 0)

threshold = 0.5
for imageName in imageNameList:
    max_val = 0.0
    readImagePath = imageName+".jpg"
    image = cv2.imread(readImagePath, 0)
    colorImage = cv2.imread(readImagePath, 1)
    gaussianImage = cv2.GaussianBlur(image, (3,3), 0)
    laplacianImage = cv2.Laplacian(gaussianImage,cv2.CV_8U)
    x = 1.0
    y = 1.0
    while(max_val < threshold):
        resizedTemplate = resizeTemplate(template, x, y)
        laplacianTemplate = cv2.Laplacian(resizedTemplate,cv2.CV_8U)
        matchedImage = matchTemplate(laplacianImage, laplacianTemplate)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matchedImage)
        if(x <= 2 and y <= 2):
            if(max_val >= threshold):
                top_left = max_loc
                bottom_right = (top_left[0] + len(resizedTemplate[0]), top_left[1] + len(resizedTemplate))
                top_left = (int(top_left[0] - (len(resizedTemplate[0])/2)),int(top_left[1] - (len(resizedTemplate)/2)))
                cv2.rectangle(colorImage, top_left, bottom_right, 255, 2)
            else:
                x = x + 0.05
                y = y + 0.05
        else:
            max_val = 1.0
    writeCursorFinalImagePath = "Cursor_"+imageName
    cv2.imwrite(writeCursorFinalImagePath+".png", colorImage)

positiveImageNames = ["t3_1","t3_2","t3_3","t3_4","t3_5","t3_6"]
negativeImageNames = ["neg_1","neg_2","neg_3","neg_4","neg_5","neg_6","neg_8", "neg_9", "neg_10","neg_11", "neg_12"]

imageNameList = positiveImageNames
imageNameList.extend(negativeImageNames)

template = cv2.imread("Cursor3.jpg", 0)

threshold = 0.5
for imageName in imageNameList:
    max_val = 0.0
    readImagePath = imageName+".jpg"
    image = cv2.imread(readImagePath, 0)
    colorImage = cv2.imread(readImagePath, 1)
    gaussianImage = cv2.GaussianBlur(image, (3,3), 0)
    laplacianImage = cv2.Laplacian(gaussianImage,cv2.CV_8U)
    x = 1.0
    y = 1.0
    while(max_val < threshold):
        resizedTemplate = resizeTemplate(template, x, y)
        laplacianTemplate = cv2.Laplacian(resizedTemplate,cv2.CV_8U)
        matchedImage = matchTemplate(laplacianImage, laplacianTemplate)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matchedImage)
        if(x <= 2 and y <= 2):
            if(max_val >= threshold):
                top_left = max_loc
                bottom_right = (top_left[0] + len(resizedTemplate[0]), top_left[1] + len(resizedTemplate))
                top_left = (int(top_left[0] - (len(resizedTemplate[0])/2)),int(top_left[1] - (len(resizedTemplate)/2)))
                cv2.rectangle(colorImage, top_left, bottom_right, 255, 2)
                x = 1.0
                y = 1.0
            else:
                x = x + 0.05
                y = y + 0.05
        else:
            max_val = 1.0
    writeCursorFinalImagePath = "Cursor_"+imageName
    cv2.imwrite(writeCursorFinalImagePath+".png", colorImage)

