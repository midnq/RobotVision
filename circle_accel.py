import numpy as np
from numpy.linalg import norm

def circle_accel(vect,ball_midy,ball_midx,player_midy,player_midx):
    """ 
    #ベクトル解法
    v=np.array(vect)
    ab=np.array([ball_midy-player_midy,ball_midx-player_midx])
    accel_vec=ab/norm(ab)*np.dot(v,ab)/norm(ab)
    return (int(accel_vec[0]),int(accel_vec[1]))
    """
    #行列解法
    collusion_x=(ball_midx+player_midx)/2
    collusion_y=(ball_midy+player_midy)/2
    a = np.array([collusion_x,collusion_y])
    b = np.array([player_midx,player_midy])
    p = np.array([collusion_x+100,collusion_y])
    vec=np.array([vect[1],vect[0]])
    ap = p - a
    ab = b - a
    cos=np.dot(ap, ab)/norm(ab)/norm(ap)
    sin=(1-cos**2)**0.5
    if collusion_y>=player_midy:
            t=np.array([[cos,-sin],[sin,cos]])
            inv_t=np.array([[cos,sin],[-sin,cos]])
    else:
            inv_t=np.array([[cos,-sin],[sin,cos]])
            t=np.array([[cos,sin],[-sin,cos]])
    uv=np.dot(t,vec)
    uv[1]=0
    vec=np.dot(inv_t,uv)
    return vec[1],vec[0]