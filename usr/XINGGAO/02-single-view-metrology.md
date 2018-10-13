# Single View metrology
Recover known structure of the 3D world if we have a single image and the property of the camera that took the image.

## 2D transformation
1. Isometric transformations:
Preserve distance, combination of rotation `R` and translation `t`:
```
[x' y' 1]^T = [R t\\0 1][x y 1]^T
```
2. Similarity transformation
```
[x' y' 1]^T = [SR t\\0 1][x y 1]^T, S = [s 0\\0 s]
```
3. Affine transformation
Preserve points, straight lines and parallelism, and in homogeneous coordinates:
```
[x' y' 1]^T = [A t\\0 1][x y 1]^T
```
Where `A` is linear transformation of `R^n`.
4. Projective transformations
```
[x' y' 1]^T = [A t\\v b][x y 1]^T
```
And cross ratio takes four points on a line preserves invariant:
```
cross ratio = \frac{||P_3 - P_1||||P_4 - P_2||}{||P_3 - P_2||||P_4 - P_1||}
```

## Points and Lines at infinity
2D line coud be represented with homogeneous vector `l = [a b c]^T`, and cross production of two lines is the intersection point.

In homogeneous coordinates, a point at infinity is `[x y 0]^T`, and two parallel line intersect at `[b -a 0]\in \infty`.

And we would have line in infinity with `[0 0 1]^T`

When we apply projective transformation `H` to a line `l`, we could use `0 = x^TIl = x^TH^TH^{-T}l = 0`

## Vanishing Points and Lines
We use `[a b c d]` to represent a plane, which first 3 as a regular vector and the last as a distance from origin. And line in 3D is represented as 
intersection of two planes.

Then we apply a projective transformation to one of these points at infinity `x_\infty` we obtain a point `p_\infty` in the image plane and is known as 
a vanishing point.

Lets define `d = (a, b,c )` as the direction of a set of 3D parallel lines in the camera reference system, which intersect toa point at infinity 
and the projection of such a point in the image returns the vanishing point v, which is defined `v = Kd`

If we consider a plane `\Pi` as a superset of parallel lines, each set of parallel lines intersects at a point at infinity. The line taht passes 
through such set of points at infinity is the line at infinity `l_\infty` associated to `Pi`. And the projective transformation of `l_\infty` to the 
image plane is called the vanishing line or the horizon line. `l_{horiz} = H^{-T}_Pl_\infty`.


