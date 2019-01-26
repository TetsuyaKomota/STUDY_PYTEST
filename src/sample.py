# coding=utf-8

def func(a):
    return func(a-1)*a if a > 0 else 1

if __name__=="__main__":
    print(func(10))
