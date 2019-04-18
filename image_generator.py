from PIL import Image, ImageDraw
import os
import random
import math
import options

IMAGE_SIZE = options.image_size
CRUST_COLOR = (214, 144, 40)
PATTY_COLOR = (114, 45, 8)
LETTUCE_COLOR = (170, 221, 0)
TOMATO_COLOR = (221, 33, 0)
CHEESE_COLOR = (255, 195, 0)
FRIES_COLOR = (255, 195, 0)
FRIES_BOX_COLOR = (255, 0, 0)
STRAW_COLOR = (255, 255, 0)
CAP_COLOR = (240, 240, 245)
CUP_COLOR = (255, 0, 0) # cola
CUP_COLOR = (0, 52, 211) # pepsi

CONDIMENTS_COLORS = [
    PATTY_COLOR,
    LETTUCE_COLOR,
    TOMATO_COLOR,
    CHEESE_COLOR
]

def get_base_path():
    return os.path.dirname(os.path.abspath(__file__))

def get_safe_zone_size(size):
    return math.sqrt(2) / 2 * size

def get_safe_zone_rect(size):
    safe = get_safe_zone_size(size)
    pads = (size - safe)/2
    return [pads, pads, size - pads, size - pads]
    

def generate_burger(output, size=IMAGE_SIZE):
    image = Image.new("RGBA", (size, size))
    draw = ImageDraw.Draw(image)
    
    w = size * 0.5 + random.random() * size * 0.5
    h = size * 0.5 + random.random() * size * 0.5
    x0 = (size - w) / 2
    y0 = (size - h) / 2

    bunsize = h * 0.15
    draw.pieslice([x0, y0, x0 + w, y0 + bunsize * 2], 180, 360, CRUST_COLOR)
    draw.pieslice([x0, y0 + h - bunsize * 2, x0 + w, y0 + h], 0, 180, CRUST_COLOR)

    y = y0 + bunsize
    maxpartsize = h * 0.15
    minpartsize = h * 0.1

    while y < y0 + h - bunsize:
        partsize = random.random() * (maxpartsize - minpartsize) + minpartsize
        partsize = min(partsize, y0 + h - bunsize - y)       
        draw.rectangle([x0, y, x0+w, y + partsize], fill=random.choice(CONDIMENTS_COLORS))
        y = y + partsize

    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    image.save(output)

def generate_fries(output, size=IMAGE_SIZE):
    image = Image.new("RGBA", (size, size))
    draw = ImageDraw.Draw(image)
    
    w = size * 0.5 + random.random() * size * 0.5
    h = size * 0.5 + random.random() * size * 0.5
    x0 = (size - w) / 2
    y0 = (size - h) / 2
    cupw = w - w * (random.random() * 0.1 + 0.1)
    cuph = h * 0.4 + h * 0.4 * random.random()

    num = random.randint(5, 10)
    for _ in range(num):
        fw = random.random() * w * 0.1 + w * 0.05;
        fx = random.random() * (w - fw) + x0
        draw.rectangle([fx, y0 + random.random() * h * 0.1, fx + fw, y0 + h - cuph], fill=FRIES_COLOR)

    
    draw.polygon([
        x0, y0 + h - cuph,
        x0 + w, y0 + h - cuph,
        x0 + w/2 + cupw/2, y0 + h,
        x0 + w/2 - cupw/2, y0 + h,
    ], fill=FRIES_BOX_COLOR)

    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    image.save(output)

def generate_cola(output, size=IMAGE_SIZE):
    image = Image.new("RGBA", (size, size))
    draw = ImageDraw.Draw(image)
    
    w = size * 0.5 + random.random() * size * 0.5
    h = size * 0.5 + random.random() * size * 0.5
    x0 = (size - w) / 2
    y0 = (size - h) / 2

    straw_w = random.random() * 5 + 10 * (size / 150)
    draw.rectangle([
        x0 + w / 2 - straw_w / 2,        
        y0,
        x0 + w / 2 + straw_w / 2,
        y0 + h
    ], fill=STRAW_COLOR)
    draw.rectangle([
        x0 + w / 2 - straw_w / 2,        
        y0,
        x0 + w,
        y0 + straw_w
    ], fill=STRAW_COLOR)
    
    cupw = w - w * (random.random() * 0.1 + 0.1)
    cuph = h * 0.4 + h * 0.4 * random.random()
    draw.polygon([
        x0, y0 + h - cuph,
        x0 + w, y0 + h - cuph,
        x0 + w/2 + cupw/2, y0 + h,
        x0 + w/2 - cupw/2, y0 + h,
    ], fill=CUP_COLOR)
    draw.rectangle([
        x0, y0 + h - cuph,
        x0 + w, y0 + h - cuph + 10 * (size/150)
    ], fill=CAP_COLOR)
    
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    image.save(output)



def generate_set(dirname, n=50, force_overwrite=False):
    # print("generating set \"{}\"".format(dirname))
    base_path = "./{}/".format(dirname)

    if (os.path.exists(base_path) and not force_overwrite):
        # print("set already generated")
        return

    for i in range(n):
        generate_burger(base_path + "/burger/burger_{}.png".format(i))
        generate_cola(base_path + "/cola/cola_{}.png".format(i))
        generate_fries(base_path + "/fries/fries_{}.png".format(i))