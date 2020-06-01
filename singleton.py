# Only one object is created after that all instantiation calls return None 
class SingletonClass(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = True
            return super(SingletonClass, cls).__call__(*args, **kwargs)
        return None

class test(metaclass=SingletonClass):
    pass


if __name__ == "__main__":
    singleton1 = test()
    print(singleton1)

    singleton2 = test()
    print(singleton2)
