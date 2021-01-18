import tensorflow as tf

a = tf.fill([2,2], 2.)
b = tf.fill([2,2], 5.)

a + b

a - b

a * b

a / b

a // b

b % a

# tf.math.log & tf.exp

a
tf.math.log(a)
tf.exp(a)

# log2, log10?
tf.math.log(8.)/tf.math.log(2.)

tf.math.log(100.)/tf.math.log(10.)

# pow, sqrt
b
tf.pow(b,3)
b ** 3
tf.sqrt(b)
# @ matnul
a, b
a @ b
tf.matmul(a,b)

# With broadcasting
a = tf.ones([4,2,3])
b = tf.ones([3,5])
bb = tf.broadcast_to(b, [4,3,5])
a @ bb

# Recap

## Y = X@W + b
x = tf.ones([4,2])
W = tf.ones([2,1])
b = tf.constant(0.1)

x@W + b
## out = relu(X@W + b)
x@W + b
out = x@W + b
out = tf.nn.relu(out)
out