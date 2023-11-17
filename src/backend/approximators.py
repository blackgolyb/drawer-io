from dataclasses import dataclass, field

import numpy as np
from PIL import Image


@dataclass
class Primitive(object):
    color: list[int, int, int]


@dataclass
class Line(Primitive):
    start: list[int, int]
    end: list[int, int]


@dataclass
class Pixel(Primitive):
    x: int
    y: int


@dataclass
class Rect(Primitive):
    start: list[int, int]
    end: list[int, int]


@dataclass
class Ellipse(Primitive):
    start: list[int, int]
    end: list[int, int]


@dataclass
class Polygon(Primitive):
    point1: list[int, int]
    point2: list[int, int]
    point3: list[int, int]


@dataclass
class Figures:
    pixels: list[Pixel] = field(default_factory=list)
    rects: list[Rect] = field(default_factory=list)


class Approximator(object):
    def __init__(self, canvas_size, resample=Image.Resampling.LANCZOS):
        self.canvas_size = canvas_size
        self.resample = resample

    def __call__(self, image: Image) -> list[Primitive]:
        self.rescale_image(image)
        return self.calculate(image)

    def rescale_image(self, image: Image.Image) -> None:
        image.thumbnail(self.canvas_size, self.resample)

    def calculate(self, image: Image) -> list[Primitive]:
        raise NotImplementedError()


class ColorPalateApproximator(Approximator):
    colors = np.array(
        [
            [0, 0, 0],
            [255, 255, 255],
        ]
    )

    def __init__(self, *args, colors=None, patch=1, **kwargs):
        super().__init__(*args, **kwargs)

        self.patch = patch
        if colors is not None:
            self.colors = colors

    def calculate(self, image: Image) -> list[Primitive]:
        data = np.asarray(image).copy()
        colors = self.colors
        shapes = Figures()

        def apply_color(x):
            return colors[np.argmin(np.sum(np.abs(colors - x) ** 2, axis=1))]

        if self.patch == 1:

            def add_shape(figures, i, j, data):
                figures.pixels.append(Pixel(x=j, y=i, color=data))

        else:

            def add_shape(figures, i, j, data):
                figures.rects.append(
                    Rect(start=(j, i), end=(j + self.patch, i + self.patch), color=data)
                )

        for i in range(0, data.shape[0] - self.patch + 1, self.patch):
            for j in range(0, data.shape[1] - self.patch + 1, self.patch):
                add_shape(shapes, i, j, apply_color(data[i][j]))
            print(i)

        return shapes
