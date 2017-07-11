"""fully connected layer"""

import numpy as np


class FCLayer:
    def __init__(self, num_input, num_output, init_std=0.01, trainable=True):
        """Applies a linear transformation to the incoming data: :math:`y = Ax + b`
        Args:
             num_input: size of each input sample
             num_output: size of each output sample
             init_std: std of weight initializer
             trainable: whether if this layer is trainable.
        Shape:
             Input: :math:`(N, num_input)`
             Output: :math:`(N, num_output)`

        Attributes:
             W: the learnable weights of the module of shape
                    (num_output x num_input)
             b:   the learnable bias of the module of shape (num_output, 1)
        """
        self.num_input = num_input
        self.num_output = num_output
        self.trainable = trainable

        self.W = np.random.normal(0, init_std, (num_output, num_input))
        self.b = np.random.normal(0, init_std, (num_output, 1))

        self.diff_W = np.zeros((num_output, num_input))
        self.diff_b = np.zeros((num_output, 1))

    def forward(self, Input):
        # TODO: Put your code here
        # Please delete `pass` and return the output
        pass

    def backward(self, delta):  # delta has been calculated in the last layer
        # TODO: Put your code here
        # Please delete `pass`, calculate delta, self.grad_W, self.grad_b and return delta
        pass
