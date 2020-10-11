# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 12:25:54 2020

@author: acrog
"""

import sys
import cv2
import random
import os

def openImage(filename):
    
    img = cv2.imread(filename)
    
    if img is None:
        print("Invalid filename")
        sys.exit(2)
        
    return img

def cropImage(img):
    width = 200 # width of image in pixels
    height = 200 # height of image in pixels
    x = random.randint(width, img.shape[1] - width) # x location of cropping
    y = random.randint(height, img.shape[0] - height) # y location of cropping
    
    imgCrop = img[y:y+height, x:x+width]
    
    return imgCrop
    
    return img

def writeImage(img, inputFilename, num):
    num = str(num)
    
    inputDirName = "captured_images" # directory of the inputFilename file
    
    #removes dir and extension from filename
    inputFilename = os.path.relpath(inputFilename, inputDirName)
    inputFilename = os.path.splitext(inputFilename)[0]
    
    outputDirName = "cropped_images"
    if not os.path.exists(outputDirName):
        os.makedirs(outputDirName)
    
    outputFileDirName = outputDirName + "/" + inputFilename + "_" + num
    if not os.path.exists(outputFileDirName):
        os.makedirs(outputFileDirName)
        
    outputFilename = outputFileDirName + "/target" + num + ".jpg"
    print(outputFilename)
    
    cv2.imwrite(outputFilename, img)
    
    
def main(argv):
    if len(argv) != 1:
        print("Invalid Number of Arguments")
        sys.exit(2)
        
    inputFilename = argv[0]
    print(inputFilename)
    
    inputImg = openImage(inputFilename)
    
    currentTarget = 1 # represents which target in the image we are on
    inputImgCrop = cropImage(inputImg)
    
    writeImage(inputImgCrop, inputFilename, currentTarget)
    

if __name__ == "__main__":
   main(sys.argv[1:])

