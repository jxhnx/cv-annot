# Computer vision annotation workflow

## CVAT-fiftyone annotation workflow

1. Start [CVAT](https://github.com/openvinotoolkit/cvat) in Docker
2. Create .env file with CVAT credentials (see .env.example)
3. Start a cvat_*.ipynb notebook

Paths to datasets can be added/adjusted in configs/default.py.

**Note**: CVAT does currently not support labeled keypoints (e.g., COCO format).

## coco-annotator(-fiftyone) annotation workflow (keypoint example)

1. Start [coco-annotator](https://github.com/jsbroks/coco-annotator) in Docker and open the app (default: http://localhost:5000)
2. Create a new dataset with the label "person": coco-annotator will create a new folder in its root/datasets directory
3. Copy the contents of /data/coco_keypoint_example/ in the newly created folder
4. Open the created dataset in coco-annotator and click scan: coco-annotator will import all added pictures
5. Import the example.json file with "Import COCO": coco-annotator will create a new category "person" with keypoints in the COCO format. Furthermore, the example picture will be annotated according to the .json-file. The coloring of the keypoints can be adjusted in the categories tab.
6. Annotate (see below for hints).
7. Use "Export COCO" to download the updated .json-file.
8. (optional) load the dataset into fiftyone with coco_annotator_keypoints.ipynb; after updating the paths in the config file (default.py).

**Note [macOS]**: In order to run coco-annotator on macOS, the docker compose file needs two changes. See [here](https://github.com/jsbroks/coco-annotator/compare/master...random9v2:coco-annotator:macos#diff-e45e45baeda1c1e73482975a664062aa56f20c03dd9d64a827aba57775bed0d3).

**Annotation (keypoint example)**:
- In a dataset, click on a picture to open it. In the top right corner, add a label (e.g., person).
- Choose the keypoint tool in the left sidebar (k).
- Add all keypoints for one person. The current keypoint to be assigned is highlighted in the right sidebar.
- In most cases it is quickest to cycle through a whole person first and to adjust keypoint visibility later. Keypoints out of bounds (not in the picture) have to be deleted. They can either be deleted by clicking the trash icon, or by choosing the keypoint in the picture and to hit delete. Hidden (occluded) keypoints have to be labeled as such. Double-click a keypoint in the picture and change the lable to "LABELED NOT_VISIBLE". Do **not** choose "NOT LABELED" – it does not follow the [COCO standard](https://cocodataset.org/#format-data).
- People are always labeled from their point of view. The right arm is the right arm of the labled person, not the right arm facing the camera.
- Once one person is added, additional people can be added to the same picture, following the same workflow.
- Save with the save button (left sidebar) or switch to the next picture.
- Click on image settings (left sidebar) to show or/and adjust the keyboard shortcuts. 
- [Official documentation](https://github.com/jsbroks/coco-annotator/wiki)