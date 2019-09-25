from time import time
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j

        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

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
  helper = open("selection_Python.txt","a");
  helper.write(str(tamanho) + " , "+ str(tiempo) + "\n")
  helper.close()

random_list_of_nums = []
for k in range(50,10001,50):
    random_list_of_nums = llenar_array(random_list_of_nums, k)
    print('\t',len(random_list_of_nums))
    start_time = time()
    selection_sort(random_list_of_nums)
    elapsed_time = time() - start_time
    elapsed_time=round(float(elapsed_time),4)
    set_data(len(random_list_of_nums), elapsed_time)
    del random_list_of_nums[:]