# ライブラリのインポート
import copy
import time
import cv2
import numpy as np
import random
from Ball import Ball
from Player import Player
from motion_detection import motion_detection
from numpy.linalg import norm

# 中心の画素に類似した色の範囲を取得する関数
"""
TODO
ゴール、得点などの表示、
ゴール後の動き
カメラと操作の接続（白猫形式か追従形式かを決める)
発表資料の作成
カメラ追従について、反応している位置（反応している箇所の中心座標とそれに沿って円を描いた形で表示する

"""

# 画像から特定の範囲の色のみを抽出して二値画像にする関数


# 上の関数で出た画像のオプティカルフローを取得


# メインの処理
# Webカメラ設定
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# ret, frame = cap.read()  # frameは(480,640,3)
ball_img = cv2.imread("./image_data/ball2.png")
stadium_img = cv2.imread("./image_data/stadium.png")
hand_img = cv2.imread("./image_data/hand2.png")
# Webカメラの画面の大きさにスタジアムを合わせる
# stadium_img = cv2.resize(stadium_img, (frame.shape[1]*2, frame.shape[0]))
stadium_img = cv2.resize(stadium_img, (480*2, 640))
# ボールの高さ、幅の[半分](半分だから注意！！)
# (注意!)今回ボールの大きさが H:198、W:200と両方偶数のためこれで良いが、奇数の場合は工夫が必要
ball_r = ball_img.shape[1] // 2

# ボールの初期位置（中心座標)をスタジアムの中心に設定
idx_h = stadium_img.shape[0] // 2
idx_w = stadium_img.shape[1] // 2
hand_r = hand_img.shape[1] // 2
a = [[[True for k in range(3)] for i in range(100)] for j in range(100)]
for i in range(100):
    for j in range(100):
        if ball_img[i,j].sum()==0:
            for k in range(3):
                a[i][j][k]=False

    
flager=np.array(a)


