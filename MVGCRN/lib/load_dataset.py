import os
import numpy as np
import pandas as pd

def load_st_dataset(dataset):
    #output B, N, D
    if dataset == 'FirstRingRoad':
        data_path = os.path.join('./data/FirstRingRoad/FirstRingRoad.npz')
        data = np.load(data_path)['data'][:, :, 0]  #onley the first dimension, traffic flow data
    elif dataset == 'PiduDistrict':
        data_path = os.path.join('./data/PiduDistrict/PiduDistrict.npz')
        data = np.load(data_path)['data'][:, :, 0]  #onley the first dimension, traffic flow data
    else:
        raise ValueError
    if len(data.shape) == 2:
        data = np.expand_dims(data, axis=-1)
    print('Load %s Dataset shaped: ' % dataset, data.shape, data.max(), data.min(), data.mean(), np.median(data))
    return data

