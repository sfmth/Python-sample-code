import sys, math, random, threading, time
from functools import reduce
from typing import List


def main():
    classes()


def first():
    print('Hello World')
    name = input("what's your name")
    print('hi', name)
    v1 = (
        1 + 2
        + 3
    )
    v1 = 1 + 2\
        + 3
    v1 = v1 + 2


def second():
    n = 'hello'
    print(type(n))
    print(sys.maxsize)
    print(sys.float_info.max)
    a = 922337203685477580733
    print(str(a))
    b = 1.7976931348623157e+309
    print(str(b))
    complex1 = 5 + 6j
    print(str(complex1))
    print("Escape Sequences: \' \" \\ \t t \n g")
    print('''triple quote easy " ' ' " '' ''')
    print(str(ord('d')))
    print(str(chr(94)))
    print(12, 21, 1974, sep='/')
    print('no new line', end='')
    print("\n%04d %s %.2f %c" % (1, 'derek', 1.234, 'a'))
    print(5**3)
    a = 20.4
    b = 3.456
    print(abs(a))
    print(round(a))
    print(math.sin(a))
    math.hypot(a, b)  #lenght of vector
    math.radians(60)
    math.degrees(math.pi)
    random.randint(1, 10)
    print(math.inf)
    print(math.inf/math.inf)
    print(1/math.inf)


def third():
    print(r"i'll be ignored")
    str1 = "i'm a string"
    print(str1[0:4])
    print(str1[0:-1:2])
    str1 = str1.replace("i'm", "you're")
    print(str1)
    str1 = str1[:8] + " bad " + str1[9:]
    print(str1)
    print("you" not in str1)
    str2 = "     dhhh       "
    str2 = str2.strip()
    print(str1.find("u"))
    print(str2)
    print(" ".join(["some", "words"]))
    print("my good string".split(" "))
    int1 = 7
    int2 = 7
    print(f'{int1} + {int2} = {int1 + int2}')
    print("string".isalnum())
    str1.isalpha()
    str1.isdigit()


def lists():
    list1 = [1, 2, 3, 4, 5, 6]
    list1[0] = 2
    lstr = "my good string is rocking".split(" ")
    print(str(lstr[0:-1]))
    for i in range(len(lstr)):
        print(lstr[i] + " ", end="")
    tensor = [[1, 2, 3], [1, 2, 3]]


def loops():
    l1: list[int] = [1, 34, 3, 4, 5, 6, 7, 7]

    while len(l1):
        print(l1.pop(0))

    for x in range(0, 10):
        print(x, ' ', end="")
    print()
    itr = iter([32, 32, 23])
    for i in range(3):
        v = next(itr)
        print(v)
    l2 = list(range(0, 11))
    tuples()


def tuples():
    t1 = (1, 3, 4, 5)
    print(len(t1))
    print(t1[0:2])
    print(t1[::-1])
    dictionaries()


def dictionaries():
    heroes = {
        "super": "cld",
        "bat": "asd"
    }
    len(heroes)
    print(heroes["super"])
    print(list(heroes.items()))
    print(list(heroes.keys()))
    print(list(heroes.values()))
    sets()


def sets():
    '''
    sets are good for finding a thing in the set
    lists are good for iteration
    sets cannot have diplicate values

    '''
    s1 = {1, 2, 3, 4, 5}
    s2 = set(range(0, 11))
    print(s2)
    s3 = s1 | s2
    print(s3)
    s3.add(122)
    #s3.discard()
    s3.pop()
    s3 |= s2
    print(s3)
    s1.intersection(s2)
    s1.symmetric_difference(s2)
    s1.difference(s2)
    s3.clear()
    print(functions())
    print(get_sum(1))
    print(next2(3))
    print(mult(2)(2))
    mapme()


def functions(num1: int = 1, num2 = 1):
    return num1 + num2


def get_sum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


def next2(num):
    return num + 1, num + 2


def mult(num):
    return lambda x: x * num


def mapme():
    nums = range(2, 10)
    #print(list(map(get_sum(), nums)))
    print(sum(range(1, 10)))
    print(list(filter((lambda x: x % 2 == 0), range(1, 11))))
    print(multip(list(range(1, 11))))
    print(reduce((lambda x, y: x * y), range(1, 11)))

    while True:
        break
        try:
            number = int(input("enter num: "))
        except ValueError:
            print("you not number")
            break
        except:
            print("unknoiwn error")
    nextone()


def nextone():
    with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
        my_file.write("random\ntext\nall\nover")

    with open("mydata.txt", encoding="utf-8") as my_file:
        print(my_file.read())
    print("file closed") if my_file.closed else print("error")



def multip(list = [], *args):

    multip = 1

    for item in list:
        if item != 0:
            multip = multip * item
        else:
            multip = 0
            break

    for arg in args:
        if arg != 0:
            multip = multip * arg
        else:
            multip = 0
            break
    return multip


def classes():
    pass



class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width
    @property
    def height(selfself):
        prit("retrieving height")
        return self.__height






if __name__ == '__main__':
    main()
