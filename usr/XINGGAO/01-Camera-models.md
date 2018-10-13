# Camera Models
Camera lenses model applied with a projection transformation:
P' = [x' y']^T = [z'x/z z'y/z].

Then as image and len have different center, we add a vector to it, moving the center to the lower left corner:  
P' = [x' y']^T = [fx/z+c_x fy/z+c_y].

Moreover, the points are expressed in pixels, we unify the length with:  
p' = [\alpha x/z+c_x  \beta y/z+c_y]

It is not a linear transformation, we apply homogeneous coordinate system to it, append another 1 to the end of the coordiates:  
P'_h = [\alpha x+c_xz \betay+c_yz z]^T = [\alpha 0 c_x 0\\0 \beta c_y 0\\0 0 1 0][x y z 1]^T = [\alpha 0 c_x 0\\0\beta c_y 0\\0 0 1 0]P_h = MP

Then decompose it further into:  
P' = MP = [\alpha 0 c_x\\0 \beta c_y\\0 0 1][I 0]P = K[I 0]P, where K is referred to as camera matrix. And it has 5 degrees of freedom: 2 for focal length, 2 for offset and 1 for skewness.

Finally, we need a matrix to transform world reference system into cemera reference system:  
P' = K[R T]P_\omega

## Camera Calibration
Suppose 3D position point P_i and correspond 2D point p_i, we have:  
p_i = [u_i v_i]^T = MP_i = [\frac{m_1P_i}{m_3P_i} \frac{m_2P_i}{m_3P_i}]

And as M has 11 unknown parameters, we need at lease 6 correspondences to solve it. Usually it is overdetermined:  
```
min ||Pm||^2
s.t. ||m||^2 = 1
```
To solve it, we use SVD then we have ![Solution](https://raw.githubusercontent.com/3DMBDP/3D_Drone_Reconstruction/master/usr/XINGGAO/img/Solution-Camera-Calibration.png). 
