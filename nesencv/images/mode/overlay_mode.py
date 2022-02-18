import os
from typing import Union, Tuple

from PIL import Image


class OverlayMode(object):
    """
    call: None, Image.Image
    """

    def __init__(self):
        pass

    def __call__(self, left, right):
        pass


class ModePaste(OverlayMode):
    def __init__(self, box: Union[Tuple[float, float], Tuple[int, int, int, int], None]):
        super(ModePaste, self).__init__()
        self.box = box
        pass

    def __call__(self, left, right):
        if left is None and right is None:
            return None

        if left is None:
            left = Image.new("RGB", right.size)
        else:
            left = left.copy()
        left.paste(right, self.box)
        return left
