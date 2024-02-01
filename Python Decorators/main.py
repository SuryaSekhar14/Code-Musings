### Write to file decorator
# def write_to_file(file_handler):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             file_handler.write(str(result))
#             return result
#         return wrapper
#     return decorator


# handler = open('log.txt', 'w')

# @write_to_file(handler)
# def add(a, b):
#     return a + b



### Timer decorator
# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         print(f"Function took {time.time() - start} seconds to run")
#         return result
#     return wrapper


# @timer
# def add(a, b):
#     return a + b

# add(2, 3)



### Decorator with arguments
# def repeat(num_times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator


# @repeat(3)
# def greet(name):
#     print(f"Hello {name}")


# greet("Surya")



#Logging decorator
# def logger(func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)

#     def wrapper(*args, **kwargs):
#         logging.info(
#             'Ran with args: {}, and kwargs: {}'.format(args, kwargs)
#         )
#         return func(*args, **kwargs)
#     return wrapper


# @logger
# def add(a, b):
#     return a + b


# add(2, 3)



