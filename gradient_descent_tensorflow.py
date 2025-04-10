import random
import tensorflow as tf
import numpy as np
import keras
TF_USE_LEGACY_KERAS=True
np.random.seed(50)

def init(N):
    X = tf.Variable(np.random.uniform(-N, N), trainable=True)
    Y = tf.Variable(np.random.uniform(-N, N), trainable=True)
    return X, Y

def function(X,Y):
    return (3*X**4+4*X**3-12*X**2+12*Y**2-24*Y)


X,Y = init(N=5)
min = function(X.numpy(), Y.numpy())

for i in range(5):
    optimizer = tf.optimizers.SGD(learning_rate=0.0005, momentum=0.0)
    for epoch in range(1000):
        with tf.GradientTape() as tape:
            loss = function(X, Y)
        grads = tape.gradient(loss, [X, Y])
        optimizer.apply_gradients(zip(grads, [X, Y]))
        print(loss.numpy(), X.numpy(), Y.numpy(), end="\r")
    print(X.numpy(), Y.numpy(), function(X, Y).numpy())
    X, Y = init(N=5)
    