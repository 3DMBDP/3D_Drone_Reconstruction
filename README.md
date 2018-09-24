# 3D_Drone_Reconstruction
## Comment on the Sprint 1 PPT
- Emphasize:
	- Hardwork, former opensource implementation is no less then 10K LOC
	- State-of-art, until 2013, people still working on optimizing the method of 3D reconstruction
- What is 3D Reconstruction(images: uav, uav grid, image and model):
	- Tools: UAV, to take images at the position of grids
	- The process the images with algorithm to get the position of vertex and edges in 3D space.
	- People focused on constructing the 3d model first, then trying to reconstruct with less strictly positioned camera, and finally in a incremental and parallel way to run the algorithm.
- Alternatives:
	- Commercial Softwares(images: a sketch of Pix4d model)
		- Pix4D(Accurate; Beautiful models with millions of meshes; Cheap, 49$/mo.)
		- Auto Desk
		- ...
	- Open Source Project for research
		- Opencv Module(Simple)
		- Bundler(20k LOC, old but widely used as basic)
		- openMVG(8k LOC, state-of-art, try to make it parallel)
		- ...
- What should we do to beat them
	- Focus on a single object: telecommunicate tower; Catch its original feature to optimize the Algorithm
		- Accuracy
		- Efficiency(c++, and deploy it on GPU to speed up)

- High level system diagram
(Something about algorithm needed to be put here i guess)
## Timeline
- Sprint2(9/26 - 10/06): review and investigate background papers and codes, get familiar to algorithms(SFM, SIFT, RANSAC, CUDA), and design the project
- Sprint3(10/07 - 11/10): build a prototype, able to generate feasible model with images
- Sprint4(11/11 - 12/13): add accelerate methods, able to handle fault and noised, make it stronger

## Relevant Open source Project
- [sba](http://users.ics.forth.gr/~lourakis/sba/index.html#)
- [Bundler_SFM](https://github.com/snavely/bundler_sfm)
- [mve](https://github.com/simonfuhrmann/mve)
- [openMVG](https://github.com/openMVG/openMVG/)
- [opencv.sfm](https://docs.opencv.org/4.0.0-alpha/d8/d8c/group__sfm.html)

## Reference
- [Multiple View Geometry in computer vision, Chapter 10: 3D Reconstruction](http://cvrs.whu.edu.cn/downloads/ebooks/Multiple%20View%20Geometry%20in%20Computer%20Vision%20\(Second%20Edition\).pdf)
- [Methods for 3D Reconstruction from Multiple Images](https://people.csail.mit.edu/sparis/talks/Paris_06_3D_Reconstruction.pdf)
- [2009. M. Lourakis and A. Argyros. SBA: A Software Package for Generic Sparse Bundle Adjustment.](users.ics.forth.gr/~lourakis/sba/sba-toms.pdf)
- [2006. N. Snavely, S. Seitz, R. Szeliski. Photo Tourism: Exploring Image Collections in 3D.](http://phototour.cs.washington.edu/Photo_Tourism.pdf)
- [2004. D. Lowe. Distinctive Image Features from Scale-Invariant Keypoints.](https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf)
- [2007. M. Goesele, N. Snavely, B. Curless, H. Hoppe, S. Seitz. Multi-view Stereo for Community Photo Collections.](https://www.gcc.tu-darmstadt.de/media/gcc/papers/Goesele-2007-MVS.pdf)
- [2012. P. Moulon, P. Monasse, R. Marlet. Adaptive Structure from Motion with a Contrario Model Estimation.](http://imagine.enpc.fr/~marletr/publi/ACCV-2012-Moulon-et-al.pdf)
- [2013. P. Moulon, P. Monasse, R. Marlet. Global Fusion of Relative Motions for Robust, Accurate and Scalable Structure from Motion.](http://imagine.enpc.fr/~moulonp/publis/iccv2013/index.html)
- [2011. C. Wu, S. Agarwal, B. Curless, S. Seitz. Multicore Bundle Adjustment.](http://grail.cs.washington.edu/projects/mcba/pba.pdf)
- [CS231A: Computer Vision, From 3D Reconstruction to Recognition](http://web.stanford.edu/class/cs231a/course_notes.html)

