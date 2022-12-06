import os
from shutil import copyfile

import cv2
from numpy import imag

"""
Make dataset for multi-task net by combining detection(yolo format) and segmentation(masks) datasets.
"""

# You only need to change this line to your dataset root path
root_path = "/mnt/ext/data/temp"
if not os.path.exists(root_path):
    print(f"{root_path} is not exist, please check!")
    exit(0)

images_path = root_path + "/images"
if not os.path.exists(images_path):
    os.makedirs(images_path)

labels_path = root_path + "/labels"
if not os.path.exists(labels_path):
    os.makedirs(labels_path)

masks_path = root_path + "/masks"
if not os.path.exists(masks_path):
    os.makedirs(masks_path)

src_paths = ["temp1", "temp2"]
types = ["train", "val"]

for type in types:
    # source path1
    images_path1 = root_path + f"/{src_paths[0]}/images/{type}"
    if not os.path.exists(images_path1):
        print(f"{images_path1} is not exist, please check!")
        exit(0)

    labels_path1 = root_path + f"/{src_paths[0]}/labels/{type}"
    if not os.path.exists(labels_path1):
        print(f"{labels_path1} is not exist, please check!")
        exit(0)

    # source path2
    images_path2 = root_path + f"/{src_paths[1]}/images/{type}"
    if not os.path.exists(images_path2):
        print(f"{images_path2} is not exist, please check!")
        exit(0)

    masks_path2 = root_path + f"/{src_paths[1]}/masks/{type}"
    if not os.path.exists(masks_path2):
        print(f"{masks_path2} is not exist, please check!")
        exit(0)

    # destination path
    save_images_path = images_path + f"/{type}"
    if not os.path.exists(save_images_path):
        os.makedirs(save_images_path)

    save_labels_path = labels_path + f"/{type}"
    if not os.path.exists(save_labels_path):
        os.makedirs(save_labels_path)

    save_masks_path = masks_path + f"/{type}"
    if not os.path.exists(save_masks_path):
        os.makedirs(save_masks_path)

    for root, dirs, files in os.walk(images_path1, topdown=True):
        for name in files:

            if not name[-3:]=='jpg':
                continue
            name = name[:-4]

            image_path = os.path.join(images_path2, name + ".jpg")
            label_path = os.path.join(labels_path1, name + ".txt")
            mask_path = os.path.join(masks_path2, name + "_bin.png")

            if not os.path.exists(image_path) \
                or not os.path.exists(label_path) \
                or not os.path.exists(mask_path):
                continue

            dst_path = os.path.join(save_images_path, name + ".jpg")
            print(f"copy {image_path} to {dst_path}")
            os.popen(f"cp -rv {image_path} {dst_path}")

            dst_path = os.path.join(save_labels_path, name + ".txt")
            print(f"copy {label_path} to {dst_path}")
            os.popen(f"cp -rv {label_path} {dst_path}")

            dst_path = os.path.join(save_masks_path, name + "_bin.png")
            print(f"copy {mask_path} to {dst_path}")
            os.popen(f"cp -rv {mask_path} {dst_path}")

            print()
