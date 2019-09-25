from time import time

def counting_sort(alist):
    largest = max(alist)
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1

    c[0] = c[0] - 1  # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(alist)

    for x in reversed(alist):
        result[c[x]] = x
        c[x] = c[x] - 1

    return result

def set_data(tamanho,tiempo):
  helper = open("counting_Python.txt","a");
  helper.write(str(tamanho) + " , "+ str(tiempo) + "\n")
  helper.close()

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

random_list_of_nums=[]
for k in range(50,10001,50):
    random_list_of_nums = llenar_array(random_list_of_nums, k)
    print('\t',len(random_list_of_nums))
    start_time = time()
    counting_sort(random_list_of_nums)
    elapsed_time = time() - start_time
    elapsed_time=round(float(elapsed_time),4)
    set_data(len(random_list_of_nums), elapsed_time)
    del random_list_of_nums[:]
