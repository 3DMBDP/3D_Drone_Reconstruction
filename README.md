# 3D_Drone_Reconstruction
## Progress
- Read materials on reconstruction
- Run VisualSFM to get a adaptable result which is shown on sprint 2 pre
- **Start to solve background and feature detector problem**
## Dependency
To run our source code, add the following dependency:
- Opencv(v>=3)
- BOOST Lib
```
sudo apt-get install libboost-all-dev
```
## Demo
A completely integration of 3D reconstruction software:
- [VisualSFM](http://ccwu.me/vsfm/)
	- Easy to run:
		- download feasible version from the website
		- download dependency: CMVS/PMVS [by Pierre Moulon](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/osm-bundler/osm-bundler-pmvs2-cmvs-full-32-64.zip)
		- simply follow the guide in the website

## Components
~A script to combine the packages will be uploaded~

For now, user need to download and compile dependencies manually:
```
	git submodule update --init
	make prog/OpenSIFT
	make prog/Bundler
```
Set the env for bundler:
```
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/bundler/bin
```

Dependency:
- [GDK/GTK](http://www.gtk.org)(at least v2.18.4)
- jhead
- ImageMagick
- Python
- PIL
- Fortran

### Feature Detectors
Get feature points, we used Lowe's program but failed to generate feasible solution with complex background and blur. Trying alternatives now:
- SIFT
	- [Lowe's binary](http://www.cs.ubc.ca/~lowe/keypoints/siftDemoV4.zip)
	- [OpenSIFT](https://github.com/robwhess/opensift)
		- Download the repo with `git submodule`
		- Compile

- BRISK

OpenCV provide us with an implemented BRICK algorithm:

To run the code:
- Put the image need to process in `meandir/img`
- Enter dir `cd src/brisk`
- `make`
- `make run` 
## SFM
We refered to Bundler to do SFM, and replace the feature detection part ourselves;

To run bundler, simply entering the directory of feature detection results and run
```
	python utils/bundler.py
```
Note that it should be the right path of bundler.py, and the script to integrate them will be uploaded
