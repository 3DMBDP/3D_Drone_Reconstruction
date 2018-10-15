# Stereo System & SFM
## Triangulation
The process of determining the location of a 3D point given it projection into two or more images is called triangulation.

We have two cameras with known camera intrinsic parameters `K` and `K'` and the relative orientations and offsets `R, T` of the cameras respectively 
to each other. We could compute the two lines `l` and `l'` and they intersect at `P`.

In real world with the `p` and `p'` are noisy and camera calibration parameters are not precise, the two lines may nver intersect.

## non-linear methond for Triangulation
```
min_{P\cap}||MP\cap - p||^2 - ||M'P\cap - p'||^2
```
We seek to find a `P\cap` in 3D that best approximates `P` by finding the best least-squares estimations of the reprojection error of it in both images. 
And add more terms when there is more than two images. Gauss-Newton methond to find the tangent is used to solve the problem.

## Structure of Motion
All of them are vital actually
