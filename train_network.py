from scipy import misc
import os
import numpy as np
import cv2
import image_generator
from utils import get_dataset, predict, id_to_vector, zip_converter, \
    concat_converter, grayscale_converter

DATASET_PATH = "trainset"

def train(dataset, learning_rate, num_variants=3):
    """
    Shape of dataset: [{id, label, filepath, image},...]
    """        
    if len(dataset) == 0:
        raise "error: empty dataset given"

    weights_shape = (len(dataset[0]["data"]), num_variants)
    weights = np.random.random(weights_shape)
    for (i, el) in enumerate(dataset):
        print("Processing image {}: {}".format(i, el["filename"]))
        id = el["id"]
        data = el["data"]
        prediction = predict(data, weights)
        err = id_to_vector(id) - prediction
        dweights = 0.005 * err * np.reshape(data, (weights_shape[0], 1))  # TODO play with learning rate
        weights = weights + dweights

    return weights


image_generator.generate_set(DATASET_PATH, 500, force_overwrite=False)

dataset = get_dataset(DATASET_PATH, image_to_data_converter=zip_converter)

weights = train(dataset, learning_rate=0.005)

np.save("weights", weights)
print(weights)