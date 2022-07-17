import numpy as np;
import time;


def sortTime(unsorted):
  start = time.time_ns();

  #bubble sort
  bubbleSort(unsorted);
  
  end = time.time_ns();
  print("\nTime to sort with Bubble Sort: ",end - start,"ms");

def bubbleSort(unsorted):
  sorted = False;

  while(sorted == False):
    swap = False;
    for i in range(len(unsorted)-2):
      if (unsorted[i]>unsorted[i+1]):
        temp = unsorted[i];
        unsorted[i] = unsorted[i+1];
        unsorted[i+1] = temp;
        swap = True;

    if (swap != True):
      sorted = True;




arr = np.random.randint(0,999,50);

# print("Unsorted array is:")
# for i in range(len(arr)):
#     print("% d" % arr[i], end=" ")
 
sortTime(arr);

# print("Sorted array is:")
# for i in range(len(arr)):
#     print("% d" % arr[i], end=" ")

  
