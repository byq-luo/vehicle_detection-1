import numpy as np
import os
from PIL import Image
from PIL import ImageFont, ImageDraw
import time
import core.utils as utils
import core.v_detection as detect
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', type=str, default="./1.jpg", help="input video")
parser.add_argument('-o', type=str, default="./result_sv.jpg", help="input video")
args = parser.parse_args()
#images
if __name__ == "__main__":
    image = cv2.imread(args.i)
    bboxes = detect.vehicle_detection(image)
    image = utils.draw_bbox(image, bboxes)
    image = Image.fromarray(image)
    image.save(args.o)