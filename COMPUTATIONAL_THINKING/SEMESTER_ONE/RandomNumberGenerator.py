#Importing Random Engine
import random
import time
import matplotlib.pyplot as plt

MAX_RANGE = 999999#max range of the list elements
MIN_RANGE = 100000#min range of the list elements
#three different sizes for three different list arrays
LIST_SIZE_SET_1 = 100
LIST_SIZE_SET_2 = 1000
LIST_SIZE_SET_3 = 10000

camparison_count = {'selection_sort':0,'merge_sort':0,'quick_sort':0,}
#defining the random number generator function for reusablity
def random_num_generator(size,min_range,max_range):
    random_numbers = []#declaring empty list
    for it in range(size):#running upto specified size
        #appending list with random numbers
      random_numbers.append(random.randint(min_range,max_range))
    #returing list with random numbers 
    return random_numbers

#List container to store random numbers
set_1 = random_num_generator(LIST_SIZE_SET_1,MIN_RANGE,MAX_RANGE)
set_2 = random_num_generator(LIST_SIZE_SET_2,MIN_RANGE,MAX_RANGE)
set_3 = random_num_generator(LIST_SIZE_SET_3,MIN_RANGE,MAX_RANGE)
#storing the lists within a list
DATASETS = [set_1,set_2,set_3]

#defining selection sort algorithm
def selection_sort(arr):
    camparison_count['selection_sort'] += 1
    #getting the lenght of the array
    arr_lenght = len(arr);
    #nesting loop
    for x in range(arr_lenght-1):
        #innder loop
        for y in range(x+1,arr_lenght):
            if arr[x]>arr[y]:
                camparison_count['selection_sort'] += 1
                #swapping if found the greater value than the out loop element
                arr[x],arr[y]=arr[y],arr[x]
                
#defining MergeSort algorithm 
def merge_sort(arr):
    camparison_count['merge_sort'] += 1
    #recursive
    if len(arr)>1:#only true if array size is greater than 1
        camparison_count['merge_sort'] += 1
        left_half = arr[:len(arr)//2]#storing the left half of the array
        right_half = arr[len(arr)//2:]#storing the right half of the array
        merge_sort(left_half)#sorting the left of the the array
        merge_sort(right_half)#sorting the right of the the array
        #these indexs been defined to keep track of :
        #left half arr,right half arr and original array respectively
        idx1,idx2,idx3 = 0,0,0
        #sorting and merging the divided array left half to right half
        while idx1<len(left_half) and idx2<len(right_half):
            camparison_count['merge_sort'] += 1
            #Comparing and merging the sorted element into the original array
            if left_half[idx1] < right_half[idx2]:
                camparison_count['merge_sort'] += 1
                arr[idx3] = left_half[idx1]
                idx1 += 1
            else:
                arr[idx3] = right_half[idx2]
                idx2 += 1
            idx3 += 1
        #Merging the other lefted arrays elements which are already sorted
        while idx1 < len(left_half):
            camparison_count['merge_sort'] += 1
            arr[idx3]= left_half[idx1]
            idx1 += 1
            idx3 += 1
        #similary out of right half of the array
        while idx2 < len(right_half):
            camparison_count['merge_sort'] += 1
            arr[idx3]= right_half[idx2]
            idx2 += 1
            idx3 += 1

#defining quick sort algorithm
def quick_sort(arr):
    #this function is definied to put pivot on its original sorted place
    def partition(arr,low,high):
        pivot = arr[high]#pivot as a last element is array
        idx = low-1 #setting null value yet 
        for x in range(low,high):
            #moving all elements smaller than pivot
            if arr[x] < pivot:
               camparison_count['quick_sort'] += 1
               idx+=1
               arr[x],arr[idx] = arr[idx],arr[x]
        #moving pivot at the end of the smaller elements
        idx+=1
        arr[idx],arr[high]=arr[high],arr[idx]
        return idx
    def sort(arr,low,high):
        if low<high:
           camparison_count['quick_sort'] += 1
           pivot = partition(arr,low,high)
           #recursivley dividing arrays
           sort(arr,low,pivot-1)
           sort(arr,pivot+1,high)
    #Inititing QuickSort
    sort(arr,0,len(arr)-1)
    
def time_complexity(arr,func):
    copied = list(arr)
    starting_time = time.time()
    func(copied)
    return time.time()-starting_time  
ALGORITHMS = [selection_sort,merge_sort,quick_sort]
time_elapsed_selection_sort = []
time_elapsed_merge_sort = []
time_elapsed_quick_sort = []

index = 0
#Calculating time complexity of datasets with different sorting algorithms

#calculating time Elapsed to sort Different sets of  DATASETS with different algorithms
for data_set in DATASETS:
    time_elapsed_selection_sort.append(time_complexity(data_set,selection_sort))
    time_elapsed_merge_sort.append(time_complexity(data_set,merge_sort))
    time_elapsed_quick_sort.append(time_complexity(data_set,quick_sort))


# Plotting the graph
plt.figure(figsize=(10, 6))  # Setting figure size

# Plotting for Selection Sort
plt.plot([LIST_SIZE_SET_1, LIST_SIZE_SET_2, LIST_SIZE_SET_3], time_elapsed_selection_sort, marker='o', label='Selection Sort')

# Plotting for Merge Sort
plt.plot([LIST_SIZE_SET_1, LIST_SIZE_SET_2, LIST_SIZE_SET_3], time_elapsed_merge_sort, marker='o', label='Merge Sort')

# Plotting for Quick Sort
plt.plot([LIST_SIZE_SET_1, LIST_SIZE_SET_2, LIST_SIZE_SET_3], time_elapsed_quick_sort, marker='o', label='Quick Sort')

plt.xlabel('Input Size')  # Label for x-axis
plt.ylabel('Time Complexity')  # Label for y-axis
plt.title('Time Complexity Analysis of Sorting Algorithms')  # Title for the plot
plt.legend()  # Showing legend
plt.grid(True)  # Displaying grid
plt.show()  # Displaying the plot
