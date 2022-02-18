import numpy as np
from PIL import Image



def decrator_ge(func):
    def decrator(width=100, height=None, channels=1, color=None, thinkness=None, *arg, **kws):
        thinkness = width // 6 if thinkness is None else thinkness
        kws["thinkness"] = thinkness
        if color == "red":
            color = (255, 0, 0)
        color = (0, 255, 0) if color == "green" else color
        color = (0, 0, 255) if color == "blue" else color
        color = (255, 255, 0) if color == "yellow" else color
        if (color == "random-single") or (color == "random"):
            color = tuple(np.random.randint(0, 255, 3))

        height = width if height is None else height
        channels = len(color) if color and not isinstance(color, str) else channels
        if color is not None:
            if isinstance(color, (tuple, list)):
                channels = len(color)
            elif isinstance(color, np.ndarray):
                color = color.shape[-1]
            elif isinstance(color, str):
                channels = 3
            else:
                assert False

        res = func(width, height, channels, color, *arg, **kws)

        res = np.stack([res] * channels, axis=-1) if channels > 1 else res
        if color is not None:
            if color == "random-random":
                res = np.uint8(res) * np.random.randint(
                    0, 255, (height, width, channels))
            else:
                res = np.uint8(res) * np.uint8(color)
            res = res.astype(np.uint8)

        class A:
            pass

        a = A()
        a.arr = res
        a.pil = lambda: Image.fromarray(res)
        return a

    return decrator
