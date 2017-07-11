
### Jupyter

```sh
git clone https://github.com/
cd *
jupyter notebook --ip 0.0.0.0
```

Jupyter would return you a url like
```
http://0.0.0.0:8888/?token=70f9d9457fec7045f5f991ad9d896060122b13d60cafbbc0
```
Replace the `0.0.0.0` with the ip of your server and the port `8888` with `240**`.

Then copy/paste this URL into your browser.

If you are not familar with Jupyter notebook, see [Jupyter notebook basics]( http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Notebook%20Basics.html).

### What are these files ?

##### Jupyter notebook files
```
Problem.ipynb: build and train your model in this notebook.
Demo.ipynb: a demo of this framework in which a MLP is built with builtin FCLayer, ReLULayer.
```

##### Python files
```
layers/
    - fc_layer.py: implement the forward and backward of fully connected layer in this file.
    - sigmoid_layer.py: implement the forward and backward of ReLU layer in this file.
    - relu_layer.py: implement the forward and backward of Sigmoid layer in this file.
    - __init__.py: mark layers/ as Python package directory.
criterion/
    - softmax_cross_entropy.py: the softmax cross entropy criterion.
    - __init__.py: mark layers/ as Python package directory.
builtin/
    - Some pyc files that can be executed.
MNIST_data/
    - the directory in which MNIST dataset is stored.
network.py: the class network is defined here.
optimizer.py: the SGD is defined here and you need to implement the SGD with momentum in this file.
solver.py: the train and test function is defined here.
```

