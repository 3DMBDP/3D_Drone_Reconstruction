#include "opencv2/opencv.hpp"
#include "opencv2/core/cvstd.hpp"
#include "opencv2/features2d/features2d.hpp"

#include <sys/stat.h>

#include <vector>
#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <cstdio>

const char* IMG_PATH = "../../img/*.JPG";

int main(){
	std::vector<cv::String> filenames;
	cv::glob(IMG_PATH, filenames);

	//save image
	cv::Mat img;
	//feature detect
	cv::Mat descriptor;
	std::vector<cv::KeyPoint> keypoints;

	//brisk para
	int Thresh = 60;
	int Octaves = 4;
	float PatternScales = 1.0f;
	cv::Ptr<cv::BRISK> brisk = cv::BRISK::create(Thresh, Octaves, PatternScales);

	std::ofstream ofile;

	for(size_t i = 0; i < filenames.size(); i++){
		img = cv::imread(filenames[i]);
		std::cout<<"Processing "<<filenames[i]<<"..."<<std::endl;
		brisk->detect(img, keypoints);
		brisk->compute(img, keypoints, descriptor);	

		// create .sift.temp for temp output
		size_t raw = filenames[i].find_last_of(".");
		std::string newname = filenames[i].substr(0, raw);
		std::string newname_temp(newname);
		newname_temp.append(".sift.temp");
		newname.append(".sift");
		//size_t found = newname.find("img")+4;
		//newname.insert(found, "sift/");
		std::cout<<"Writing to "<<newname_temp<<"..."<<std::endl;

		ofile.open(newname_temp.c_str());

		// output in lowe's sift ascii format
		ofile<<keypoints.size()<<" "<<descriptor.rows<<std::endl;
		//TODO However, not so sure of the pixel coordinate order, test later
		int j;
		std::vector<cv::KeyPoint>::iterator it;
		for(it = keypoints.begin(), j=0; it != keypoints.end(); ++it, j++){
			ofile<<it->pt.y<<" "<<it->pt.x<<" "<<it->size<<" "<<(it->angle/180.0-1)*M_PI<<std::endl;
			ofile<<format(descriptor.row(j), cv::Formatter::FMT_CSV)<<std::endl;
		}
		ofile.close();

		// Rm comma in *.sift to make the format coincident with lowe's
		std::ifstream ifile;
		ifile.open(newname_temp.c_str());
		ofile.open(newname.c_str());
		std::string rm_comma;

		if(ifile.is_open()){
			while(std::getline(ifile, rm_comma)){
				rm_comma.erase(std::remove(rm_comma.begin(), rm_comma.end(), ','), rm_comma.end());
				//write to new file
				ofile<<rm_comma<<std::endl;
			}
		}
		ifile.close();
		ofile.close();

		//rm temp file
		remove(newname_temp.c_str());
	}

	return 0;
}

