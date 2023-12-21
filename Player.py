class Player:
    def __init__(self,y,x,hand_r):
        self.y=y
        self.x=x
        self.hand_r=hand_r
        self.vec=[0,0]
    
    def move(self,y,x):
        self.vec=[y-self.y,x-self.x]
        self.y = y
        self.x = x
    
    def collison_check(self,ball):
        if abs(self.y-ball.y)<=(ball.ball_r+self.hand_r) and abs(self.x-ball.x)<=(ball.ball_r+self.hand_r): #衝突する場合は、ballのベクトルや、handの位置を調整
            y_diff=abs(self.y-ball.y)
            x_diff=abs(self.x-ball.x)
            if y_diff>x_diff:
                ball.vec[0]*=-1
                self.y = ball.y+(ball.ball_r+self.hand_r) if self.y>ball.y  else ball.y-(ball.ball_r+self.hand_r) 
            elif y_diff<x_diff:
                ball.vec[1]*=-1
                self.x = ball.x+(ball.ball_r+self.hand_r) if self.x>ball.x  else ball.x-(ball.ball_r+self.hand_r)  
            else:
                ball.vec[0]*=-1
                ball.vec[1]*=-1
                self.y = ball.y+(ball.ball_r+self.hand_r) if self.y>ball.y  else ball.y-(ball.ball_r+self.hand_r)
                self.x = ball.x+(ball.ball_r+self.hand_r) if self.x>ball.x  else ball.x-(ball.ball_r+self.hand_r)  
        
            
        
            
        