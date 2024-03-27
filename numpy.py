#Packages have to be downloaded. Instead use Google Collab 

#adding two arrays
'''
import numpy as np
a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
print(a+b)
#output: [2 4 6 8]
'''
#Type and shape
'''
import numpy as np
a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
c = a+b
type(c)
c.shape
#output: numpy.ndarray
#        (4,)
'''
#List to array and its type
'''
import numpy as np
l = [[1, 2, 3], [3, 6, 9], [2, 4, 6]] # create a list
a = np.array(l) # convert a list to an array
print(a)
print(a.dtype)
#output:[[1 2 3]
#       [3 6 9]
#       [2 4 6]]
#       int64
'''
#Arange, linspace
'''
import numpy as np
x = np.arange(0,10,2)
y = np.linspace(0,10,20)
print(x, y, sep="\n")
#output: [0 2 4 6 8]
#       [ 0.          0.52631579  1.05263158  1.57894737  2.10526316  2.63157895
#         3.15789474  3.68421053  4.21052632  4.73684211  5.26315789  5.78947368
#         6.31578947  6.84210526  7.36842105  7.89473684  8.42105263  8.94736842
#         9.47368421 10.   
'''