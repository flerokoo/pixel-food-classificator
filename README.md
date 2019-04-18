# Pixel Food Classificator

## Machine Learning Project

__Goal of the project__: teach neural network Bob to recognize different types of food from drawings without using any ML-related third party libraries.

In Bob's world there are three types of food: burgers, fries and pepsi. 

![Today's Menu](https://raw.githubusercontent.com/flerokoo/pixel-food-classificator/master/pics/menu.png)

Images of food for training and testing are generated with help of Pillow library in `image_generator.py` script. 

Neural network was trained on datasets consisting of 10-200 32x32 images with 1-10 epochs. Results are on the following plot:

![Percentage of correct answers](https://raw.githubusercontent.com/flerokoo/pixel-food-classificator/master/pics/plots.png)


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