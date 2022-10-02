from math import inf
import numpy as np

colors = {
    'red': np.array([255, 0, 0]),
    'green': np.array([0, 255, 0]),
    'blue': np.array([0, 0, 255]),
    'black': np.array([0, 0, 0]),
    'white': np.array([255, 255, 255]),
    'yellow': np.array([255, 255, 0]),
    'cyan': np.array([0, 255, 255]),
    'magenta': np.array([255, 0, 255]),
    # # 'gray': np.array([128, 128, 128]),
    # 'dark-green': np.array([0, 100, 0]),
    # # 'pale-green': np.array([152, 251, 152]),
    # 'purple': np.array([128, 0, 128]),
    # 'dark-blue': np.array([0, 0, 128]),
    'orange': np.array([255, 140, 0]),
    # # 'bright-orange': np.array([255, 69, 0]),
    # # 'indigo': np.array([75, 0, 130]),
    # # 'hot-pink': np.array([255, 105, 180]),
    # 'deep-pink': np.array([255, 20, 147]),
    # 'brown': np.array([139, 69, 19]),
    # # 'pale-violet-red': np.array([219, 112, 147])
}


def get_color(img):
    height = img.shape[0]
    width = img.shape[1]

    colors_in_img = []
    X = [round(width - 0.20*width), round(width - 0.50*width), round(width - 0.80*width)]
    Y = [round(height - 0.20*height), round(height - 0.50*height), round(height - 0.80*height)]

    for y in Y:
        for x in X:
            colors_in_img.append(img[y][x])

    return colors_in_img
    
def get_color_name(img):
    colors_in_img = get_color(img)
    basic_colors_in_img = []

    for color in colors_in_img:
        b, g, r = color
        color_vect = np.array([r, g, b])
        min_val = inf
        min_color = None

        for c in colors:
            difference = color_vect - colors[c]
            mag = np.linalg.norm(difference) 
            if mag < min_val:
                min_val = mag
                min_color = c
        
        basic_colors_in_img.append(min_color)
    
    return max(set(basic_colors_in_img), key=basic_colors_in_img.count)
