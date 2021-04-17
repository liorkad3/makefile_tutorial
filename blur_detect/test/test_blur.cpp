#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

#include "functions.h"
 
int main( int argc, char** argv ) {
    cv::Mat image, grey;
    image = cv::imread("test/images/dog2.jpg" ,cv::IMREAD_COLOR);
  
    if(! image.data ) {
        std::cout <<  "Image not found or unable to open" << std::endl ;
        return -1;
    }

    cv::cvtColor(image, grey, cv::COLOR_BGR2GRAY);
    double blurVar = varianceOfLaplacian(grey);

    std::cout << "Blur: " << blurVar << std::endl;

    return 0;
}