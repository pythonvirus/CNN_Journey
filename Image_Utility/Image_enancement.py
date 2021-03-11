#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:01:23 2018

@author: mayank
"""
#import PIL.Image

import os
import glob
import pdb
import time
start_time = time.time()
out_dir ="/home/mayank/Downloads/object_detection/output_result/"
img_dir = "/home/mayank/Downloads/object_detection/faces_for_enhancement" # Enter Directory of all images 
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)

from PIL import Image
from PIL import ImageEnhance
def adjust_brightness(input_image,factor,factor_contrast,factor_sharpness):
    
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Brightness(image)
    out = enhancer_object.enhance(factor)
    enhancer_object1 = ImageEnhance.Contrast(out)
    out1 = enhancer_object1.enhance(factor_contrast)
    enhancer_object2 = ImageEnhance.Sharpness(out1)
    out2 = enhancer_object2.enhance(factor_sharpness)
    #pdb.set_trace()
    return out2
    
'''    
def adjust_contrast(input_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Contrast(image)
    out1 = enhancer_object.enhance(factor)
    return out1
    #out.save(output_image)

def adjust_sharpness(input_image, output_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Sharpness(image)
    out2 = enhancer_object.enhance(factor)
    out2.save(output_image)
'''
if __name__ == '__main__':
    for input_image in files :
        img1 = adjust_brightness(input_image,1.2,1.7,2)
        img1.save(out_dir+input_image.split("/")[-1])
    print("--- %s seconds ---" % (time.time() - start_time))
    #img2 = adjust_contrast(img1,1.7)
    #adjust_sharpness(img2,
    #                 '/home/mayank/Downloads/object_detection/output_result/ver1.png',
    #                 10)
    
    
