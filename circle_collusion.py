import numpy as np
from numpy.linalg import norm

# a, b, pはそれぞれshape=(2,)のndarrayであると想定する
def calc_distance_and_neighbor_point(a, b, p):#a,b 直線上の2点 ,p 点の座標(交点から、ベクトルの逆方向に移動させた点)
    ap = p - a
    ab = b - a
    ai_norm = np.dot(ap, ab)/norm(ab)
    neighbor_point = a + (ab)/norm(ab)*ai_norm
    return neighbor_point #(点と線の交点の最短距離の交点)

def circle_collusion(ball_midy,ball_midx,collusion_y,collusion_x,vecy,vecx):
    f=0
    if f:
        #ベクトルを使う方法
        a = np.array([collusion_y,collusion_x])
        b = np.array([collusion_y+(collusion_y-ball_midy)*100,collusion_x+(collusion_x-ball_midx)*100])
        p = np.array([collusion_y-vecy,collusion_x-vecx])
        neighbor_point=calc_distance_and_neighbor_point(a, b, p)
        q = neighbor_point+(neighbor_point-p)
        return -collusion_y+q[0],-collusion_x+q[1]

    else:
        #行列を使う方法
        a = np.array([collusion_x,collusion_y])
        b = np.array([ball_midx,ball_midy])
        p = np.array([collusion_x+100,collusion_y])
        vec=np.array([vecx,vecy])
        ap = p - a
        ab = b - a
        cos=np.dot(ap, ab)/norm(ab)/norm(ap)
        sin=(1-cos**2)**0.5
        if collusion_y>=ball_midy:
            t=np.array([[cos,-sin],[sin,cos]])
            inv_t=np.array([[cos,sin],[-sin,cos]])
        else:
            inv_t=np.array([[cos,-sin],[sin,cos]])
            t=np.array([[cos,sin],[-sin,cos]])
        uv=np.dot(t,vec)
        uv[0]*=-1
        vec=np.dot(inv_t,uv)
        
        
        a = np.array([collusion_y,collusion_x])
        b = np.array([collusion_y+(collusion_y-ball_midy)*100,collusion_x+(collusion_x-ball_midx)*100])
        p = np.array([collusion_y-vecy,collusion_x-vecx])
        neighbor_point=calc_distance_and_neighbor_point(a, b, p)
        q = neighbor_point+(neighbor_point-p)
        return vec[1],vec[0]

    
    



  
    