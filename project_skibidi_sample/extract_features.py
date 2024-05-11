#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np  
import os
from PIL import Image, ImageOps
import cv2
import matplotlib.pyplot as plt
from skimage import color, segmentation
import pandas as pd
from statistics import variance



def extract_features(image_path, mask_path, img_name):
    #image = plt.imread(image_path)
    
    mask = Image.open(mask_path)
    
    rgb_img = plt.imread(image_path)[:,:,:3]
    mask_rgb_img = plt.imread(mask_path)
    img_slic_segments = img_slic_segmentation(rgb_img, mask_rgb_img)

    rgb_img_cv2 = cv2.imread(image_path)
    mask_rgb_img_cv2 = cv2.imread(mask_path)
    
    
    
    asymmetry = rotation_asymmetry(mask)
    color= check_color(rgb_img, img_slic_segments)
    blue_white = detect_blue_white_veil(rgb_img_cv2, mask_rgb_img_cv2)

    return [img_name, asymmetry, color, blue_white]


def img_slic_segmentation(image, mask, segments=100, compactness=10):   
    slic_segment = slic_segment = segmentation.slic(np.array(image),
                n_segments = segments,
                compactness = compactness,
                sigma = 1,
                mask = np.array(mask),
                start_label = 1,
                channel_axis = 2)

        
    return slic_segment


def rotation_asymmetry(mask):
    asymmetry_scores = {}

    for angle in range(0, 361, 5):
        rotated_mask = rotate_image(mask, angle)
        fixed_mask = fix_mask(rotated_mask)
        asymmetry_scores[angle] = test_asymmetry(fixed_mask)

    min_angle = min(asymmetry_scores, key=asymmetry_scores.get)
    min_score = asymmetry_scores[min_angle]

    return min_score

def rotate_image(image, angle):
    
    open_cv_image = np.array(image)

    rotated_image = np.array(Image.fromarray(open_cv_image).rotate(angle))
    return rotated_image

def fix_mask(mask):
    mask_np = np.array(mask)
    binary_mask = np.where(mask_np > 240, 255, 0).astype(np.uint8)
    mask_image = Image.fromarray(binary_mask)

    row_indices = np.where(np.sum(mask_np, axis=1) > 0)[0]
    first_row, last_row = row_indices[0], row_indices[-1]
    if (last_row - first_row) % 2 != 0:
        last_row += 1 

    col_indices = np.where(np.sum(mask_np, axis=0) > 0)[0]
    first_col, last_col = col_indices[0], col_indices[-1]
    if (last_col - first_col) % 2 != 0:
        last_col += 1 

    cropped_mask = mask_image.crop((first_col, first_row, last_col, last_row))

    old_width, old_height = cropped_mask.size
    fixed_mask = ImageOps.expand(cropped_mask, border=int(old_width / 2))

    return fixed_mask

def test_asymmetry(mask):
    mask_array = np.array(mask)

    height, width = mask_array.shape
    left = mask_array[:, :width // 2]
    right = np.flip(mask_array[:, width // 2:], axis=1)

    top = mask_array[:height // 2, :]
    bottom = np.flip(mask_array[height // 2:, :], axis=0)

    asym_vertical = np.sum(left != right)
    asym_horizontal = np.sum(top != bottom)
    total_white = np.sum(mask_array == 255)

    max_asym_vertical = total_white / 2
    max_asym_horizontal = total_white / 2

    norm_asymmetry_vertical = (asym_vertical / max_asym_vertical) * 2
    norm_asymmetry_horizontal = (asym_horizontal / max_asym_horizontal) * 2

    avg_asymmetry = (norm_asymmetry_vertical + norm_asymmetry_horizontal) / 2

    return round(avg_asymmetry, 3)
def check_color(image, slic_segments):
    rgb_mean_float = get_rgb_means(image, slic_segments)
    rgb_mean_int = [tuple(int(value * 255) for value in rgb) for rgb in rgb_mean_float]

    final_color_count = []

    color_thresholds = {
        "Black": ((0, 0, 0), (35, 35, 35)),
        "Dark Brown": ((48, 40, 10), (100, 90, 60)),
        "Light Brown": ((150, 100, 50), (200, 150, 115)),
        "Blue-Gray": ((90, 90, 100), (150, 150, 200)),
        "Red": ((125, 0, 0), (255, 100, 100)),
        "White": ((185, 185, 185), (255, 255, 255))
    }

    for rgb in rgb_mean_int:
        color_detected = False
        for color, (lower_thresh, upper_thresh) in color_thresholds.items():
            if all(lower <= value <= upper for value, lower, upper in zip(rgb, lower_thresh, upper_thresh)):
                final_color_count.append(color)
                color_detected = True
                break

        if not color_detected:
            final_color_count.append("Other")
            
    black_pres = False
    darkBrown_pres = False
    lightBrown_pres = False
    blueGray_pres = False
    red_pres = False
    white_pres = False
    
    # Iterate through the list of slic colors.
    for i in final_color_count:
        if i == "Black":
            black_pres = True
        if i == "Dark Brown":
            darkBrown_pres = True
        if i == "Light Brown":
            lightBrown_pres = True
        if i == "Blue-Gray":
            blueGray_pres = True
        if i == "Red":
            red_pres = True
        if i == "White":
            white_res = True

    # Output the converted RGB values
    #print("Converted RGB values:", rgb_mean_int)
    #print("Colors present:", final_color_count)
    
    
    # Returns an int value between 0 and 6s
    return int(black_pres+darkBrown_pres+lightBrown_pres+blueGray_pres+red_pres+white_pres)


def get_rgb_means(image, slic_segments):
    max_segment_id = np.unique(slic_segments)[-1]

    rgb_means = []
    for i in range(1, max_segment_id + 1):
        segment = image.copy()
        segment[slic_segments != i] = np.int8(-1)
        rgb_mean = np.mean(segment, axis=(0, 1), where=(segment != -1))
        rgb_means.append(rgb_mean) 
        
    return rgb_means

def rgb_var(image, slic_segments):
    if len(np.unique(slic_segments)) == 2:
        return 0, 0, 0

    rgb_means = get_rgb_means(image, slic_segments)
    n = len(rgb_means)

    red = []
    green = []
    blue = []
    for rgb_mean in rgb_means:
        red.append(rgb_mean[0])
        green.append(rgb_mean[1])
        blue.append(rgb_mean[2])

    red_var = variance(red, sum(red) / n)
    green_var = variance(green, sum(green) / n)
    blue_var = variance(blue, sum(blue) / n)

    return red_var, green_var, blue_var


def detect_blue_white_veil(image, mask):
    # Convert image and mask to HSV color space
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask_hsv = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for blue and white colors in HSV
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 30, 255])

    # Threshold the HSV images to get only blue and white regions
    blue_mask = cv2.inRange(image_hsv, lower_blue, upper_blue)
    white_mask = cv2.inRange(image_hsv, lower_white, upper_white)

    # Bitwise-AND mask and original image
    blue_region = cv2.bitwise_and(mask, mask, mask=blue_mask)
    white_region = cv2.bitwise_and(mask, mask, mask=white_mask)

    # Combine blue and white regions
    blue_white_veil = cv2.add(blue_region, white_region)

    # Calculate the ratio of bluewhiteveil pixels to the total lesion pixels
    total_pixels = np.count_nonzero(mask)
    bluewhiteveil_pixels = np.count_nonzero(blue_white_veil)
    bluewhiteveil_ratio = bluewhiteveil_pixels / total_pixels if total_pixels > 0 else 0

    return bluewhiteveil_ratio


