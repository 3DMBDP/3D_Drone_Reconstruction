# Epipolar Geometry
Here is the general sketch of epipolar geometry, 
![Epipolar](https://raw.githubusercontent.com/3DMBDP/3D_Drone_Reconstruction/master/usr/XINGGAO/img/epipolar.png). 

We don't have exact location of the 3D location of `P`, but can determine its projection in one of the image planes `p`. We should be able 
to have cameras locations, orientations and camera matrices. And when we have the knowledge of camera location `O_1` and `O_2` and the
image point `p`, we can have the epipolar plane. Then `p'` must be located on the epipolar line of the second image, which is a strong constraint 
between image pairs.

# Fundamental matrix
We have camera projection matrices to be `M = K[I 0]` and `M' = K'[R T]`, then as `p` lies in epipolar plane, the production of `p` and the plane 
is zero, leads to a equation: `(T\cross p')^TRp = 0`. Abbr to `p'^T[T_\cross]Rp = 0`. Then add projection matrices, we have `p'^TK`^{-T}[T_\cross]RK^{-1}p = 0`

Where `F =K`^{-T}[T_\cross]RK^{-1}` is called fundamental matrix which has 7 freedom. With the fundamantal matrix we can derive the relationship between 
any `p` and `p'` without knowledge of actual position of `P`.

# Eight-Point Algorithm
Each correspondence `p_i = (u_i, v_i, 1)` and `p'_i = (u'_i, v'_i, 1)` gives us the constraint like:
```
[u_iu'_i v_iu'_i u'_i u_iv'_i v_iv'_i v'_i u_i v_i 1][F11 F12 F13 F21 F22 F23 F31 F32 F33]^T = 0
```
which requires 8 constraints to determine the Fundamental matrix. And in order to eliminate the noise, we useSVD to solve the overdetermined equation.
```
min_F ||F - F'||_F
s.t. det(F) = 0
```
