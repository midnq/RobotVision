import numpy as np
import cv2

height_stadium = 700
width_stadium = 1200
margin_stadium = 20
thick_line = 5
color_line = [0,0,0]

stadium_img = np.zeros((height_stadium,width_stadium,3))
stadium_img[:,:] = [255,255,255] #白の画像

#円
center_circle = [[margin_stadium,height_stadium//2],[width_stadium//2,height_stadium//2],[width_stadium-margin_stadium,height_stadium//2]]
radius_circle = 200
color_circle = [1,1,1]

for center in center_circle:
  for x in range(margin_stadium, width_stadium-margin_stadium):
    for y in range(margin_stadium, height_stadium-margin_stadium):
      if np.linalg.norm(np.array([x,y])-np.array(center)) > radius_circle and np.linalg.norm(np.array([x,y])-np.array(center)) < radius_circle+thick_line:
        stadium_img[y,x] = color_circle

#内線
short_side_x = [width_stadium//2]
color_inside = [1,1,1]

for j in short_side_x:
  for i in range(margin_stadium, height_stadium-margin_stadium):
    for thickness in range(thick_line):
      stadium_img[i,j+thickness] = color_inside

#横線
long_side_y = [margin_stadium,height_stadium-margin_stadium]

for i in long_side_y:
    
  for j in range(margin_stadium, width_stadium-margin_stadium):
    for thickness in range(thick_line):
      stadium_img[i+thickness,j] = color_line

#縦線
short_side_x = [margin_stadium,width_stadium-margin_stadium]

for j in short_side_x:
  for i in range(margin_stadium, height_stadium-margin_stadium):
    for thickness in range(thick_line):
      stadium_img[i,j+thickness] = color_line

cv2.imwrite('stadium.png', stadium_img)

#球
height_ball = 100
width_ball = 100
radius_ball = 20
color_ball = [0,0,255]
center_ball = [width_ball//2,height_ball//2]

ball_img = np.zeros((height_ball,width_ball,3))
ball_img[:,:] = color_ball

cv2.imwrite('ball.png', ball_img)

#持つやつ
height_hand = 100
width_hand = 100
radius_hand = 30
color_hand = [0,255,0]
center_hand = [width_hand//2,height_hand//2]

hand_img = np.zeros((height_hand,width_hand,3))
hand_img[:,:] = color_hand

cv2.imwrite('hand.png', hand_img)

