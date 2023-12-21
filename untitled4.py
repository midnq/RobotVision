# ライブラリのインポート
import copy
import time
import cv2
import numpy as np
import random
from Ball import Ball
from Player import Player
from motion_detection import motion_detection

#中心の画素に類似した色の範囲を取得する関数



#画像から特定の範囲の色のみを抽出して二値画像にする関数



#上の関数で出た画像のオプティカルフローを取得



#メインの処理
# Webカメラ設定
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
ret, frame = cap.read() #frameは(480,640,3)
ball_img = cv2.imread("./image_data/ball.png")
stadium_img = cv2.imread("./image_data/stadium.png")
hand_img = cv2.imread("./image_data/hand.png")
# Webカメラの画面の大きさにスタジアムを合わせる
stadium_img = cv2.resize(stadium_img, (frame.shape[1]*2, frame.shape[0]))

# ボールの高さ、幅の[半分](半分だから注意！！)
# (注意!)今回ボールの大きさが H:198、W:200と両方偶数のためこれで良いが、奇数の場合は工夫が必要
ball_r =  ball_img.shape[1] // 2

# ボールの初期位置（中心座標)をスタジアムの中心に設定
idx_h = stadium_img.shape[0] // 2
idx_w = stadium_img.shape[1] // 2

hand_r = hand_img.shape[1] // 2


ball = Ball(idx_h,idx_w,stadium_img.shape[0],stadium_img.shape[1],ball_r)
hand1 = Player(idx_h,100,hand_r)
hand2 = Player(idx_h,540,hand_r)
start=False
# 実行
while True:
    ret, frame = cap.read() #frameは(480,640,3)
    if start:
        time.sleep(0.01)
        
        
        stadium = copy.deepcopy(stadium_img)
       # print((ball.y - ball_h) ,(ball.y + ball_h), (ball.x- ball_w) , (ball.y + ball_w),ball.y,ball.x,ball_h,ball_w)
        stadium[(ball.y - ball_r) : (ball.y + ball_r), (ball.x- ball_r) : (ball.x + ball_r)] = ball_img
        stadium[(hand1.y - hand_r): (hand1.y + hand_r),(hand1.x - hand_r): (hand1.x + hand_r)] = hand_img
        stadium[(hand2.y - hand_r): (hand2.y + hand_r),(hand2.x - hand_r): (hand2.x + hand_r)] = hand_img
        cv2.imshow("output", stadium)
        ball.collision_check(hand1)
        ball.collision_check(hand2)
        ball.move()
        ny,nx = motion_detection(frame,hmin,smin,vmin,hmax,smax,vmax,hand1.y,hand1.x)
        if ny-hand_r<0:
            ny=hand_r
        if ny+hand_r>=480:
            ny=479-hand_r
        if nx-hand_r<0:
            nx=hand_r
        if nx+hand_r>=640:
            nx=639-hand_r
        hand1.move(ny,nx)
        hand1.collison_check(ball)
        ny,nx = motion_detection(frame,hmin,smin,vmin,hmax,smax,vmax,hand2.y,hand2.x)
        nx += idx_w
        if ny-hand_r<0:
            ny=hand_r
        if ny+hand_r>=480:
            ny=479-hand_r
        if nx-hand_r<0:
            nx=hand_r
        if nx+hand_r>=1280:
            nx=1279-hand_r
            
        hand2.move(ny,nx)
        hand2.collison_check(ball)
    else:
        temp = copy.deepcopy(frame)
        temp[210,290:350]=[0,0,255]
        temp[270,290:350]=[0,0,255]
        temp[210:270,290]=[0,0,255]
        temp[210:270,350]=[0,0,255]
        cv2.imshow("camera", temp)

    k = cv2.waitKey(1)


    if k == ord("s"):
            
            # 対象範囲を切り出し
            boxFromX = 290 #対象範囲開始位置 X座標
            boxFromY = 210 #対象範囲開始位置 Y座標
            boxToX = 350 #対象範囲終了位置 X座標
            boxToY = 270 #対象範囲終了位置 Y座標
            # y:y+h, x:x+w　の順で設定
            imgBox = frame[boxFromY: boxToY, boxFromX: boxToX]
            
            # RGB平均値を出力
            # flattenで一次元化しmeanで平均を取得 
            imgBoxHsv = cv2.cvtColor(imgBox,cv2.COLOR_BGR2HSV)
            # HSV平均値を取得
            # flattenで一次元化しmeanで平均を取得 
            hmin = imgBoxHsv.T[0].flatten().min()
            smin = imgBoxHsv.T[1].flatten().min()
            vmin = imgBoxHsv.T[2].flatten().min()
            hmax = imgBoxHsv.T[0].flatten().max()
            smax = imgBoxHsv.T[1].flatten().max()
            vmax = imgBoxHsv.T[2].flatten().max()
            start = not(start)
            


    if k == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

    