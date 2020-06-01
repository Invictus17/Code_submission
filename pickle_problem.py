# Problem: A class that cannot be pickled
import pickle


def test():
    class Test_class:
        def func(self):
            return 10

    return Test_class()


x = test()
print(pickle.dumps(x))

# classes that are defined at the top level of a module are picklable
# So if we shift the class definition it should work

class Test_class:
    def func(self):
        return 10


def test():
    return Test_class()


x = test()
print(pickle.dumps(x))
