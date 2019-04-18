# Pixel Food Classificator

## Machine Learning Project

__Goal of the project__: teach neural network Bob to recognize different types of food from drawings without using any ML-related third party libraries.

In Bob's world there are three types of food: burgers, fries and pepsi. 

![Today's Menu](https://raw.githubusercontent.com/flerokoo/pixel-food-classificator/master/pics/menu.png)

Images of food for training and testing are generated with help of Pillow library in `image_generator.py` script. 

Neural network trained on a dataset of 500 32x32 images is showing following results:

| Format of input data  | Percentage of correct predictions, %  |  
|---|---|
| Grayscale = 0.2126R + 0.7152G + 0.0722B | 42-48  |
| [R0, G0, B0, ... R1024, G1024, B1024] | 66-68 |
| Avg = (R + G + B)/3 | 33-34 |




## Usage

```
python train_network.py
python test_network.py
```

Check `options.py` to adjust some values that may affect the result