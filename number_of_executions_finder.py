import numpy as np
import timeit
import copy
# import python script with defined algorithm if not using builtin or numpy
# sorting algorithm

sorting_algorithm = sorted # Choose sorting_algorith to test
number_of_elements = 1000  # Number of elements
max_time = 1               # Max time you want to let the computation take

# Modified timeit.clock.autorange to find the number required for the
# computation to take atleast time sec.


def autoranger(timer_object, max_time, callback=None):
    """Return the number of loops and time taken so that total time >= 1.

    Calls the timeit method with increasing numbers from the sequence
    1, 2, 5, 10, 20, 50, ... until the time taken is at least time
    second.  Returns (number, time_taken).

    If *callback* is given and is not None, it will be called after
    each trial with two arguments: ``callback(number, time_taken)``.
    """
    i = 1
    while True:
        for j in 1, 2, 5:
            number = i * j
            time_taken = timer_object.timeit(number)
            if callback:
                callback(number, time_taken)
            if time_taken >= max_time:
                return (number, time_taken)
        i *= 10


np.random.seed(1337)
test_data = np.random.random((number_of_elements,))
clock = timeit.Timer(stmt='sort_func(copy(data))',
                     globals={'sort_func': sorting_algorithm,
                              'data': test_data,
                              'copy': copy.copy})
n_ar, t_ar = autoranger(clock, max_time, print)
t = clock.repeat(repeat=7, number=n_ar)
