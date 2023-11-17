import time
from PIL import Image
import numpy as np


from src.backend.approximators import ColorPalateApproximator
from src.drawers.gatic_phone import Drawer, Canvas


def main():
    canvas_size = (940, 519)
    canvas_padding = (489+20, 337+20)
    
    image = Image.open("./test.jpg")
    colors = np.array([
        [0, 0, 0],
        [102, 102, 102],
        [0, 80, 205],
        
        [255, 255, 255],
        [170, 170, 170],
        [38, 201, 255],
        
        [1, 116, 32],
        [153, 0, 0],
        [150, 65, 18],
        
        [17, 176, 60],
        [255, 0, 19],
        [255, 120, 41],
        
        [176, 112, 28],
        [153, 0, 78],
        [203, 90, 87],
        
        [255, 193, 38],
        [255, 0, 143],
        [254, 175, 168],
    ])
    a = ColorPalateApproximator((800, 800), colors=colors, patch=10)
    # a = ColorPalateApproximator(canvas_size, colors=colors)
    shapes = a(image)
    # print(shapes)
    d = Drawer(Canvas(canvas_size, canvas_padding))
    
    time.sleep(5)
    d.draw(shapes)
    
if __name__ == "__main__":
    main()