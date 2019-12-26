a = 100


def func_a():
    print(a)


def func_b():
    a = 10
    func_a()


func_a()
func_b()
