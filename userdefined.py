#split() function user defined program
s = 'hello'
s1 = 'fan'
#print(s.split('e'))
def split():
    a = input("Enter delimiter:")
    for i in s:
        if(i == a):
            print(f"['{s}']")
split()