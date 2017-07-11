"""relu layer"""

import numpy as np


class ReLULayer:
    def __init__(self):
        """Applies the rectified linear unit function element-wise :math:`{ReLU}(x)= max(0, x)`
        Shape:
             Input: :math:`(N, num_input)`
             Output: :math:`(N, num_input)`
        """
        self.trainable = False

    def forward(self, Input):
        # TODO: Put your code here
        # Please delete `pass` and return the output
        self.Input = Input
        self.Output = np.maximum(np.zeros((Input.shape[0],Input.shape[1])),Input)

        return self.Output

    def backward(self, delta):
        # TODO: Put your code here
        # Please delete `pass`, calculate and return delta
        
        return (1* (self.Input>0))* delta