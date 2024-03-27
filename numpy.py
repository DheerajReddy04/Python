'''
import numpy as np
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[1,2],[3,4]])
print(np.dot(arr1,arr2))
#Output: [[ 7 10]
         [15 22]]
'''


'''
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[6,7,8,9,10]
plt.plot(x,y)
plt.xlabel('Giri Swami')
plt.ylabel('Y axis')
plt.show()
#Output: Graph
'''


'''
from tkinter import *
root = Tk()
label = Label(root, text = "Hello")
textbox = Entry(root)
button = Button(root, text="Button")
button.pack(side=BOTTOM)
canvas= Canvas(root,bg="yellow")
b2=Button(root,text="On top of canvas")
#b2.pack()
canvas.pack(side=LEFT)
textbox.pack(side=RIGHT)
label.pack(side=TOP)
root.mainloop()
'''
