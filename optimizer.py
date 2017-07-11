
import numpy as np


class SGD(object):
    def __init__(self, learning_rate, weight_decay):
        self.learning_rate = learning_rate
        self.weight_decay = weight_decay

    def step(self, model):
        layers = model.layer_list
        for layer in layers:
            if layer.trainable:
                # Calculate diff_W and diff_b
                layer.diff_W = - self.learning_rate * (layer.grad_W + self.weight_decay * layer.W)
                layer.diff_b = - self.learning_rate * layer.grad_b

                # weight updating
                layer.W += layer.diff_W
                layer.b += layer.diff_b

                
class SGDwithMomentum(object):
    def __init__(self, learning_rate, weight_decay, momentum):
        self.learning_rate = learning_rate
        self.weight_decay = weight_decay
        self.momentum = momentum

    def step(self, model):
        layers = model.layer_list
        for layer in layers:
            if layer.trainable:
                # TODO: Calculate diff_W and diff_b with momentum


                # weight updating
                layer.W += layer.diff_W
                layer.b += layer.diff_b
        