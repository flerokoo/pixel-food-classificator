from scipy import misc
import os
import numpy as np
import cv2
import shutil

BURGER = 0
FRIES = 1
COLA = 2

def get_labels(dataset_path):
    return os.listdir(dataset_path)


def label_to_id(label):
    return {
        "burger": BURGER,
        "fries": FRIES,
        "cola": COLA
    }[label.lower()]    

def id_to_vector(id, num_variants = 3):
        ret = [0 for _ in range(num_variants)]
        ret[id] = 1
        return np.array(ret)

def vector_to_id(vec, target = 1):
    minIndex = 0
    minDist = 100000000
    for (i, x) in enumerate(vec):
        if abs(x - target) < minDist:
            minDist = abs(x - 1)
            minIndex = i
    return minIndex


def extractChannel(image, channelId):
    ret = []
    for row in image:
        for col in row:
            ret.append(col[channelId])
    return np.array(ret)

def normalize(a, max=255):
    return np.array([i/max for i in a])

def get_dataset(dataset_path, image_to_data_converter):
    # print("reading dataset \"{}\"".format(dataset_path))
    labels = get_labels(dataset_path)
    ret = []       

    for label in labels:
        id = label_to_id(label)
        label_path = os.path.join(dataset_path, label)
        
        for filename in os.listdir(label_path):
            filepath = os.path.join(label_path, filename)   
            image = cv2.imread(filepath)
            data = image_to_data_converter(image)

            ret.append({
                "id": id,
                "label": label,
                "filename": filename,
                "filepath": filepath,
                "data": data
            })
    return ret;

def predict(data, weights):
    dot_product = np.dot(data, weights)
    return 1 / (1 + np.exp(-dot_product))


def to_channel_arrays(image):
    return (
        normalize(extractChannel(image, 0)),
        normalize(extractChannel(image, 1)),
        normalize(extractChannel(image, 2))
    )
    
def cleanup(path):
    shutil.rmtree(path, ignore_errors=True)


###################### CONVERTERS ##########################

def channel_converter(channel, image):
    return normalize(extractChannel(image, channel))

def grayscale_converter(image):
    (red, green, blue) = to_channel_arrays(image)    
    grayscale = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    return grayscale

def concat_converter(image):
    (red, green, blue) = to_channel_arrays(image)   
    return np.concatenate([red, green, blue])

def zip_converter(image):
    (red, green, blue) = to_channel_arrays(image)
    zipped = np.array(list(zip(red, green, blue)))
    zipped = zipped.flatten()
    return zipped
    
def avg_converter(image):
    (red, green, blue) = to_channel_arrays(image)    
    grayscale = (red + green + blue)/3
    return grayscale