from codetiming import Timer

# code snippet which using decorators to calculate function execution time
# the code prints Elapsed Time - saying hello: 0.0001265000000000016 secs


@Timer(name='saying hello', text='Elapsed Time - {name}: {} secs')
def say_hello():
    print('Hello World!')


say_hello()
