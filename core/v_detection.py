
import argparse
import numpy as np
import os
import colorsys
from builtins import range
from PIL import Image
from PIL import ImageFont, ImageDraw
from tensorrtserver.api import *
import tensorrtserver.api.model_config_pb2 as model_config
import time
import core.utils as utils
import cv2



def vehicle_detection(image):
    protocol = ProtocolType.from_str('http')

    input_name = 'input/input_data'
    sboxes = 'pred_sbbox/concat_2'
    mboxes = 'pred_mbbox/concat_2'
    lboxes = 'pred_lbbox/concat_2'
    model_name = 'vehicle-detector'



    ctx = InferContext('localhost:8000', protocol, model_name, -1, False)

    ori_size = image.shape[:2]
    image_preprocess = utils.image_preporcess(image, [416, 416])
    
    image_data = []
    image_data.append(image_preprocess)
    result = []
    image_idx = 0
    request_ids = []
    batch_size = 4
    last_request = False

    input_batch = []
    while not last_request:
        input_batch = []
        for idx in range(batch_size):
            input_batch.append(image_data[image_idx])
            image_idx = (image_idx + 1) % len(image_data)
            if image_idx == 0:
                last_request = True
                batch_size = len(input_batch)
                break
        request_ids.append(ctx.async_run(
             {input_name: input_batch},
             {sboxes: (InferContext.ResultFormat.RAW),
             mboxes: (InferContext.ResultFormat.RAW),
             lboxes: (InferContext.ResultFormat.RAW)},
             batch_size))

    raw_results = []
    num_classes = 80
    # # For async, retrieve results according to the send order
    for request_id in request_ids:
        raw_results.append(ctx.get_async_run_results(request_id, True))
    for ix in range(len(raw_results)):
        pred_sbbox, pred_mbbox, pred_lbbox = raw_results[ix]['pred_sbbox/concat_2'], raw_results[ix]['pred_mbbox/concat_2'], raw_results[ix]['pred_lbbox/concat_2']
        pred_bbox = np.concatenate([np.reshape(pred_sbbox, (-1, 5 + num_classes)),
                                np.reshape(pred_mbbox, (-1, 5 + num_classes)),
                                np.reshape(pred_lbbox, (-1, 5 + num_classes))], axis=0)
        bboxes = utils.postprocess_boxes(pred_bbox, ori_size, 416, 0.3)
        bboxes = utils.nms(bboxes, 0.45, method='nms') 
        return bboxes
