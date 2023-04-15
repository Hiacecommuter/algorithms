"""
Sorting Insertion
How it works
A- swapping
  1 - from arr[0] to arr[n-1], if arr[i]> arr[i+1], move arr[i+1] down until arr[i+1]>arr[j]
  2 - repeat
  
B - Move the greater elements one position up to make space for the swapped element
  1 - from arr[1] to arr[n-1], if arr[i]<arr[i-1], key = arr[i], arr[i] = arr[i-1]
  2 - compare key with arr[i-2], if key < arr[i-2], arr[i-1] = arr[i-2]
  3 - move element up one by one, until key > arr[j], put key in arr[j+1]
  4 - if the element needs to go to the 0 position, end loop need to put j=-1, so j+1 = 0

"""
#A:
for i in range(1,n):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            for j in range(i-1,0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                else:
                    break
#B:
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=key
