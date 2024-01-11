
class Player:
    def __init__(self,y,x,hand_r):
        self.y=y
        self.x=x
        self.sty=y
        self.stx=x
        self.hand_r=hand_r
        self.vec=[0,0]
    def start(self):
        self.vec=[0,0]
        #self.y=self.sty
        #self.x=self.stx
    def move(self,y,x):
        self.vec=[y-self.y,x-self.x]
        self.y = y
        self.x = x
    
    def collison_check(self,ball):
        if (self.y-ball.y)**2+(self.x-ball.x)**2<=(ball.ball_r+self.hand_r)**2: #衝突する場合は、ballのベクトルや、handの位置を調整
            y_diff=abs(self.y-ball.y)
            x_diff=abs(self.x-ball.x)
            if (self.y-320)**2+(self.x-480)**2>= (ball.y-320)**2+(ball.x-480)**2:
                """
                if y_diff>x_diff:
                    #ball.vec[0]*=-1
                    ball.y = self.y+(ball.ball_r+self.hand_r) if self.y<ball.y  else self.y-(ball.ball_r+self.hand_r)
                elif y_diff<x_diff:
                    #ball.vec[1]*=-1
                    ball.x = self.x+(ball.ball_r+self.hand_r) if self.x<ball.x  else self.x-(ball.ball_r+self.hand_r)
                else:
                    #ball.vec[0]*=-1
                    #ball.vec[1]*=-1
                    ball.y = self.y+(ball.ball_r+self.hand_r) if self.y<ball.y  else self.y-(ball.ball_r+self.hand_r)
                    ball.x = self.x+(ball.ball_r+self.hand_r) if self.x<ball.x  else self.x-(ball.ball_r+self.hand_r)
                """
                r_sum=ball.ball_r+self.hand_r
                r=((self.y-ball.y)**2+(self.x-ball.x)**2)**0.5
                ball.y=int(self.y+(ball.y-self.y)*r_sum/r)
            else:
                """
                if y_diff>x_diff:
                    #ball.vec[0]*=-1
                    self.y = ball.y+(ball.ball_r+self.hand_r) if self.y>ball.y  else ball.y-(ball.ball_r+self.hand_r) 
                elif y_diff<x_diff:
                    #ball.vec[1]*=-1
                    self.x = ball.x+(ball.ball_r+self.hand_r) if self.x>ball.x  else ball.x-(ball.ball_r+self.hand_r)  
                else:
                    #ball.vec[0]*=-1
                    #ball.vec[1]*=-1
                    self.y = ball.y+(ball.ball_r+self.hand_r) if self.y>ball.y  else ball.y-(ball.ball_r+self.hand_r)
                    self.x = ball.x+(ball.ball_r+self.hand_r) if self.x>ball.x  else ball.x-(ball.ball_r+self.hand_r) 
                """
                r_sum=ball.ball_r+self.hand_r
                r=((self.y-ball.y)**2+(self.x-ball.x)**2)**0.5
                self.y=int(ball.y+(self.y-ball.y)*r_sum/r)
            if self.x<480:
                if self.y-self.hand_r < 0+20:
                    self.y = self.hand_r+20
                if self.y+self.hand_r >= 640-20:
                    self.y = 639-self.hand_r-20
                if self.x-self.hand_r < 0+20:
                    self.x =self. hand_r+20
                #if self.x+self.hand_r >= 480-20:
                 #   self.x = 479-self.hand_r-20
                if self.x>= 480-20:
                    self.x = 479-20
            else:
                self.x-=480
                if self.y-self.hand_r < 0+20:
                    self.y = self.hand_r+20
                if self.y+self.hand_r >= 640-20:
                    self.y = 639-self.hand_r-20
                #if self.x-self.hand_r < 0+20:
                 #   self.x =self.hand_r+20
                if self.x < 0+20:
                    self.x =20
                if self.x+self.hand_r >= 480-20:
                    self.x = 479-self.hand_r-20
                self.x+=480
            if ball.y-ball.ball_r < 0+20:
                ball.y = ball.ball_r+20
            if ball.y+ball.ball_r >= 640-20:
                ball.y = 639-ball.ball_r-20
            if ball.x-ball.ball_r < 0+20:
                ball.x =ball.ball_r+20
            if ball.x+ball.ball_r >= 960-20:
                ball.x = 959-ball.ball_r-20

            
            
        
            
        
