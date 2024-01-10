from circle_collusion import circle_collusion
from circle_accel import circle_accel

class Ball:
    def __init__(self, y, x, h, w, ball_r):
        self.y = y
        self.x = x
        self.vec = [0,0]
        self.h = h
        self.w = w
        self.ball_r = ball_r
        self.goal=0
    def start(self):
        
        if self.goal==1:
            self.y=self.h // 2
            self.x=self.w // 2 - 100
            self.vec = [0, 0]
            
            
        elif self.goal==2:
            self.y=self.h // 2
            self.x=self.w // 2 + 100
            self.vec = [0, 0]
        else:
            self.y=self.h // 2
            self.x = self.w //2
            self.vec = [0, 0]
        
        self.goal=0
            
            
            
        
    def move(self):
        self.y += round(self.vec[0])
        self.x += round(self.vec[1])
        if self.y-self.ball_r < 0+20:
            self.y = self.ball_r+21
            self.vec[0] *= -1
        if self.y+self.ball_r >= self.h-20:
            self.y = self.h-self.ball_r-21
            self.vec[0] *= -1
        if self.x-self.ball_r < 0+20:
            if 120+self.ball_r<=self.y<=520-self.ball_r:
                self.goal=1
                if self.x - self.ball_r < 0:
                    self.x = self.ball_r+1
            else:
                self.x = self.ball_r+21
                self.vec[1] *= -1
        if self.x+self.ball_r >= self.w-20:
            if 120+self.ball_r<=self.y<=520-self.ball_r:
                self.goal=2
                if self.x + self.ball_r >= self.w:
                    self.x = self.w-self.ball_r-1
            else:
                self.x = self.w-self.ball_r-21
                self.vec[1] *= -1
    def collision_check(self, player):
        temp_y = self.y+self.vec[0]
        temp_x = self.x+self.vec[1]
        if ((player.y-temp_y)**2+(player.x-temp_x)**2)**0.5<=(self.ball_r+player.hand_r):# 衝突しているので、処理をする
            #衝突箇所の判定(二つの中心の中点)
            y,x=circle_collusion(temp_y,temp_x,(temp_y+player.y)/2,(temp_x+player.x)/2,self.vec[0],self.vec[1])
            """
            if y>0:
                y+=1
            else:
                y-=1
            if x>0:
                x+=1
            else:
                x-=1
            """
            #要検討
            self.vec[0]=(y)
            self.vec[1]=(x)
            (acy,acx)=circle_accel(player.vec,self.y,self.x,player.y,player.x)
            self.vec[0]+=acy
            self.vec[1]+=acx
            self.vec[0]=round(self.vec[0])
            self.vec[1]=round(self.vec[1])
            return True
        return False
            
"""     
    def collision_check(self, player):
        temp_y = self.y+self.vec[0]
        temp_x = self.x+self.vec[1]
        if abs(player.y-temp_y) <= (self.ball_r+player.hand_r) and abs(player.x-temp_x) <= (self.ball_r+player.hand_r):  # 衝突しているので、処理をする
            y_diff = abs(player.y-temp_y)
            x_diff = abs(player.x-temp_x)
            if y_diff > x_diff:
                self.vec[0] *= -1
            elif y_diff < x_diff:
                self.vec[1] *= -1
            else:
                self.vec[0] *= -1
                self.vec[1] *= -1
"""
