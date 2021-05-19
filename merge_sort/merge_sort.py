def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid] #slicing from begging to mid point (excluded)
        right = array[mid:] #from mid point (included) to the end of passed array

        merge_sort(left)
        merge_sort(right)

        #When we limit all arrays to the one element, we have to travel all indexes (both, left and right array) 
        # and compare them to each other, we're going to merge the arrays in this step
        # the array will be merged from the bottom of a branch to the top
        # (in the first step it will be only arrays that are on the left side of the tree)

        #let's prepare variables that are going to represent an arrray indexes

        i = 0 # -> left array indexes
        j = 0 # -> right array indexes
        k = 0 # -> array passed as a parameter /we'll be merging arrays and put values to the passed array/

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1 

            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(left):
            array[k] = right[j]
            j += 1
            k += 1

        

#TEST OF THE MERGE SORT ALGORITHM
array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Original array ->", array) #printing an array before sorting it

merge_sort(array)

print("Sorted array ->",array) #printing an array after sorting
