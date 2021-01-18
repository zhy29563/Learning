import tensorflow as tf

a = tf.random.normal([4,28,28,3])
a.shape, a.ndim

tf.reshape(a,[4,784,3]).shape

tf.reshape(a,[4,-1,3]).shape
tf.reshape(a,[4,784*3]).shape
tf.reshape(a,[4,-1]).shape

# Rreshape is flexible
a = tf.random.normal([4,28,28,3])
a.shape
tf.reshape(tf.reshape(a,[4,-1]),[4, 28, 28, 3]).shape

list(tf.reshape(tf.reshape(a,[4,-1]),[4, 28, 28, 3]).shape)

tf.reshape(tf.reshape(a,[4,-1]),[4, 14, 56, 3]).shape

tf.reshape(tf.reshape(a,[4,-1]),[4, 1, 784, 3]).shape

# tf.transpose
a = tf.random.normal((4,3,2,1))
a.shape
tf.transpose(a).shape
tf.transpose(a, perm=[0,1,3,2]).shape

# >>[b,3,h,w]
a = tf.random.normal([4,28,28,3])
a.shape

tf.transpose(a, perm=[0,2,1,3]).shape
tf.transpose(a, perm=[0,3,2,1]).shape
tf.transpose(a, perm=[0,3,1,2]).shape
# Expand Dim
a = tf.random.normal([4,35,8])
a.shape
tf.expand_dims(a,axis=0).shape
tf.expand_dims(a,axis=3).shape
# Axis
a = tf.random.normal([4,35,8])
a.shape

tf.expand_dims(a,axis=0).shape
tf.expand_dims(a,axis=3).shape
tf.expand_dims(a,axis=-4).shape
# Squeeze dim
# Only squeeze for shape = 1 dim

tf.squeeze(tf.zeros([1,2,1,1,3])).shape
a = tf.zeros([1,2,1,3])
a.shape

tf.squeeze(a, axis=0).shape
tf.squeeze(a, axis=2).shape
tf.squeeze(a, axis=-2).shape
tf.squeeze(a, axis=-4).shape

