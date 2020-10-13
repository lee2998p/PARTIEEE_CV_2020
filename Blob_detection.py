import cv2
import numpy as np

image_read = cv2.imread("input image.jpg", cv2.IMREAD_COLOR)
image_mser_setup = cv2.mser_create()
cv2.mser.detectRegions()
