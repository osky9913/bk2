import os
import random

from config_global import TEETH_DATASET_PATH
from config_global import teeth_class
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


models = [os.path.join(model.path,'input') for model in os.scandir(TEETH_DATASET_PATH)]
X =  []

for model in models:
    images = os.scandir(model)
    for image in images:
        X.append(image.path)

number_of_plot = 4
for plot in range(number_of_plot):
    selected_input_path = X[random.randint(1, len(X))]
    masks_path = []
    for t_class in teeth_class:
        masks_path.append(selected_input_path.replace('input', t_class+os.sep+'binary_mask'))

    fig, ax = plt.subplots(1,2)
    ax[0].imshow(plt.imread(selected_input_path))
    mask = np.zeros((500,500))
    for i in masks_path:
        class_of_teeth =i.split('\\')[5]
        print(teeth_class.index(class_of_teeth) + 1 )
        mask_of_teeth = np.array(Image.open(i))
        mask[mask_of_teeth !=0 ] = teeth_class.index(class_of_teeth) + 1
    ax[1].imshow(mask)
    plt.show()
print(X)
