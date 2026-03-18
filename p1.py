print('hello world')


d = {
    (1, 2): "point1",
    (3, 4): "point2"
}

print(d[(3, 4)])


def demo(*args):
    print(sum(args))

demo(1, 23, 42)