# Computer vision annotation workflow

## CVAT-fiftyone annotation workflow

1. Start [CVAT](https://github.com/openvinotoolkit/cvat) in Docker
2. Create .env file with CVAT credentials (see .env.example)
3. Start a cvat_*.ipynb notebook

Paths to datasets can be added/adjusted in configs/default.py.

**Note**: CVAT does currently not support labeled keypoints (e.g., COCO format).

## coco-annotator annotation workflow

Check:
- [coco-annotator-setup.md](docs/coco-annotator-setup.md) for working with the coco annotator
- [human_keypoint_annotation.md](docs/human_keypoint_annotation.md) for a keypoint-annotation guideline

