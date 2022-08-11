"""Default project config.
"""

import os

from dotenv import load_dotenv
from yacs.config import CfgNode as CN

load_dotenv()
_C = CN()

# Set environment variables
os.environ['FIFTYONE_CVAT_USERNAME'] = os.getenv('FIFTYONE_CVAT_USERNAME')
os.environ['FIFTYONE_CVAT_PASSWORD'] = os.getenv('FIFTYONE_CVAT_PASSWORD')

# Datasets
_C.DATASET = CN()
# ROOT/annotations/[file] and ROOT/images/[coco_set]/(images)
_C.DATASET.COCO = CN()
_C.DATASET.COCO.ROOT = 'data/coco'
# ROOT/json/[file] and ROOT/[images]/(images)
_C.DATASET.CROWD_POSE = CN()
_C.DATASET.CROWD_POSE.ROOT = 'data/crowd_pose'
