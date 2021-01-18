'''
Data Container
- list
- np.ndarray
- tf.Tensor

# What's Tensor

- scalar:1.1
- vector:[1.1],[1.1,2.2,...]
- matrix:[[1.1,2,2],[3.3,4.4],[5.5,6.6]]
- tensor:rank > 2

# TF is a computing lib

- int, float, double
- bool
- string


'''
import tensorflow as tf

# Create
tf.constant(1)
tf.constant(1.)
tf.constant(2.2, dtype=tf.int32)
tf.constant(2., dtype=tf.double)

tf.constant([True, False])
tf.constant("hello, world.")

with tf.device('cpu'):
    a_cpu = tf.constant([1])
with tf.device('gpu'):
    a_gpu = tf.constant([1])

print (a_cpu)
print (a_gpu)

print (a_cpu.device)
print (a_gpu.device)

# CPU数据与GPU数据转换
a_cpu_togpu = a_cpu.gpu()
a_cpu_togpu.device

a_gpu_tocpu = a_gpu.cpu()
a_gpu_tocpu

#与Numpy数据的转换
a_cpu.numpy()
a_cpu.ndim
tf.rank(a_cpu)
tf.rank(tf.ones([3,4,2]))
a_cpu.ndim

# Check Tensor Type
a = tf.constant([1.])
a

b = tf.constant([True, False])
b

c = tf.constant('hello world.')
c

import numpy as np
d = np.arange(4)
d

isinstance(a, tf.Tensor)
tf.is_tensor(d)
a.dtype, b.dtype, c.dtype
a.dtype == tf.float32
c.dtype == tf.string

# Convert
a = np.arange(5)
a

a.dtype

aa = tf.convert_to_tensor(a)
aa

aa = tf.convert_to_tensor(a, dtype=tf.int64)
aa

tf.cast(aa, dtype=tf.float32)
aaa = tf.cast(aa, dtype=tf.double)
aaa

tf.cast(aaa, dtype=tf.int32)

# bool & int
b = tf.constant([0,1])
b

bb = tf.cast(b, dtype=tf.bool)
bb

tf.cast(bb, tf.int32)
# tf.Variable
a = tf.range(5)
a

b = tf.Variable(a)
b

b.dtype
b.name

b = tf.Variable(a, name='input_data')
b

b.name
b.trainable
isinstance(b, tf.Tensor)
isinstance(b, tf.Variable)

tf.is_tensor(b)
b.numpy()

# To numpy
a.numpy()
b.numpy()
a = tf.ones([])
a
a.numpy()
int(a)
float(a)
# From Numpy, List
tf.convert_to_tensor(np.ones([2,3]))
tf.convert_to_tensor(np.zeros([2,3]))
tf.convert_to_tensor([1,2])
tf.convert_to_tensor([1,2.0])
tf.convert_to_tensor([[1],[2.]])
# tf.zeros
tf.zeros([])
tf.zeros([1])
tf.zeros([2,2])
tf.zeros([2,3,3])
# tf.zeros_like
a = tf.zeros([2,3,3])
a

tf.zeros_like(a)
tf.zeros(a.shape)
# tf.ones
tf.ones(1)
tf.ones([])
tf.ones([2])
tf.ones([2,3])
tf.ones_like(a)
# Fill
tf.fill([2,2], 0)
tf.fill([2,2], 0.)
tf.fill([2,2], 1)
tf.fill([2,2], 9)
# Normal
tf.random.normal([2,2], mean = 1, stddev = 1)
tf.random.normal([2,2])
tf.random.truncated_normal([2,2], mean = 0, stddev = 1)
# Uniform
tf.random.uniform([2,2], minval = 0, maxval = 1)
tf.random.uniform([2,2], minval = 0, maxval = 100)
# Random Permutation
idx = tf.range(10)
idx
idx = tf.random.shuffle(idx)
idx
a = tf.random.normal([10,784])
b = tf.random.uniform([10], maxval = 10, dtype = tf.int32)
b
a = tf.gather(a,idx)
a
b = tf.gather(b, idx)
b

# tf.constant
tf.constant(1)
tf.constant([1])
tf.constant([1,2.])
tf.constant([[1,2.],[3.]])

# Loss
out = tf.random.uniform([4, 10])
out

y = tf.range(4)
y = tf.one_hot(y, depth = 10)
y

loss = tf.keras.losses.mse(y, out)
loss

loss = tf.reduce_mean(loss)
loss

# Vector
net = tf.layer.Dense(10)
net.build((4,8))

net.kernel
net.bias

# Matrix
x = tf.random.normal([4, 784])
x

net = layers.Dense(10)
net.build((4,784))

net(x).shape()
net.kernel.shape
net.bias.shape

# Dim = 3 Tensor
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.imdb.load_data(num_words = 10000)
x_train = tf.keras.preprocessing.sequence.pad_sequences(X_train, maxlen = 80)
x_train.shape
emb = embedding(x_train)
emb.shape
out = rnn(emb[:4])
out.shape
# Dim = 4 Tensor
x = tf.random.normal((4,32,32,3))
net = layers.Conv2D(16, kernel_size = 3)
net(x)