"""Launch fiftyone with dataset.
"""

from configs import cfg  # import first, set env variables for fiftyone
import fiftyone as fo

dataset = fo.Dataset.from_dir(
    dataset_type = fo.types.COCODetectionDataset,
    label_types = ["detections", "segmentations", "keypoints"],
    data_path = f'{cfg.DATASET.COCO.ROOT}/images/val2017',
    labels_path = f'{cfg.DATASET.COCO.ROOT}/annotations/person_keypoints_val2017.json')

session = fo.launch_app(dataset, port=5151)
session.wait()



