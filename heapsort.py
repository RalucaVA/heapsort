import time
st = time.time()


def heapify(data, N, i):
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2   
    if l < N and data[largest] < data[l]:
        largest = l
 
    if r < N and data[largest] < data[r]:
        largest = r
 
    if largest != i:
        data[i], data[largest] = data[largest], data[i]  
 
        heapify(data, N, largest)
 
 
def heapSort(data):
    N = len(data)

    for i in range(N//2 - 1, -1, -1):
        heapify(data, N, i)
 
    for i in range(N-1, 0, -1):
        data[i], data[0] = data[0], data[i]  
        heapify(data, i, 0)
 
 
import random
if __name__ == '__main__':
    dataset=[]
for i in range(4902939):
    #x=random.randrange(0, 500000339783)
        dataset.append(i)
        heapSort(dataset)
        N = len(dataset)
 
print("Sorted array is")
for i in range(N):
    print("%d" % dataset[i], end=" ")


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
