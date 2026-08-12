
def swap_two_elements(alist, pos1, pos2):
    temp = alist[pos1]
    alist[pos1] = alist[pos2]
    alist[pos2] = temp

def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                swap_two_elements(alist, i, i+1)

def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        current_largest_item_index = 0
        for i in range(1, fillslot+1):
            if alist[i] > alist[current_largest_item_index]:
                current_largest_item_index = i
        
        # at the end of this pass (i.e. inner loop), 
        # move largest item to the fillslots position
        swap_two_elements(alist, fillslot, current_largest_item_index)
            
def insertionSort(alist):
    for index in range(1, len(alist)):
        item_to_be_inserted = alist[index]
        position = index
        while position > 0 and alist[position-1] > item_to_be_inserted:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = item_to_be_inserted



