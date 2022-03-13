# 1)

# 2)

prev = None   # to remember the previous output
func = None   # to remember the previous function


def lastcall(f):
    def wrap(*args, **kwargs):
        global prev
        global func
        res = f(*args, **kwargs)
        if prev is res and prev is not None and func is f:
            print(f"I already told you the answer is {prev}")
        prev = res
        func = f
        return res

    return wrap


@lastcall
def f(x):
    return x ** 2


@lastcall
def g(x):
    return x


f(2)
f(2)   # prints message
f(3)
f(3)  # prints message
f(3)  # prints message
g(9)  # doesnt prints message
g(9)  # prints message
g('9')# doesnt prints message
g('9')# prints message
f(3)  # doesnt prints message


# 3)

class List(list):

    def __getitem__(self, *args):  # overwrite the index operator
        if type(*args) is type(()):
            l = list(*args)
        else:
            l = list(args)         # if given only one parameter it doesnt treat it as tuple
        res = super().__getitem__(l[0])    # get the first element
        first = True
        for i in l:               # for every element in the list
            if first:             # try to get the i element of the current list
                first = False
            else:
                res = res[i]      # the current element
        return res


l = List([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])

print(l[1,0,2])    # prints 12
print(l[0,0])      # prints [4,5,6]
print(l[1])        # prints [[1, 2, 3], [4, 5, 6]]
l.append(13)       # can still use the original list methods
print(l[2])        # prints 13

# 4)
# https://www.codingame.com/training/medium/death-first-search-episode-1
