from PIL import Image


class ImgNode(Image.Image):

    def __init__(self, left=None, right=None, op=None):
        self.left = left
        self.right = right
        self.op = op

    def __call__(self):

        if self.left is None and self.right is None:
            return None
        left = right = None
        if isinstance(self.left, Image.Image):
            left = self.left


        if self.left is None and self.right is None:
            return None
        left = None if self.left is None else self.left()
        right = None if self.right is None else self.right()

        return self.op(left, right)





if __name__ == '__main__':
    node = ImgNode()
