import tensorflow as tf

x = tf.random.normal([4,32,32,3])
x.shape

y = tf.random.normal([3])
y.shape

(x + y).shape

y = tf.random.normal([32,32,1])
y.shape

(x + y).shape

y = tf.random.normal([4,1,1,1])
y.shape

(x + y).shape

y = tf.random.normal([1,4,1,1])
y.shape

(x + y).shape

x.shape

y = tf.random.normal([4,1,1,1])
y.shape

(x + y).shape

z = tf.broadcast_to(y, list(x.shape))
z.shape

a = tf.ones([3,4])
a1 = tf.broadcast_to(a, [2,3,4])
a1

a2 = tf.expand_dims(a, axis=0)
a2.shape

a3 = tf.tile(a2,[2,1,1])
a3.shape

