import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math

from ..utils import decrator_ge

__all__ = [
    "ge_square",
    "ge_circle",
    "ge_right_triangle",
]


# Square

@decrator_ge
def ge_square(width=100, height=None, channels=1, color=None, *arg, **kws):
    """
        @width: int, >0
        @height: int, >0
        @channels: int, >0
        @color: rgb, [0, 255]
        >>> ge_square().shape == (100,100)
        True
        >>> ge_square(50, 100, 3).shape == (100, 50,3)
        True
        >>> ge_square(50, 100, 4).shape == (100, 50, 4)
        True
    """
    res = np.ones((height, width))
    return res


# Circle
@decrator_ge
def ge_circle(width=100, height=None, channels=1, color=None, *arg, **kws):
    X, Y = np.ogrid[:height, :width]
    ch, cw = height // 2, width // 2
    dist = (X - ch) ** 2 + (Y - cw) ** 2
    res = (dist < min(width ** 2 / 4, height ** 2 / 4))

    return res


# rigth_triangle

@decrator_ge
def ge_right_triangle(width=100, height=None, channels=1, color=None, *arg, **kws):
    res = np.tri(width, width)
    if height is not None:
        res = cv2.resize(res, (width, height))
    return res
