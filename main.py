import time

from PIL import Image

from src.backend.approximators import ColorPalateApproximator
from src.drawers.gatic_phone import Canvas, Drawer, color_pallet


def main():
    canvas_size = (940, 519)
    canvas_padding = (489 + 20, 337 + 20)

    image = Image.open("./test.jpg")

    a = ColorPalateApproximator((800, 800), colors=color_pallet, patch=10)
    shapes = a(image)
    drawer = Drawer(Canvas(canvas_size, canvas_padding))

    time.sleep(5)
    drawer.draw(shapes)


if __name__ == "__main__":
    main()
