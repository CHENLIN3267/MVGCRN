import os
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from lib.util import load_adj1

def load_adj_poi(dataset):
    #output B, N, D
    if dataset == 'FirstRingRoad':
        data_path = os.path.join('./data/FirstRingRoad/POI_data.csv')
        data = pd.read_csv(data_path,header=0)
    elif dataset == 'PiduDistrict':
        data_path = os.path.join('./data/PiduDistrict/POI_data.csv')
        data = pd.read_csv(data_path,header=0)  #onley the first dimension, traffic flow data
    else:
        raise ValueError

    feature_columns = data.columns[1:-1]  # 取除id和poi个数外的所有列
    poi_data = data[feature_columns].values.astype(np.float32)  # 形状 [N, 21]
    # 计算所有虚拟停车场之间的余弦相似性
    data = cosine_similarity(poi_data)
    print("\n相似性矩阵的形状：", data.shape)
    data = load_adj1(data, "scalap")


    return data

#
# data_path = os.path.join('../data/PeMS07/PEMS07.npz')
# data = np.load(data_path)['data'][:, :, 0]  # onley the first dimension, traffic flow data
