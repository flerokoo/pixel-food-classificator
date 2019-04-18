# Pixel Food Classificator

## Machine Learning Learning Project

__Goal of the project__: teach neural network Bob to recognize different types of food from drawings without using any ML-related third party libraries.

In Bob's world there are three types of food: burgers, fries and pepsi. 

![Today's Menu](https://raw.githubusercontent.com/flerokoo/pixel-food-classificator/master/pics/menu.png)

Images of food for training and testing are generated with help of Pillow library in `image_generator.py` script. 

Neural network was trained on datasets consisting of 10-200 32x32 images with 1-10 epochs. Results are on the plots.

### Zipped channels
Images was piped into neural network in following format:
```
data = [R0, G0, B0, ... Ri, Gi, Bi, ... R1024, G1024, B1024]
```

![Zipped channels](https://raw.githubusercontent.com/flerokoo/pixel-food-classificator/master/pics/plots.png)

### Grayscale
Here images was converted to grayscale mode
```
Gi = 0.2126Ri + 0.7152Gi + 0.0722Bi
data = [G0, ... Gi, ... GN]
```

![Zipped channels](https://raw.githubusercontent.com/flerokoo/pixel-food-classificator/master/pics/plots_grayscale.png)

For some reason grayscale-network does its job better than zip-network when both are trained on small sets. On big sets zip-network classifies with almost 100% probability when grayscale-networks tops out at ~96%.


## Usage

Generate images and train NN
```
python train_network.py
```

Generate more images and test NN on 'em
```
python test_network.py
```

Check `options.py` to adjust some values that may affect the result