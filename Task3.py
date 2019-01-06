import cv2
import numpy as np

positiveImageNames = ["pos_1","pos_2","pos_3","pos_4","pos_5","pos_6","pos_7","pos_8",
                      "pos_9","pos_10","pos_11","pos_12","pos_13","pos_14","pos_15"]
negativeImageNames = ["neg_1","neg_2","neg_3","neg_4","neg_5","neg_6","neg_8"]

imageNameList = positiveImageNames
imageNameList.extend(negativeImageNames)

template = cv2.imread("task3/template.png", 0)

for imageName in imageNameList:
    readImagePath = imageName+".jpg"
    image = cv2.imread("task3/"+readImagePath, 0)
    colorImage = cv2.imread("task3/"+readImagePath, 1)
    gaussianImage = cv2.GaussianBlur(image, (3,3), 0)
    laplacianImage = cv2.Laplacian(gaussianImage,cv2.CV_8U)
    
    resizedTemplate = cv2.resize(template,None,fx=0.56, fy=0.56, interpolation = cv2.INTER_CUBIC)
    gaussianTemplate = cv2.GaussianBlur(resizedTemplate, (3,3), 0)
    laplacianTemplate = cv2.Laplacian(gaussianTemplate,cv2.CV_8U)

    matchedImage = cv2.matchTemplate(laplacianImage, laplacianTemplate, cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matchedImage)
    if(max_val >=0.5):
        top_left = max_loc
        bottom_right = (top_left[0] + len(template[0]), top_left[1] + len(template))
        top_left = (int(top_left[0] - (len(template[0])/2)),int(top_left[1] - (len(template)/2)))
        cv2.rectangle(colorImage, top_left, bottom_right, 255, 2)
                      
    writeCursorFinalImagePath = "Cursor_"+imageName
    cv2.imwrite("task3/"+writeCursorFinalImagePath+".png", colorImage)

