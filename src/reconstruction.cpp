#define CERES_FOUND true

#include "opencv2/sfm.hpp"
#include "opencv2/opencv.hpp"
#include "opencv2/core/cvstd.hpp"
#include <iostream>
#include <fstream>

#define IMG_PATH "../img/*.JPG"
float FL = 9;
float CX = 300;
float CY = 400;

using namespace std;
using namespace cv;
using namespace cv::sfm;

int main() {
    std::vector<cv::String> filenames;
    cv::glob(IMG_PATH,filenames);

    cv::Matx33d K = cv::Matx33d(FL, 0, CX,
                                0, FL, CY,
                                0, 0, 1);

    bool is_projective = true;
    std::vector<cv::Mat> Rs_est, ts_est, points3d_estimated;
    sfm::reconstruct(filenames, Rs_est, ts_est, K, points3d_estimated, is_projective);

    // Print output
    using std::cout;
    using std::endl;
    cout << "\n----------------------------\n" << endl;
    cout << "Reconstruction: " << endl;
    cout << "============================" << endl;
    cout << "Estimated 3D points: " << points3d_estimated.size() << endl;
    cout << "Estimated cameras: " << Rs_est.size() << endl;
    cout << "Refined intrinsics: " << endl << K << endl << endl;
    cout << "============================" << endl;

      // recover estimated points3d
    ofstream points_file;
    cv::MatIterator_<double> mat_it;
    points_file.open("points.txt");
    points_file.precision(std::numeric_limits<double>::digits10);
    for (int i = 0; i < points3d_estimated.size(); ++i) {
        for(mat_it = points3d_estimated[i].begin<double>(); mat_it != points3d_estimated[i].end<double>(); mat_it++) {
            points_file << *mat_it << " ";
    }
        points_file << "\n";
  }

    cout << "Done. Points saved to points.txt" << endl;
    points_file.close();

    return 0;
}
