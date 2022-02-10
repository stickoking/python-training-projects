from colorgram import extract

def generate_colors(image):
    color_list = []
    colors = extract(image, 256)
    for i in range(len(colors)):
        r = colors[i].rgb.r
        g = colors[i].rgb.g
        b = colors[i].rgb.b
        color_list += [(r, g, b)]
    return color_list
