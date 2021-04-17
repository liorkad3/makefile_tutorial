from imutils import paths
import argparse
import cv2
from PIL import Image
from torchvision.transforms import GaussianBlur

def create_blury_images():
    path = './images/dog2.jpg'
    im = Image.open(path)
    sigma = 2.0
    for i in range(20):
        gb = GaussianBlur(kernel_size=(3+2*i), sigma=sigma)
        im_blur = gb(im)
        im_blur.save(f'./images/dog_blur{i:03d}.png')


def variance_of_laplacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images",
	help="path to input directory of images", default='./images')
ap.add_argument("-t", "--threshold", type=float, default=50.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

# create_blury_images()

for imagePath in sorted(paths.list_images(args["images"])):
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)
	text = "Not Blurry"
	if fm < args["threshold"]:
		text = "Blurry"
	# show the image
	cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	cv2.imshow(imagePath, image)
	key = cv2.waitKey(0)