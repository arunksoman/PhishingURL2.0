import os
import glob

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "Dataset")
DATASET_PATH = os.path.join(DATASET_DIR, "urldata.csv")
PREPROCESSED_DIR = os.path.join(BASE_DIR, 'Preprocessed_dataset')
PREPROCESSED_DATASET = os.path.join(PREPROCESSED_DIR, 'new_urldata.csv')
