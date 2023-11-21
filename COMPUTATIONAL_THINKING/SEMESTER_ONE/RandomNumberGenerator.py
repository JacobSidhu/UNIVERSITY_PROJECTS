#Importing Random Engine
import random
import time

MAX_RANGE = 999999#max range of the list elements
MIN_RANGE = 100000#min range of the list elements
#three different sizes for three different list arrays
LIST_SIZE_SET_1 = 100
LIST_SIZE_SET_2 = 1000
LIST_SIZE_SET_3 = 10000

#defining the random number generator function for reusablity
def random_num_generator(size,min_range,max_range):
    random_numbers = []#declaring empty list
    for it in range(size):#running upto specified size
        #appending list with random numbers
      random_numbers.append(random.randint(min_range,max_range))
    #returing list with random numbers 
    return random_numbers

#defining selection sort algorithm
def selection_sort(arr):
    #getting the lenght of the array
    arr_lenght = len(arr);
    #nesting loop
    for x in range(arr_lenght-1):
        #innder loop
        for y in range(x+1,arr_lenght):
            if arr[x]>arr[y]:
                #swapping if found the greater value than the out loop element
                arr[x],arr[y]=arr[y],arr[x]
                
#defining MergeSort algorithm 
def merge_sort(arr):
    #recursive
    if len(arr)>1:#only true if array size is greater than 1
        left_half = arr[:len(arr)//2]#storing the left half of the array
        right_half = arr[len(arr)//2:]#storing the right half of the array
        merge_sort(left_half)#sorting the left of the the array
        merge_sort(right_half)#sorting the right of the the array
        #these indexs been defined to keep track of :
        #left half arr,right half arr and original array respectively
        idx1,idx2,idx3 = 0,0,0
        #sorting and merging the divided array left half to right half
        while idx1<len(left_half) and idx2<len(right_half):
            #Comparing and merging the sorted element into the original array
            if left_half[idx1] < right_half[idx2]:
                arr[idx3] = left_half[idx1]
                idx1 += 1
            else:
                arr[idx3] = right_half[idx2]
                idx2 += 1
            idx3 += 1
        #Merging the other lefted arrays elements which are already sorted
        while idx1 < len(left_half):
            arr[idx3]= left_half[idx1]
            idx1 += 1
            idx3 += 1
        #similary out of right half of the array
        while idx2 < len(right_half):
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
               idx+=1
               arr[x],arr[idx] = arr[idx],arr[x]
        #moving pivot at the end of the smaller elements
        idx+=1
        arr[idx],arr[high]=arr[high],arr[idx]
        return idx
    def sort(arr,low,high):
        if low<high:
           pivot = partition(arr,low,high)
           #recursivley dividing arrays
           sort(arr,low,pivot-1)
           sort(arr,pivot+1,high)
    #Inititing QuickSort
    sort(arr,0,len(arr)-1)
    
def time_complexity(arr,func):
    copied = list(arr)
    list_length = len(arr)
    starting_time = time.time()
    func(copied)
    return time.time()-starting_time  

#List container to store random numbers
set_1 = random_num_generator(LIST_SIZE_SET_1,MIN_RANGE,MAX_RANGE)
set_2 = random_num_generator(LIST_SIZE_SET_2,MIN_RANGE,MAX_RANGE)
set_3 = random_num_generator(LIST_SIZE_SET_3,MIN_RANGE,MAX_RANGE)
#storing the lists within a list
DATASETS = [set_1,set_2,set_3]
#Calculating time complexity of datasets with different sorting algorithms
for x in range(len(DATASETS)):
    print(f"Time complexity of dataset of size {len(DATASETS[x])}")
    print(f" Selection Sort = {time_complexity(DATASETS[x],selection_sort)}")#Invoking for selection sort on each dataset
    print(f" merge Sort = {time_complexity(DATASETS[x],merge_sort)}")#Invoking for merge sort on each dataset
    print(f" Quick Sort = {time_complexity(DATASETS[x],quick_sort)}")#Invoking for quick sort on each dataset