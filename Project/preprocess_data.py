import pandas as pd
import numpy as np
from configuration import *
from utils.dataset_preprocessing import preprocessing

urldata = pd.read_csv(DATASET_PATH)
# print(urldata.head(10))

preprocessed_df = preprocessing(urldata)
# print(preprocessed_df.head())
preprocessed_df.to_csv(PREPROCESSED_DATASET)
