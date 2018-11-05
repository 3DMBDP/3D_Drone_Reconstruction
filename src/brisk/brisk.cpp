#include <iostream>
#include "opencv2/opencv.hpp"
#include "opencv2/core/cvstd.hpp"
#include <vector>

const char* IMG_PATH = "../../img/*.JPG";

int main(){
	std::vector<cv::String> filenames;
	cv::glob(IMG_PATH, filenames);
	for(size_t i = 0; i < filenames.size(); i++)
		std::cout<<filenames[i]<<std::endl;
}

