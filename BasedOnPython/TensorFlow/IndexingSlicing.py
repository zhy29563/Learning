import tensorflow as tf
# Basic indexing
a = tf.ones([1,5,5,3])
a

a[0]
a[0][0]
a[0][0][0]
a[0][0][0][2]

# Numpy-style indexing
a = tf.random.normal([4,28,28,3])
a

a[1].shape
a[1,2].shape
a[1,2,3].shape
a[1,2,3,2].shape
## start:end
a = tf.range(10)
a
a[-1:]
a[-2:]
a[:2]
a[:-1]
## Indexing by :
a = tf.random.normal([4,28,28,3])
a.shape
a[0].shape
a[0,:,:,:].shape
a[0,1,:,:].shape
a[:,:,:,0].shape
a[:,:,:,2].shape
a[:,0,:,:].shape
## Indexing by ::
a.shape
a[0:2,:,:,:].shape
a[:,0:28:2,0:28:2,:].shape
a[:,:14,:14,:].shape
a[:,14:,14:,:].shape
a[:,::2,::2,:].shape
## ::-1
a = tf.range(4)
a
a[::-1]
a[::-2]
a[2::-2]
## ...
a = tf.random.normal([2,4,28,28,3])
a[0].shape
a[0,:,:,:,:].shape
a[0,...].shape
a[:,:,:,:,0].shape
a[...,0].shape
a[...,0].shape
a[0,:,:,:,2].shape
a[1,0,:,:,0].shape
# tf.gather

#tf.gather(params,indices,axis=0 )
#从params的axis维根据indices的参数值获取切片

a = tf.random.normal([4,35,8])
a.shape
tf.gather(a, axis = 0, indices=[2,3]).shape
a[2:4].shape

tf.gather(a, axis = 0, indices=[2,0,3]).shape

tf.gather(a, axis = 1, indices = [2,3,7,9,16]).shape
tf.gather(a,axis = 2, indices = [2,3,7]).shape

'''
# tf.gather_nd

tf.gather_nd(params, indices, batch_dims=0, name=None)

Gather slices from params into a Tensor with shape specified by indices

indices is an K-dimensional integer tensor, best thought of as a (K-1)-dimensional tensor of indices into params, where each element defines a slice of params:
'''

a = tf.random.normal([4,35,8])
a.shape
tf.gather_nd(a, [0]).shape
tf.gather_nd(a, [0,1]).shape
tf.gather_nd(a, [0,1,2]).shape
tf.gather_nd(a, [[0,1,2]]).shape

tf.gather_nd(a, [[0,0],[1,1]]).shape

tf.gather_nd(a, [[0,0],[1,1],[2,2]]).shape
tf.gather_nd(a, [[0,0,0],[1,1,1],[2,2,2]]).shape
tf.gather_nd(a, [[[0,0,0],[1,1,1],[2,2,2]]]).shape
# tf.boolean_mask
a = tf.random.normal([5,4,3,2])
a = tf.random.normal([5,4,3,2])
tf.boolean_mask(a, mask=[True,True,True,False,False]).shape
tf.boolean_mask(a, mask=[True,True,True,False,False],axis = 0).shape
tf.boolean_mask(a, mask=[True,False] ,axis = 3).shape
a = tf.ones([2,3,4])
tf.boolean_mask(a, mask=[[True,False,False],[False,True,True]]).shape