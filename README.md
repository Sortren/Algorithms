# Algorithms

 Most common algorithms, such as binary search, merge sort, quick sort, Dijkstra's algorithm and so on, will be added here on this repository using python.
 If you are intrested, just click the follow button and enjoy ;). 
 
 # Merge sort:
 In brief, this algorithm is quite efficient with O(n log n) complexity (worst case scenario). It's based on recursion, it slices the passed array to smaller arrays
 and it's purpose is to decrease the size of an each array to one. When it will be done, the comparision part will be started. It will compare values from left array 
 with values on right array. Smaller value will be put on the first place at the main array. Due to recursively calling a function, we have to deal with a call stack. 
 When the first "if statement" returns false, the function will go back to the last part of the call stack and continue running, so we have to keep it in mind if we want
 to know how it works properly. That might sound a bit confusing but it will be present better on the diagram.
![first_step](https://user-images.githubusercontent.com/79079000/115121259-f0a05800-9fb1-11eb-9d66-29b80ff094cb.png)
First part was to choose the mid point of an array. It will be always floored length of array divided by two. Next step is to slice the array, everything what's on left side
from mid point goes to "left" array, analogically the same will happen to the right side of the array. When we recursively call this function couple times, we will be
at the point where all arrays are limited to one element, that's what we need! Now we have to travel beetween the elements and compare them to each other. 
So we simply declare variables to represent the indexes of given arrays and start to compare. If the value on the right is lesser than value on the left, it's going to 
be put at the first place in the array one step higher in the "tree". We increase the values of index variables when the statements retun true, and start to merging 
all the arrays so on. 
The main goal is to reach the point when we've got one part of the array that is sorted. I hope that it will be understood after this image:
![second_step](https://user-images.githubusercontent.com/79079000/115121555-a61fdb00-9fb3-11eb-8a6a-da518c80586e.png)
Now the same will happen to the right branch of the "tree", the array will be splitted, values compared and replaced the original values in higher array. 
![step_three](https://user-images.githubusercontent.com/79079000/115122426-32cc9800-9fb8-11eb-88dc-9afa83569c70.png)
So now we have to merge this two sorted arrays (left and right) to one array that is higher (quite logical, in case that we have done the same thing beneath :p)
The trick is that we have two arrays with two elements each, the algorithm still looks the same but it might be a little bit confusing. I described this as a comment in 
the main .py file. 
It should look like this:
![step_four](https://user-images.githubusercontent.com/79079000/115122396-0f095200-9fb8-11eb-99d4-a91a515eb937.png)
Now it's the part when the program will do exacly the same as it had done with the left "branch". There is no point to explain this one more time. Literally,
We are done with writing our code, even when we just finished to code the left "branch" of the tree. It might be proved by something called "inductive proof", it's a mathematical
proof, that you could find on the internet. It's really bounded to recursion, I encourage you to look through this.
Thus, the right part of the tree should look like this:
![step_five](https://user-images.githubusercontent.com/79079000/115122616-1ed56600-9fb9-11eb-9d36-c5d45bf38d1c.png)
Now the same will happen, algorithm will merge both left and right arrays in the "tree" and replace original array with a new - sorted one. 
(BTW I marked the right branch with "IX" number, that means the same operation order is going to happen as on the left branch)
You might know the result:
![step_final](https://user-images.githubusercontent.com/79079000/115122793-17628c80-9fba-11eb-96e0-0496e69f9b2e.png)
Important things weren't cover today, such as how does the recusrion, and the call stack really work. Therefore, I really encourage you to look through 
"Grokking algorithms" by Aditya Y. Bhargava, best book for beginners in algorithms. 
That's it for the merge sort!



