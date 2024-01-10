# ライブラリのインポート
import copy

import cv2
import numpy as np

from Ball import Ball

#中心の画素に類似した色の範囲を取得する関数



#画像から特定の範囲の色のみを抽出して二値画像にする関数



#上の関数で出た画像のオプティカルフローを取得



# #メインの処理
# # Webカメラ設定
# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# ret, frame = cap.read() #frameは(480,640,3)
# ball_img = cv2.imread("./image_data/ball.png")
# stadium_img = cv2.imread("./image_data/stadium.png")
# # Webカメラの画面の大きさにスタジアムを合わせる
# stadium_img = cv2.resize(stadium_img, (frame.shape[1], frame.shape[0]))

# # ボールの高さ、幅の[半分](半分だから注意！！)
# # (注意!)今回ボールの大きさが H:198、W:200と両方偶数のためこれで良いが、奇数の場合は工夫が必要
# ball_h, ball_w = ball_img.shape[0] // 2, ball_img.shape[1] // 2

# # ボールの初期位置（中心座標)をスタジアムの中心に設定
# idx_h = stadium_img.shape[0] // 2
# idx_w = stadium_img.shape[1] // 2


# # はじめボールは中央に配置
# stadium = copy.deepcopy(stadium_img)
# stadium[
#     (idx_h - ball_h) : (idx_h + ball_h), (idx_w - ball_w) : (idx_w + ball_w)
# ] = ball_img
# ball = Ball(idx_h,idx_w,stadium_img.shape[0],stadium_img.shape[1],ball_h,ball_w)
# start = False
# 実行
def motion_detection(frame,y,x,ball_r):
    
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # HSVによる上限、下限の設定　 ([Hue, Saturation, Value])
            hsvLower = np.array([0, 30, 60])  # 下限
            hsvUpper = np.array([20, 150, 255])  # 上限
            # HSVからマスクを作成
            hsv_mask = cv2.inRange(hsv, hsvLower, hsvUpper)
    
            # medianblurを用いてノイズ成分を除去
            blur_mask = cv2.medianBlur(hsv_mask, ksize=3)
    
            # ラベリング結果書き出し用に二値画像をカラー変換
            #src = cv2.cvtColor(blur_mask, cv2.COLOR_GRAY2BGR)
            #cv2.imshow("labeling", src)
            nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(blur_mask)
            # 領域(stats[:, 4])が２つ以上ある場合(そのうち1つは背景)だけ処理
            if nlabels >= 2:
                # 面積でソート、　今回は最も大きい領域１つだけ利用
                idx = stats[:, 4].argsort()[-2]
                idx_h = int(centroids[idx, 1])
                idx_w = int(centroids[idx, 0])
                for i in range(-ball_r,ball_r+1):
                    for j in range(-ball_r,ball_r+1):
                        if (ball_r-2)**2<=i**2+j**2<=ball_r**2 and 0<=idx_h+i<480 and 0<=idx_w+j<640:
                            frame[idx_h+i,idx_w+j]=[0,0,255]
                return idx_h,idx_w
            else:
                return y,x
                
            
    


    