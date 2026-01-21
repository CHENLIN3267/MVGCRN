import os
import numpy as np
import pandas as pd
from lib.util import load_adj1

def load_adj(dataset):
    #output B, N, D
    if dataset == 'FirstRingRoad':
        data_path = os.path.join('./data/FirstRingRoad.csv')
        data = np.array(pd.read_csv(data_path,header=None))
    elif dataset == 'PiduDistrict':
        data_path = os.path.join('./data/PiduDistrict.csv')
        data = np.array(pd.read_csv(data_path,header=None))  #onley the first dimension, traffic flow data
    else:
        raise ValueError
    # if len(data.shape) == 2:
    #     data = np.expand_dims(data, axis=-1)
    print('Load %s Dataset shaped: ' % dataset, data.shape, data.max(), data.min(), data.mean(), np.median(data))
    data = load_adj1(data, "scalap")
    return data

#
# data_path = os.path.join('../data/PeMS07/PEMS07.npz')
# data = np.load(data_path)['data'][:, :, 0]  # onley the first dimension, traffic flow data
