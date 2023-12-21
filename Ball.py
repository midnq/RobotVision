class Ball:
    def __init__(self,y,x,h,w,ball_r):#
        self.y=y
        self.x=x
        self.vec=[-10,20]
        self.h=h
        self.w=w
        self.ball_r=ball_r
    def move(self):
        self.y+=self.vec[0]
        self.x+=self.vec[1]
        if self.y-self.ball_r<0:
            self.y=self.ball_r+1
            self.vec[0]*=-1
        if self.y+self.ball_r>=self.h:
            self.y=self.h-self.ball_r-1
            self.vec[0]*=-1
        if self.x-self.ball_r<0:
            self.x=self.ball_r+1
            self.vec[1]*=-1
        if self.x+self.ball_r>=self.w:
            self.x=self.w-self.ball_r-1
            self.vec[1]*=-1
    def collision_check(self,player):
        temp_y=self.y+self.vec[0]
        temp_x=self.x+self.vec[1]
        if abs(player.y-temp_y)<=(self.ball_r+player.hand_r) and abs(player.x-temp_x)<=(self.ball_r+player.hand_r):#衝突しているので、処理をする
            y_diff=abs(player.y-temp_y)
            x_diff=abs(player.x-temp_x)
            if y_diff>x_diff:
                self.vec[0]*=-1
            elif y_diff<x_diff:
                self.vec[1]*=-1
            else:
                self.vec[0]*=-1
                self.vec[1]*=-1
            
            
    
        
        