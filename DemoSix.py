# coding : utf-8
'''
    装饰器学习：为已有的对象添加额外的功能
'''

def log_fuc(fuc):
    def wrapper(*args):
        print("log for {fucname}".format(fucname=fuc.__name__))
        return fuc(*args)
    return wrapper

def foo(name,age):
    print("name {name}, age {age}".format(name=name,age=age))

# 因为装饰器返回wrapper,所以这条语句相当于是foo = wrapper
foo = log_fuc(foo)
foo("jj",22) # 相当于执行了wrapper()

# 采用python装饰器
@log_fuc
def foo(name,age):
    print("name {name}, age {age}".format(name=name,age=age))

# 这一句就相当于上面的两句
foo("jj",20)


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

foo()


