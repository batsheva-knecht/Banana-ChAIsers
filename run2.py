import json
from pathlib import Path

import hailo
import numpy as np
import math
import serial
import time
from enum import Enum
import random

# Importing VideoFrame before importing GST is must
from gsthailo import VideoFrame
from gi.repository import Gst

BREAK=0
FOR=1
BACK=2
RIGHT=3
LEFT=4

# # -----------------------------------------------------------------------------------
# import time

# # Constants for camera resolution
# CAMERA_WIDTH = 1.0
# CAMERA_HEIGHT = 1.0

# # Constants for the desired position of the object in the frame
# TARGET_X_CENTER = 0.5
# TARGET_Y_CENTER = 0.5
# TARGET_DISTANCE = 0.2

# # Constants for controlling robot movement
# TURN_ANGLE = 30  # in degrees
# FORWARD_DURATION = 1.0  # in seconds

# # Function to calculate the distance between two points
# def calculate_distance(x1, y1, x2, y2):
#     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# # Function to move the robot based on object position and distance
# def move_robot(object_center_x, object_center_y, object_distance):
#     # Check if the object is centered horizontally
#     if object_center_x < TARGET_X_CENTER - 0.05:
#         turn_left()
#     elif object_center_x > TARGET_X_CENTER + 0.05:
#         turn_right()
#     else:
#         stop()

#     # Check if the object is close enough
#     if object_distance > TARGET_DISTANCE:
#         move_forward()
#         time.sleep(FORWARD_DURATION)
#         stop()

# # Main loop
# while True:
#     # Simulating camera input by random values
#     object_x_min = 0.2
#     object_y_min = 0.3
#     object_x_max = 0.8
#     object_y_max = 0.6

#     # Calculate the object's center position
#     object_center_x = (object_x_min + object_x_max) / 2
#     object_center_y = (object_y_min + object_y_max) / 2

#     # Calculate the distance from the object to the camera
#     object_distance = calculate_distance(object_center_x, object_center_y, TARGET_X_CENTER, TARGET_Y_CENTER)

#     # Move the robot based on object position and distance
#     move_robot(object_center_x, object_center_y, object_distance)
# # -----------------------------------------------------------------------------------

# img_net_path = Path(__file__).parent.resolve(strict=True) / "imagenet_labels.json"
# img_net_labels = json.loads(img_net_path.read_text())


# def top1(array: np.ndarray):
#     return np.argsort(-1 * array)[0]
stream_dict = {"2b7f5679e9f0cee0776e7c9d96ffc3b4682b26f7b8931798b4254fc99bdbde9b":"0",
               "74387e2bbc5adbd216100f574a3d7fd368e2c2f6c5acdd0179e4f5645e887372":"1"}

# serialcomm = serial.Serial('COM6', 9600)
# serialcomm.timeout = 1

def drive(stream_id, detection):
    xmin = detection.get('xmin')
    ymin = detection.get('ymin')
    xmax = detection.get('xmax')
    ymax = detection.get('ymax')
    x_center = (xmax + xmin)/2
    y_center = (ymax + ymin)/2
    # print(f"center {x_center}, {y_center}")
    # diagonal = math.dist(xmin, ymax)
    diagonal = math.sqrt(math.pow((xmax - xmin),2) + math.pow((ymax - ymin),2))
    print(f"diagonal:: {diagonal}")
    is_close_to_center = np.allclose([0.5, 0.5], [x_center, y_center], rtol=0.1)
    if (is_close_to_center and diagonal >= 0.4 ):
        print("Centered + close!!")
    # order = 
    # serialcomm.write(i.encode())
    return
    
    
def run(video_frame: VideoFrame):
    roi = video_frame.roi
    stream_id = roi.get_stream_id()
    dets = hailo.get_hailo_detections(roi)
    detections = []
    for det in dets:
        label = det.get_label()
        if label == "banana":
            print("found a banana!")
            print(f"in stream: {stream_dict.get(stream_id)}")
            bbox = det.get_bbox()
            print(f"bbox: {bbox.xmin()} {bbox.xmax()}  {bbox.ymin()}  {bbox.ymax()}")
            
            confidence = det.get_confidence()
            
            xmin = np.clip(bbox.xmin(), 0, 1)
            ymin = np.clip(bbox.ymin(), 0, 1)
            xmax = np.clip(bbox.xmax(), 0, 1)
            ymax = np.clip(bbox.ymax(), 0, 1)
            detection = {'label':label,
                        'confidence': confidence,
                        'xmin' : xmin,
                        'ymin' : ymin,
                        'xmax' : xmax,
                        'ymax' : ymax
                        }
            drive(stream_id, detection)
            
            detections.append(detection)


    # results = video_frame.roi.get_tensor("resnet_v1_50/softmax1")
    
    # if results is None:
    #     return Gst.FlowReturn.ERROR

    # arr = np.squeeze(np.array(results, copy=False))

    # best_index = top1(arr)
    # label = img_net_labels[str(best_index)].split(',')[0]
    # confidence = round(results.fix_scale(arr[best_index]), 2)

    # # add_classification function is in hailo_common.hpp and needs to be binded to python
    # top_1_classification = hailo.HailoClassification("imagenet", best_index,
    #                                                  label, confidence)
    # video_frame.roi.add_object(top_1_classification)

    return Gst.FlowReturn.OK