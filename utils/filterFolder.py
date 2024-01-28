from config.config import datadir

import logging
import glob
import os


def filter_folder_by_ext(ext):
    logging.info(f"Filtering Folder based on {ext} ...")
    result_folders = []
    for root, dirs, files in os.walk(datadir):
        if "labels" in dirs:
            labels_folder = os.path.join(root, "labels")
            label_files = [file for file in os.listdir(labels_folder) if file.endswith(ext)]

            # Check if all files in the "labels" folder have the ".xml" extension
            if all(file.endswith(ext) for file in label_files) and label_files:
                result_folders.append(root)

    logging.info(f"Detected {len(result_folders)} folders have {ext} extenstions")
    return result_folders
    