import utils

# function that converts raw output from cv2.imread()
# to data format that can be fed to training algorithm
# signature: [[[int]]] -> [int]
default_converter = utils.zip_converter

# size of images to generate
image_size = 32

# number of images to generate for training 
train_set_elements = 100

# how many times NN should be trained on generated training set
epochs=10

# number of images to generate for evaluating 
# correctness of predictions
test_set_elements = 100

# self explanatory
learning_rate = 0.01






