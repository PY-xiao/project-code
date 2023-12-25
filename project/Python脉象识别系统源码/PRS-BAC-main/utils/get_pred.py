import os

import numpy as np
import pandas as pd
from keras.models import load_model


def get_pred(file_path):
    os_path = os.getcwd()
    model_path = os_path + f'/utils/model.h5'
    model = load_model(model_path)

    data = []
    text = pd.read_csv(file_path, header=None).sort_values(1)
    data.append(text.iloc[:, 0].to_numpy())
    data = np.array(data)
    data_list = np.array(data)

    pred = [0 if x < 0.5 else 1 for x in model.predict(data_list)]
    results = 0
    if isinstance(pred, list):
        results = pred[0]

    return results


if __name__ == '__main__':
    pred = get_pred('/Users/mac/workspace/PRS/media/0text1clear.csv')
    print(pred)
