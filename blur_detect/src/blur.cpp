#include <opencv2/imgproc.hpp>

double varianceOfLaplacian(cv::Mat greyImage){
    cv::Mat laplacian;
    cv::Laplacian(greyImage, laplacian, CV_64F);

    cv::Scalar mean, stddev;
    cv::meanStdDev(laplacian, mean, stddev);

    return stddev[0] * stddev[0];
}