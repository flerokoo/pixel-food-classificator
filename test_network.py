import numpy as np
from utils import get_dataset, predict, id_to_vector, vector_to_id, \
    zip_converter, grayscale_converter, concat_converter, channel_converter, avg_converter
import image_generator
import options

TESTSET_PATH = "testset"

def run_test(dataset, weights):
    right = 0
    for el in dataset:
        id = el["id"]
        data = el["data"]    
        prediction = vector_to_id(predict(data, weights))
        right = right + (1 if prediction == id else 0)         
    return right/len(dataset)

if __name__ == "__main__":    
    image_generator.generate_set(TESTSET_PATH, options.test_set_elements, force_overwrite=False)
    weights = np.load("weights.npy")
    testset = get_dataset(TESTSET_PATH, image_to_data_converter=options.default_converter)
    percentage = run_test(testset, weights)
    print(percentage)
    
    