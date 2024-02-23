from sorting_techniques import pysort
import random
import time

sortObj = pysort.Sorting()

random_list_size = 8
repetitions = 1000
while random_list_size <= 2048:
    merge_time_sum = 0
    insertion_time_sum = 0
    for _ in range(repetitions):
        list_to_sort = [random.random() for _ in range(random_list_size)]
        merge_list = list_to_sort.copy()
        insertion_list = list_to_sort.copy()

        start_time = time.time()
        __ = sortObj.mergeSort(merge_list)
        end_time = time.time()
        merge_time_sum += (end_time - start_time)
        
        start_time = time.time()
        __ = sortObj.insertionSort(insertion_list)
        end_time = time.time()
        insertion_time_sum += (end_time - start_time)
    print("List size {}. Merge sort average time (ms): {}. Insertion sort average time (ms): {}.".format(random_list_size, 1000*merge_time_sum/repetitions,1000*insertion_time_sum/repetitions))
    random_list_size *= 2   