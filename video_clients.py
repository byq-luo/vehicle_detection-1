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
parser.add_argument('-i', type=str, default="./1.mp4", help="input video")
parser.add_argument('-o', type=str, default="./output.avi", help="input video")
args = parser.parse_args()
#videos
if __name__ == "__main__":
    input = args.i
    output = args.o
    cap = cv2.VideoCapture(input)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(args.o, cv2.VideoWriter_fourcc(
        'M', 'J', 'P', 'G'), 25, (frame_width, frame_height))

    while(True):
        ret, image = cap.read()
        if ret == True:
            start = time.time()
            bboxes = detect.vehicle_detection(image)
            # print("bboxes: ", bboxes)
            image = utils.draw_bbox(image, bboxes)
            print("processing time: ", time.time() - start)
            out.write(image)
    cap.release()
    out.release()