# Multi-View Graph Convolutional Recurrent Networks for Parking Demand Forecasting in Virtual Parking Lots

This is a PyTorch implementation of [Multi-View Graph Convolutional Recurrent Networks for Parking Demand Forecasting in Virtual Parking Lots].

## Table of Contents

* config_file: training Configs and model configs for each dataset

* lib: contains self-defined modules for our work, such as data loading, data pre-process, normalization, and evaluate metrics.

* model: implementation of our model 

# Data Preparation

These datasets are available for research purposes upon request via email to chenlin99@mail2.sysu.edu.cn.

# Requirements

Python 3.6.5, Pytorch 1.9.0, Numpy 1.16.3, argparse and configparser

# Model Training

```bash
python run.py --datasets {DATASET_NAME} --mode {MODE_NAME}
```
Replace `{DATASET_NAME}` with one of `FirstRingRoad`, `PiduDistrict`

such as `python run.py --datasets FirstRingRoad`

There are two options for `{MODE_NAME}` : `train` and `test`

Selecting `train` will retrain the model and save the trained model parameters and records in the `experiment` folder.

With `test` selected, run.py will import the trained model parameters from `{DATASET_NAME}.pth` in the 'pre-trained' folder.


