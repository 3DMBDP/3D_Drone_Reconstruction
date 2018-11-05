#include <boost/filesystem.hpp>

IMG_PATH = "../../img"

void main(){
	boost::filesystem::directory_iterator itr(boost::filesystem::path(IMG_PATH));
	for(itr; itr != boost::filesystem::directory_iterator(); ++itr)
		if(itr->path().extension().string() == ".JPG"{

				}
}
