import numpy as np
from numpy.linalg import norm

def circle_accel(vec,ball_midy,ball_midx,player_midy,player_midx):
    v=np.array(vec)
    ab=np.array([ball_midy-player_midy,ball_midx-player_midx])
    accel_vec=ab/norm(ab)*np.dot(v,ab)/norm(ab)
    return (int(accel_vec[0]),int(accel_vec[1]))
