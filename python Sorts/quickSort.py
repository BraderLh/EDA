from time import time
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

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
  helper = open("quick_Python.txt","a");
  helper.write(str(tamanho) + " , "+ str(tiempo) + "\n")
  helper.close()

random_list_of_nums = []
for k in range(50,10001,50):
    random_list_of_nums = llenar_array(random_list_of_nums, k)
    print('\t',len(random_list_of_nums))
    start_time = time()
    quick_sort(random_list_of_nums)
    elapsed_time = time() - start_time
    elapsed_time=round(float(elapsed_time),4)
    set_data(len(random_list_of_nums), elapsed_time)
    del random_list_of_nums[:]