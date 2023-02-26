from datetime import datetime


def time_stamping_machine(own_function):
    def internal_wrapper(*args, **kwargs):
        timestamp = datetime.now()
        string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        print()
        print(string_timestamp)
        return own_function(*args, **kwargs)
    return internal_wrapper


@time_stamping_machine
def simple_hello():
    print("Hello from simple function!")


@time_stamping_machine
def add_two_objects(n1, n2):
    return n1 + n2


@time_stamping_machine
def multiply_two_objects(n1, n2):
    return n1 * n2


simple_hello()
print('Result:', add_two_objects('Hello', 'Python'))
print('Result:', add_two_objects(100, 88))
print('Result:', multiply_two_objects(100, 88))

# outputs...
# 2021-07-26 22:58:54
# Hello from simple function!
#
# 2021-07-26 22:58:54
# Result: HelloPython
#
# 2021-07-26 22:58:54
# Result: 188
#
# 2021-07-26 22:58:54
# Result: 8800
