from imutils import paths
import argparse
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-d", "--dataset", required=True,
# 	help="path to input dataset")
# args = vars(ap.parse_args())
imagePaths = list(paths.list_images("/home/ankit/Desktop/Data Science/face-mask-detector/dataset"))
print(imagePaths)
