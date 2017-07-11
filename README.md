### Connect to the server via ssh

Given the account information as below,

| Id | Name | Username | Password | IP             | Port-22 | Port-6006 | Port-8888 |
|----|------|----------|----------|----------------|---------|-----------|-----------|
| 0  | Alice    | alice     | password | 166.111.69.245 | 22000   | 23000     | 24000     |

ssh to the server with
```sh
ssh -p 22000 alice@166.111.69.245
```

For Mac / Linux, you can use terminal.
For Windows, you can use [MobaXterm](http://mobaxterm.mobatek.net/download.html)


### Jupyter

Jupyter notebook is recommented to used in this homework.

If you are not familar with Jupyter notebook, see [Jupyter notebook basics]( http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Notebook%20Basics.html).

Run the jupyter notebook on the server,

```sh
git clone https://github.com/wujian752/MLP
cd MLP
jupyter notebook --ip 0.0.0.0
```

Jupyter would return you a url like
```
http://0.0.0.0:8888/?token=70f9d9457fec7045f5f991ad9d896060122b13d60cafbbc0
```
Replace the `0.0.0.0` with ｀166.111.69.245｀ and the port `8888` with `24000`.

Then copy/paste this URL into your browser.


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
    - __init__.py: mark criterion/ as Python package directory.

builtin/
    - Some pyc files that can be executed.

MNIST_data/
    - the directory in which MNIST dataset is stored.

network.py: the class network is defined here.

optimizer.py: the SGD is defined here and you need to implement the SGD with momentum in this file.

solver.py: the train and test function is defined here.
```

You can train a MLP in the `Demo.ipynb` with the builtin layers.

And after you implement your FCLayer, SigmoidLayer and ReLULayer in `layers`, you can set `use_builtin` to `False` to test your implementation.

Then, build and train the SigmoidMLP and ReLUMLP in `Problem.ipynb` and compare their difference.

Finally, implement `SGDwithMomentum` in `optimizer.py` and train ReLUMLP with `SGDwithMomentum` in `Problem.ipynb`.


