# 3D_Drone_Reconstruction

**AIM:** 2D to 3D reconstruction of telecommunication tower.

## VisualSFM
A completely integration of 3D reconstruction software:
- [VisualSFM](http://ccwu.me/vsfm/)
	- Easy to run:
		- download feasible version from the website
		- download dependency: CMVS/PMVS [by Pierre Moulon](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/osm-bundler/osm-bundler-pmvs2-cmvs-full-32-64.zip)
		- simply follow the guide in the website
		
![image](https://user-images.githubusercontent.com/43014839/50065370-3485b700-0184-11e9-8161-8929c821f398.png)



## SFM

We implemented SFM using MATLAB. For feature detection SURF was used.

![image](https://user-images.githubusercontent.com/43014839/50065393-52531c00-0184-11e9-8cec-25ecfa7fd2a9.png)



### Feature Detectors
Get feature points, we used Lowe's program but failed to generate feasible solution with complex background and blur. Trying alternatives now:
- SIFT
	- [Lowe's binary](http://www.cs.ubc.ca/~lowe/keypoints/siftDemoV4.zip)
	- [OpenSIFT](https://github.com/robwhess/opensift)
		- Download the repo with `git submodule`
		- Compile

- SURF
- Minimum Eigenvalue Algorithm
- BRISK

![image](https://user-images.githubusercontent.com/43014839/50064860-6ea18980-0181-11e9-9c1e-0f7c94392660.png)



## Unet

We implemented a Unet model to segment out tower from images with complex background.

*Image Augmentation*

130 masks were manually created and augmented. Images were rotated flipped and blurred to increase dataset size.

![image](https://user-images.githubusercontent.com/43014839/50065309-eb356780-0183-11e9-9ffb-9b2dcbecbd00.png)




*Unet model*

![image](https://user-images.githubusercontent.com/43014839/50065257-a6113580-0183-11e9-9363-3a5de6b32bcd.png)

Total images: 4000

Total masks (labels): 4000

Training loss: 0.2660

Training accuracy: 88.44%

Validation loss: 0.2744

Validation accuracy: 87.84%

Test accuracy: 87.93%


![image](https://user-images.githubusercontent.com/43014839/50064924-c809b880-0181-11e9-8e97-4927e850bfd4.png)






