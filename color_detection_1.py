# import cv2

# img = cv2.imread('mask-2.png')

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

def is_white(r, g, b):
    r, g, b = int(r), int(g), int(b)
    return abs(255 - r) <= 100 and abs(255 - g) <= 100 and abs(255 - b) <= 100

def is_black(r, g, b):
    r, g, b = int(r), int(g), int(b)
    return abs(0 - r) <= 100 and abs(0 - g) <= 100 and abs(0 - b) <= 100 

def is_yellow(r, g, b):
    r, g, b = int(r), int(g), int(b)
    return abs(r - g) <= 100 and abs(r-b) >= 50

def is_cyan(r, g, b):
    r, g, b = int(r), int(g), int(b)
    return abs(g - b) <= 100 and abs(r-b) >= 50

def is_magenta(r, g, b):
    r, g, b = int(r), int(g), int(b)
    return abs(r - b) <= 100 and abs(r-g) >= 50

def is_red(r, g, b):
    r, g, b = int(r), int(g), int(b)
    if [r, g, b].index(max(r, g, b)) == 0:
        return True
    return False

def is_green(r, g, b):
    r, g, b = int(r), int(g), int(b)
    if [r, g, b].index(max(r, g, b)) == 1:
        return True
    return False 

def is_blue(r, g, b):
    r, g, b = int(r), int(g), int(b)
    if [r, g, b].index(max(r, g, b)) == 2:
        return True
    return False 
    
def get_color_name(img):
    colors_in_img = get_color(img)
    basic_colors_in_img = []

    for color in colors_in_img:
        # print(color)
        b, g, r = color
        if is_white(r, g, b):
            basic_colors_in_img.append('white')
        elif is_black(r, g, b):
            basic_colors_in_img.append('black')
        elif is_yellow(r, g, b):
            basic_colors_in_img.append('yellow')
        elif is_cyan(r, g, b):
            basic_colors_in_img.append('cyan')
        elif is_magenta(r, g, b):
            basic_colors_in_img.append('magenta')
        elif is_red(r, g, b):
            basic_colors_in_img.append('red')
        elif is_green(r, g, b):
            basic_colors_in_img.append('green')
        elif is_blue(r, g, b):
            basic_colors_in_img.append('blue')
    
    return max(set(basic_colors_in_img), key=basic_colors_in_img.count)

# print(get_color_name(img))
