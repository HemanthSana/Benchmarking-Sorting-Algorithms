import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


time_list = [] # Create list that will hold time for benchmarks
std_list = [] # Create list that will hold std of time for benchmarks
number_of_elements = [] # Create list with the number of elements for each benchmark
limit = 28
for i in range(7, limit, 3):
    number_of_elements.append(2**i)

name = "python_sorted" # name of algorithm
name_element_ordering = "BestCase" # best/worst/average
n_ar = 5000 # number of executions
#number_of_elements = 8192


for i in number_of_elements:
    times = pd.read_pickle("./benchmarks/"+name+"-"+name_element_ordering+"-"+
            str(i)+"-"+str(n_ar)+".pkl")
    times_array = times.values
    time = np.mean(times_array)
    std = np.std(times_array)
    time_list.append(time)
    std_list.append(std)

plt.errorbar(number_of_elements, time_list, std_list)
plt.xscale("log", basex=2)
plt.yscale("log", basey=10)
plt.title(name+"-"+name_element_ordering+"-"+str(n_ar))
plt.show()


