# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:39:41 2020

@author: acrog
"""

import cv2 
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random
import string


def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    
    #noise = np.zeros((image.shape[0], image.shape[1], image.shape[2]))

    #cv2.randu(noise, 0, 150)

    '''b_channel, g_channel, r_channel = cv2.split(noise)

    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 #creating a dummy alpha channel image.

    noise = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))'''
    #noisy_image = image + np.array(0.4*noise, dtype=np.int)
    noisy_image = cv2.blur(image,(1,1))

    return noisy_image

def addTarget(target, background, x, y):
    offset = 10
    temp_background = base_img[x-offset:x+target.shape[0]+offset, y-offset:y+target.shape[1]+offset].copy()
    b_channel, g_channel, r_channel = cv2.split(temp_background)

    alpha_channel = np.zeros(b_channel.shape, dtype=b_channel.dtype) #creating a dummy alpha channel image.

    temp_background = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    
    for i in range(offset,temp_background.shape[0]-offset):
        for j in range(offset,temp_background.shape[1]-offset):
            if target[i-offset][j-offset][3] != 0:
                temp_background[i][j] = target[i-offset][j-offset]
                
    temp_background = cv2.blur(temp_background,(3,3)) 
              
    cv2.imwrite('temp_background.png', temp_background[0:temp_background.shape[0], 0:temp_background.shape[0], 0:3])        
    for i in range(temp_background.shape[0]):
        for j in range(temp_background.shape[1]):
            if temp_background[i][j][3] != 0:
                background[x+i][y+j] = temp_background[i][j][0:3]
                
def createCircleTarget():
    color = np.array([random.randint(10,255), random.randint(10,255), random.randint(10,255)])
    W, H = 600, 600
    shape_img = Image.new('RGBA', (W, H), (color[0], color[1], color[2], 0))
    
    draw = ImageDraw.Draw(shape_img)
    draw.ellipse((0, 0, W, H), fill=(color[0], color[1], color[2]))
    font = ImageFont.truetype("Helvetica.ttf", 500)
    # draw.text((x, y),"Sample Text",(r,g,b))
    color = np.array([random.randint(10,255), random.randint(10,255), random.randint(10,255)])
    msg = random.choice(string.ascii_letters)
    w, h = draw.textsize(msg, font=font)
    draw.text(((W-w)/2,(H-h)/2), msg,(color[0],color[1],color[2]),font=font)
    #shape_img= shape_img.rotate(random.randint(0,360))
    shape_img.save('test.png', 'PNG')
    
def createRectangleTarget():
    color = np.array([random.randint(10,255), random.randint(10,255), random.randint(10,255)])
    W, H = 600, 600
    shape_img = Image.new('RGBA', (W, H), (color[0], color[1], color[2], 0))
    
    draw = ImageDraw.Draw(shape_img)
    draw.rectangle((0, 0, W, H), fill=(color[0], color[1], color[2]))
    font = ImageFont.truetype("Helvetica.ttf", 500)
    # draw.text((x, y),"Sample Text",(r,g,b))
    color = np.array([random.randint(10,255), random.randint(10,255), random.randint(10,255)])
    msg = random.choice(string.ascii_letters)
    w, h = draw.textsize(msg, font=font)
    draw.text(((W-w)/2,(H-h)/2), msg,(color[0],color[1],color[2]),font=font)
    #shape_img= shape_img.rotate(random.randint(0,360))
    shape_img.save('test.png', 'PNG')
    
def addSimilarColors(target):
    #back_color = target_img[1][1][0:3]
    for i in range(target.shape[0]):
        for j in range(target.shape[1]):
            #if target[i][j][0] == back_color[0] and target[i][j][1] == back_color[1] and target[i][j][2] == back_color[2]:
            target[i][j][0] += random.randint(-7,7)
            target[i][j][1] += random.randint(-7,7)
            target[i][j][2] += random.randint(-7,7)
    print(target)
    return target
    

base_img = cv2.imread("test google earth.jpg")

for i in range(10):
    createCircleTarget()
    target_img = cv2.imread("test.png", cv2.IMREAD_UNCHANGED)
    
    random_rot = random.randint(1,4)
    if random_rot == 1:
        target_img = target_img
    elif random_rot == 2:
        target_img = cv2.rotate(target_img, cv2.ROTATE_90_CLOCKWISE)
    elif random_rot == 3:
        target_img = cv2.rotate(target_img, cv2.ROTATE_180)
    elif random_rot == 4:
        target_img = cv2.rotate(target_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    shrink_size = random.randint(4,10)/100
    target_img = cv2.resize(target_img, (0,0), fx=shrink_size, fy=shrink_size,interpolation = cv2.INTER_AREA) 
    target_img = addSimilarColors(target_img)
    #target_img = sp_noise(target_img, 1)
    addTarget(target_img, base_img, random.randint(100,base_img.shape[0]-200),random.randint(100,base_img.shape[1]-200))
    
    
cv2.imwrite('combined.png', base_img)
#cv2.imshow('shape image',shape_img)
cv2.imshow('base image',base_img)
cv2.waitKey(0)
cv2.destroyAllWindows()