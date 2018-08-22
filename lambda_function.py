import numpy
import cv2
import boto3
import scipy
import skimage
import flask


def lambda_handler(event, context):
	for m in (numpy, cv2, boto3, scipy, flask, skimage):
		print("{} version :  {}".format(m, m.__version__))
	return "It works!"


if __name__ == "__main__":
	lambda_handler(None, None)
