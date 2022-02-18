




class ImgNode(object):
    def __init__(self, left=None, right=None, op_mode=None):
        self.left = left
        self.right = right
        self.op_mode = op_mode

    def __call__(self):
        if isinstance(self.left, ImgNode):
            left = self.left()
        else:
            left = self.left

        if isinstance(self.right, ImgNode):
            right = self.right()
        else:
            right = self.right

        im = self.op_mode(left, right)

        return im




