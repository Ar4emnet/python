from time import time


def decorator(func):
    def point(*args):
        start=time()
        a = func(*args)
        finich=time()
        print("time = ", finich-start)
        return a
    return point 


@decorator
def program (number,optional=None):

    if optional =="odd numbers":
        return [i for i in number if i % 2 != 0]

    elif optional =="even numbers":
        return [i for i in number if i % 2 == 0]

    else:
        res = []
       
        for i in number:
            for x in range(2, i // 2 + 1):
                if i % x == 0:
                    break
            else:
                res += [i]
        return res[1:]

print(program(range(1,40)))