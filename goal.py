import cv2
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import time
import numpy as np


def score(goal, right_score, left_score):
    ttfontname = "C:\\Windows\\Fonts\\meiryob.ttc"
    fontsize = 36
    
    if goal == 2:
        left_score += 1
    if goal == 1:
        right_score += 1
    
    score = str(left_score) + " - " + str(right_score)
    text_score = str(score)
    text_tokuten = "得点"
    
    
    canvasSize    = (300, 150)
    backgroundRGB = (255, 255, 255)
    textRGB       = (0, 0, 0)
    
    img_score = PIL.Image.new('RGB', canvasSize, backgroundRGB)
    draw = PIL.ImageDraw.Draw(img_score)
        
    font = PIL.ImageFont.truetype(ttfontname, fontsize)
    textTopLeft_score = (canvasSize[0]//2-fontsize*3/2, canvasSize[1]//2-fontsize/2)
    draw.text(textTopLeft_score, text_score, fill=textRGB, font=font)
    numpy_image = np.array(img_score)
    
    textTopLeft_tokuten = (canvasSize[0]//2-fontsize-10, canvasSize[1]//2-fontsize*2)
    draw.text(textTopLeft_tokuten, text_tokuten, fill=textRGB, font=font)
    numpy_image = np.array(img_score)
    
    return numpy_image, right_score, left_score
    
"""       

left_score = 0
right_score = 0       

i = 0
while True:
    k = cv2.waitKey(0)
    img, left_score, right_score = score(goal=1, left_score=left_score, right_score=right_score)
    cv2.imshow("score", img)
    print(left_score)
    time.sleep(1)
    if k==ord("q"):
        break
    
    
print(i)   

cv2.destroyAllWindows()
"""