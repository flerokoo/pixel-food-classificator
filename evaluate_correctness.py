from train_network import train, DATASET_PATH
from test_network import run_test
from utils import cleanup, get_dataset
import options
import image_generator
import numpy as np



if __name__ == "__main__":
    num_epochs = 10
    sizes = [10, 40, 100]
    for dataset_size in sizes:
        # training NN with num_epochs and dataset_size params
        cleanup("eva_train_set")
        image_generator.generate_set("eva_train_set", dataset_size)
        dataset = get_dataset("eva_train_set", options.default_converter)
        weights = train(dataset, options.learning_rate)
        for epoch in range(0, num_epochs):                
            print("epoch {}/{} with dataset size={}".format(epoch, num_epochs, dataset_size))            
            weights = train(dataset, options.learning_rate, weights)            

            # testing NN that we just trained
            # generate once
            image_generator.generate_set("eva_test_set", 100)
            dataset = get_dataset("eva_test_set", options.default_converter)
            result = run_test(dataset, weights)
            print(result)


