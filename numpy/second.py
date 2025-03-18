import numpy as np

a = np.array([1, 2, 3], 'float64')
# array([1., 2., 3.], dtype=float64)

np.sctypeDict # types
# {'?': <class 'numpy.bool_'>,
#  'b': <class 'numpy.int8'>,
#  'B': <class 'numpy.uint8'>,
#  'h': <class 'numpy.int16'>,}

b = np.array([1, 2, 3], 'str_')

np.complrx64(10)

np.int16(10.5)

a = np.array([1,2, 5000, 1000], dtype='int8')
# array([  1,   2, 127, -128], dtype=int8) данные исказились 
b = np.complex64(a)
# array([  1.+0.j,   2.+0.j, 127.+0.j, -128.+0.j], dtype=complex64)
c = np.int32(b)
# array([  1,   2, 127, -128], dtype=int32)


#-------------------------------------------------------------
# array №2
# ---------------------------------------------------------------
np.array( (1,2,3) )
# array([1, 2, 3])

np.array( 'Hello')
# array(['Hello'], dtype='<U5')

a = np.array ( [[1,2], [3,4]] )
# array([[1, 2],
#        [3, 4]])

a = np.array( [[[1,2], [3,4]], [[5,6], [7,8]]] )
# array([[[1, 2],
#         [3, 4]],

#        [[5, 6],
#         [7, 8]]])


# -----------------------------------------------------
# автозаполнение , создание матриц   №3
# -----------------------------------------------------
np.array( [0]*10)
# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
np.ones((3,4))
# array([[1., 1., 1., 1.],
#        [1., 1., 1., 1.],
#        [1., 1., 1., 1.]])

np.zeros((3,4))
# array([[0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.]])

np.empty((3,4))
# array([[0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.]])

np.identity(3)
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])

np.eye(3, k=1)
# array([[0., 1., 0.],
#        [0., 0., 1.],
#        [0., 0., 0.]])

np.full((3,4), 10)
# array([[10, 10, 10, 10],
#        [10, 10, 10, 10],
#        [10, 10, 10, 10]])

#-----------------------------------------------------
#matrix
np.mat('1, 2, 3, 4')
# matrix([[1, 2, 3, 4]])

np.mat('1 2; 3 4')
# matrix([[1, 2],
#         [3, 4]])

np.mat([[1, 2], [3, 4]])
# matrix([[1, 2],
#         [3, 4]])

np.mat([1, 2, 3, 4])
# matrix([[1, 2, 3, 4]])


#-----------------------------------------------------
#
np.diag([1, 2, 3, 4])
# array([[1, 0, 0, 0],
#        [0, 2, 0, 0],
#        [0, 0, 3, 0],
#        [0, 0, 0, 4]])

np.diag([1, 2, 3, 4], k=1)
# array([[0, 1, 0, 0],
#        [0, 0, 2, 0],
#        [0, 0, 0, 3],
#        [0, 0, 0, 0]])

np.diag([1, 2, 3, 4], k=-1)
# array([[0, 0, 0, 0],
#        [1, 0, 0, 0],
#        [0, 2, 0, 0],
#        [0, 0, 3, 0]])

np.diag([(1,2,3), (4,5,6), (7,8,9)])
# array([1, 5, 9])

np.diagflat([(1,2,3), (4,5,6), (7,8,9)])
# array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 5, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 9, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 3, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 6, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 7, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 8, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 9, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 1]])

#-----------------------------------------------------
#tri
np.tri(4)
# array([[1., 0., 0., 0.],
#        [1., 1., 0., 0.],
#        [1., 1., 1., 0.],
#        [1., 1., 1., 1.]])

np.tri(4, 2)
# array([[1., 0.],
#        [1., 1.],
#        [1., 1.],
#        [1., 1.]])

a = np.array( [(1,2,3), (4,5,6), (7,8,9)] )
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
np.tril(a)
# array([[1, 0, 0],
#        [4, 5, 0],
#        [7, 8, 9]])

np.triu(a)
# array([[1, 2, 3],
#        [0, 5, 6],
#        [0, 0, 9]])

#-----------------------------------------------------
# vander

np.vander([1, 2, 3])
# array([[1, 1, 1],
#        [8, 4, 2],
#        [27, 9, 3]])

np.vander([1, 2, 3], 5)
# array([[  1,   1,   1,   1,   1],
#        [  8,   4,   2,   1,   0],
#        [ 27,   9,   3,   0,   0]])

np.vander([1, 2, 3], 5, increasing=True)
# array([[  1,   1,   1,   1,   1],
#        [  0,   8,   4,   2,   1],   
#        [  0,   0,  27,   9,   3]]) 


#-----------------------------------------------------
# arange

np.arange(10)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

np.arange(1, 10)
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])

np.arange(1, 10, 2)
# array([1, 3, 5, 7, 9])

np.arange(10, 1, -2.5)
# array([10,  7.5,  5,  2.5])

np.cos(np.arange(0, np.pi, 0.1))
# array([ 1.00000000e+00,  9.99999998e-01,  9.99999994e-01,  9.99999988e-01,
#         9.99999980e-01,  9.99999969e-01,  9.99999955e-01,  9.99999937e-01,
#         9.99999912e-01,  9.99999883e-01,  9.99999849e-01,  9.99999811e-01,


#-----------------------------------------------------
# linspace

np.linspace(2.0, 3.0, num=5)
# array([2.  , 2.25, 2.5 , 2.75, 3.  ])

np.linspace(2.0, 3.0, num=5, endpoint=False)
# array([2. , 2.2, 2.4, 2.6, 2.8])


#-----------------------------------------------------
# logspace

np.logspace(2.0, 3.0, num=4)
# array([ 100.        ,  215.443469  ,  464.15888336, 1000.        ])

np.logspace(2.0, 3.0, num=4, base=2.0)
# array([ 4.        ,  5.0396842 ,  6.34960421,  8.        ])

np.logspace(2.0, 3.0, num=4, endpoint=False)
# array([ 100.        ,  215.443469  ,  464.15888336,  1000.        ])

np.logspace(2.0, 3.0, num=4, base=2.0, endpoint=False)
# array([ 4.        ,  5.0396842 ,  6.34960421,  8.        ])


#-----------------------------------------------------
# geomspace

np.geomspace(1, 1000, num=10)
# array([    1.        ,     2.        ,     4.        ,     8.        ,
#         16.        ,    32.        ,    64.        ,   128.        ,
#        256.        ,   512.        ])


#-----------------------------------------------------
# meshgrid

x, y = np.meshgrid([1, 2, 3], [4, 5, 6])
x
# array([[1, 2, 3],
#        [1, 2, 3],
#        [1, 2, 3]])

y
# array([[4, 4, 4],
#        [5, 5, 5],
#        [6, 6, 6]])


#-----------------------------------------------------
b = np.copy(a)
# это копия не ссылка


#-----------------------------------------------------
# fromfunction

np.fromfunction(lambda i, j: i == j, (3, 3))
# array([[ True, False, False],
#        [False,  True, False],
#        [False, False,  True]])


#-----------------------------------------------------
# fromiter

np.fromite("hello", dtype='U1')
# array(['h', 'e', 'l', 'l', 'o'], dtype='<U1')

np.fromiter(lambda x: x*x, dtype=int, count=5)
# array([0, 1, 4, 9, 16])

np.fromstring("1,2", dtype=int, sep=",")
# array([1, 2])

