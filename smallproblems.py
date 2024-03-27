#FIbonacci or not
'''
import math
def is_perfect_square(n):
	root = int(math.sqrt(n))
	return (root * root == n)

def is_fibonacci(n):
	if n == 0:
		return True
	a, b, c = 0, 1, 1
	while c < n:
		a = b
		b = c
		c = a + b
	return c == n or is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

for i in range(1, 11):
	if is_fibonacci(i):
		print(i, "is a Fibonacci number.")
	else:
		print(i, "is not a Fibonacci number.")
'''

#pascals triangle
'''
# Print Pascal's Triangle in Python
from math import factorial

# input n
n = 5
for i in range(n):
	for j in range(n-i+1):

		# for left spacing
		print(end=" ")

	for j in range(i+1):

		# nCr = n!/((n-r)!*r!)
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	# for new line
	print()

'''

from tkinter import *

top = Tk()
top.geometry("400x250")

name_label = Label(top, text="Name")
name_label.place(x=30, y=50)

email_label = Label(top, text="Email")
email_label.place(x=30, y=90)

password_label = Label(top, text="Password")
password_label.place(x=30, y=130)

sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue")
sbmitbtn.place(x=30, y=170)

e1 = Entry(top)
e1.place(x=80, y=50)

e2 = Entry(top)
e2.place(x=80, y=90)

e3 = Entry(top, show="*")  # Use show="*" to display password as asterisks
e3.place(x=95, y=130)

top.mainloop()