ball = Ball(idx_h, idx_w, stadium_img.shape[0], stadium_img.shape[1], ball_r)
hand1 = Player(idx_h, 180, hand_r)
hand2 = Player(idx_h, 780, hand_r)
start = False
#start = True
stadium = copy.deepcopy(stadium_img)
# 実行
pre=[]
while True:
    ret, frame = cap.read()  # frameは(480,640,3)
    k = cv2.waitKey(1)
    if start:
        cv2.imshow("camera", frame)
        time.sleep(0.001)
        if ball.goal:
            ball.start()
            hand1.start()
            hand2.start()
        """
        ny = hand1.y
        nx = hand1.x
        
        if k == ord('w'):
            ny = hand1.y - 10
        elif k == ord('s'):
            ny = hand1.y + 10
        elif k == ord('a'):
            nx = hand1.x - 10
        elif k == ord('d'):
            nx = hand1.x + 10
        elif k == ord('q'):
            ny = hand1.y - 10
            nx = hand1.x - 10
        elif k == ord('e'):
            ny = hand1.y - 10
            nx = hand1.x + 10
        
        elif k == ord('z'):
            ny = hand1.y + 10
            nx = hand1.x - 10
        
        elif k == ord('c'):
            ny = hand1.y + 10
            nx = hand1.x + 10
        """
        ny, nx = motion_detection(
            frame, hmin, smin, vmin, hmax, smax, vmax, hand1.y, hand1.x)
        if ny-hand_r < 0+20:
            ny = hand_r+20
        if ny+hand_r >= 640-20:
            ny = 639-hand_r-20
        if nx-hand_r < 0+20:
            nx = hand_r+20
        if nx+hand_r >= 480-20:
            nx = 479-hand_r-20
        hand1.move(ny, nx)
        """
        nx += idx_w
        if ny-hand_r < 0+20:
            ny = hand_r+20
        if ny+hand_r >= 640-20:
            ny = 640-hand_r-20
        if nx-hand_r < 0+20:
            nx = hand_r+20
        if nx+hand_r >= 960-20:
            nx = 959-hand_r-20
        
        hand2.move(ny, nx)
        """
        
        if ball.collision_check(hand1):
            
            bi=np.array([ball.y,ball.x])
            hi=np.array([hand1.y,hand1.x])
            vi=bi-hi
            mi=hi+vi/(norm(vi))*(ball_r+hand_r)
            mii=[int(mi[0]),int(mi[1])]
            mi=np.array(mii)
            if pre:
                for y,x,r in pre:
                    stadium[(y-r):(y+r),(x-r):(x+r)] = stadium_img[(y-r):(y+r),(x-r):(x+r)]
            
            stadium[(mi[0] - ball_r): (mi[0] + ball_r),
                (mi[1]- ball_r): (mi[1] + ball_r)] = np.where(flager,ball_img,stadium[(mi[0] - ball_r): (mi[0] + ball_r),
                (mi[1] - ball_r): (mi[1] + ball_r)])
            stadium[(hand1.y - hand_r): (hand1.y + hand_r),
                    (hand1.x - hand_r): (hand1.x + hand_r)] = np.where(flager,hand_img,stadium[(hand1.y - hand_r): (hand1.y + hand_r),
                    (hand1.x - hand_r): (hand1.x + hand_r)])
            stadium[(hand2.y - hand_r): (hand2.y + hand_r),
                    (hand2.x - hand_r): (hand2.x + hand_r)] = np.where(flager,hand_img,stadium[(hand2.y - hand_r): (hand2.y + hand_r),
                    (hand2.x - hand_r): (hand2.x + hand_r)])



                    
            pre=[(mi[0],mi[1],ball_r),(hand1.y,hand1.x,hand_r),(hand2.y,hand2.x,hand_r)]
            ball.y=mi[0]
            ball.x=mi[1]
            cv2.imshow("output", stadium)
            time.sleep(0.001)

            
        if ball.collision_check(hand2):
            time.sleep(0.001)
            bi=np.array([ball.y,ball.x])
            hi=np.array([hand2.y,hand2.x])
            vi=bi-hi
            mi=hi+vi/(norm(vi))*(ball_r+hand_r)
            mii=[int(mi[0]),int(mi[1])]
            mi=np.array(mii)
            if pre:
                for y,x,r in pre:
                    stadium[(y-r):(y+r),(x-r):(x+r)] = stadium_img[(y-r):(y+r),(x-r):(x+r)]
            stadium[(mi[0] - ball_r): (mi[0] + ball_r),
                (mi[1]- ball_r): (mi[1] + ball_r)] = np.where(flager,ball_img,stadium[(mi[0] - ball_r): (mi[0] + ball_r),
                (mi[1] - ball_r): (mi[1] + ball_r)])
            stadium[(hand1.y - hand_r): (hand1.y + hand_r),
                    (hand1.x - hand_r): (hand1.x + hand_r)] = np.where(flager,hand_img,stadium[(hand1.y - hand_r): (hand1.y + hand_r),
                    (hand1.x - hand_r): (hand1.x + hand_r)])
            stadium[(hand2.y - hand_r): (hand2.y + hand_r),
                    (hand2.x - hand_r): (hand2.x + hand_r)] = np.where(flager,hand_img,stadium[(hand2.y - hand_r): (hand2.y + hand_r),
                    (hand2.x - hand_r): (hand2.x + hand_r)])
            



                    
            pre=[(mi[0],mi[1],ball_r),(hand1.y,hand1.x,hand_r),(hand2.y,hand2.x,hand_r)]
            ball.y=mi[0]
            ball.x=mi[1]
            cv2.imshow("output", stadium)
            time.sleep(0.001)
            
        ball.move()
        """
        ny, nx = motion_detection(
            frame, hmin, smin, vmin, hmax, smax, vmax, hand1.y, hand1.x)
        """
        
        
        
        
        #stadium[:, :] = stadium_img[:, :]
        if pre:
            for y,x,r in pre:
                stadium[(y-r):(y+r),(x-r):(x+r)] = stadium_img[(y-r):(y+r),(x-r):(x+r)]
        #print((ball.y - ball_h) ,(ball.y + ball_h), (ball.x- ball_w) , (ball.y + ball_w),ball.y,ball.x,ball_h,ball_w)
        hand1.collison_check(ball)
        hand2.collison_check(ball)
        """
        stadium[(ball.y - ball_r): (ball.y + ball_r),
                (ball.x - ball_r): (ball.x + ball_r)] = ball_img
        stadium[(hand1.y - hand_r): (hand1.y + hand_r),
                (hand1.x - hand_r): (hand1.x + hand_r)] = hand_img
        stadium[(hand2.y - hand_r): (hand2.y + hand_r),
                (hand2.x - hand_r): (hand2.x + hand_r)] = hand_img
        """
        stadium[(ball.y - ball_r): (ball.y + ball_r),
                (ball.x - ball_r): (ball.x + ball_r)] = np.where(flager,ball_img,stadium[(ball.y - ball_r): (ball.y + ball_r),
                (ball.x - ball_r): (ball.x + ball_r)])
        stadium[(hand1.y - hand_r): (hand1.y + hand_r),
                (hand1.x - hand_r): (hand1.x + hand_r)] = np.where(flager,hand_img,stadium[(hand1.y - hand_r): (hand1.y + hand_r),
                (hand1.x - hand_r): (hand1.x + hand_r)])
        stadium[(hand2.y - hand_r): (hand2.y + hand_r),
                (hand2.x - hand_r): (hand2.x + hand_r)] = np.where(flager,hand_img,stadium[(hand2.y - hand_r): (hand2.y + hand_r),
                (hand2.x - hand_r): (hand2.x + hand_r)])



                    
        pre=[(ball.y,ball.x,ball_r),(hand1.y,hand1.x,hand_r),(hand2.y,hand2.x,hand_r)]
        
        cv2.imshow("output", stadium)

        """
        ny, nx = motion_detection(
            frame, hmin, smin, vmin, hmax, smax, vmax, hand2.y, hand2.x)
        """
        
        """
        stadium = copy.deepcopy(stadium_img)
       # print((ball.y - ball_h) ,(ball.y + ball_h), (ball.x- ball_w) , (ball.y + ball_w),ball.y,ball.x,ball_h,ball_w)
        stadium[(ball.y - ball_r): (ball.y + ball_r),
                (ball.x - ball_r): (ball.x + ball_r)] = ball_img
        stadium[(hand1.y - hand_r): (hand1.y + hand_r),
                (hand1.x - hand_r): (hand1.x + hand_r)] = hand_img
        stadium[(hand2.y - hand_r): (hand2.y + hand_r),
                (hand2.x - hand_r): (hand2.x + hand_r)] = hand_img
        cv2.imshow("output", stadium)
        """
    else:
        temp = copy.deepcopy(frame)
        temp[210, 290:350] = [0, 0, 255]
        temp[270, 290:350] = [0, 0, 255]
        temp[210:270, 290] = [0, 0, 255]
        temp[210:270, 350] = [0, 0, 255]
        cv2.imshow("camera", temp)
    if k == ord('r'):
        break


    if k == ord("s"):

        # 対象範囲を切り出し
        boxFromX = 290  # 対象範囲開始位置 X座標
        boxFromY = 210  # 対象範囲開始位置 Y座標
        boxToX = 350  # 対象範囲終了位置 X座標
        boxToY = 270  # 対象範囲終了位置 Y座標
        # y:y+h, x:x+w　の順で設定
        imgBox = frame[boxFromY: boxToY, boxFromX: boxToX]

        # RGB平均値を出力
        # flattenで一次元化しmeanで平均を取得
        imgBoxHsv = cv2.cvtColor(imgBox, cv2.COLOR_BGR2HSV)
        # HSV平均値を取得
        # flattenで一次元化しmeanで平均を取得
        hmin = imgBoxHsv.T[0].flatten().min()
        smin = imgBoxHsv.T[1].flatten().min()
        vmin = imgBoxHsv.T[2].flatten().min()
        hmax = imgBoxHsv.T[0].flatten().max()
        smax = imgBoxHsv.T[1].flatten().max()
        vmax = imgBoxHsv.T[2].flatten().max()
        start = not (start)


cap.release()
cv2.destroyAllWindows()
