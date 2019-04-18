import numpy as np
from utils import get_dataset, predict, id_to_vector, vector_to_id, \
    zip_converter, grayscale_converter, concat_converter
import image_generator

TESTSET_PATH = "testset"
image_generator.generate_set(TESTSET_PATH, 100, force_overwrite=False)

weights = np.load("weights.npy")
testset = get_dataset(TESTSET_PATH, image_to_data_converter=zip_converter)

right = 0
for el in testset:
    id = el["id"]
    data = el["data"]    
    prediction = vector_to_id(predict(data, weights))
    right = right + (1 if prediction == id else 0)
    print("{} -> {}".format(prediction, id))
    
print("right answers percentage: ", 100 * right/len(testset))
    