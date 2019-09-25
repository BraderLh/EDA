from time import time

def bubble_sort(nums):

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
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
  helper = open("bubble_Python.txt","a");
  helper.write(str(tamanho) + " , "+ str(tiempo) + "\n")
  helper.close()


random_list_of_nums = []
random_list_of_nums = llenar_array(random_list_of_nums,1000)
print(random_list_of_nums)
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
del random_list_of_nums[:]
'''for k in range(50,10001,50):
    random_list_of_nums = llenar_array(random_list_of_nums, k)
    print('\t',len(random_list_of_nums))
    start_time = time()
    bubble_sort(random_list_of_nums)
    elapsed_time = time() - start_time
    elapsed_time=round(float(elapsed_time),4)
    #set_data(len(random_list_of_nums), elapsed_time)
    del random_list_of_nums[:]
'''



