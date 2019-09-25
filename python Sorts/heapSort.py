from time import time

def heapify(nums, heap_size, root_index):

    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def llenar_array(nums,n):
    with open ('E:/UNSA CS/2019/Semestre II/EDA/Programas de Lab/Lab 1/c++/numsAleatorios.txt','r') as fichero:
        lineas=fichero.readlines()
        fichero.close()
    contador=0

    i=0;
    for renglon in lineas:
        for palabra in renglon.split('\t'):
            contador+=1
            if(palabra!='' and i<n):
                nums.append(palabra)
                i+=1


    nums_int = [int(x) for x in nums]
    return  nums_int

def set_data(tamanho,tiempo):
  helper = open("heap_Python.txt","a");
  helper.write(str(tamanho) + " , "+ str(tiempo) + "\n")
  helper.close();

random_list_of_nums = []
for k in range(50,10001,50):
    random_list_of_nums = llenar_array(random_list_of_nums,k)
    print('\t',len(random_list_of_nums))
    start_time = time()
    heap_sort(random_list_of_nums)
    elapsed_time = time() - start_time
    elapsed_time=round(float(elapsed_time),4)
    set_data(len(random_list_of_nums), elapsed_time)
    del random_list_of_nums[:]
