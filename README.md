# TensorFlow 2 tutorial

My personal journey through the TensorFlow 2 tutorial

## Installation

You know the drill. First, make a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). Activate the virtual environment, then install the requirements:

```shell script
pip install -U -r requirements.txt
```

## Verify TensorFlow installation

```shell script
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```
