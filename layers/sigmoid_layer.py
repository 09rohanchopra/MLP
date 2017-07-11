
import numpy as np


class SigmoidLayer:
    def __init__(self):
        """Applies the element-wise function :math:`f(x) = 1 / ( 1 + exp(-x))`
        Shape:
             Input: :math:`(N, num_input)`
             Output: :math:`(N, num_input)`
        """
        self.trainable = False

    def forward(self, Input):
        # TODO: Put your code here
        # Please delete `pass` and return the output
        pass

    def backward(self, delta):
        # TODO: Put your code here
        # Please delete `pass`, calculate and return delta
        pass
