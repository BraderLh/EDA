from time import time

def insertion_sort(nums):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert

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
    #print("\nLista sin ordenar: \n", nums_int)
    #insertion_sort(nums_int)
    #print("\nLista ordenada: \n", nums_int)
def set_data(tamanho,tiempo):
  helper = open("insertion_Python.txt","a");
  helper.write(str(tamanho) + " , "+ str(tiempo) + "\n")
  helper.close()
# Verify it works
random_list_of_nums = []
for k in range(50,10001,50):
    random_list_of_nums = llenar_array(random_list_of_nums, k)
    print('\t',len(random_list_of_nums))
    start_time = time()
    insertion_sort(random_list_of_nums)
    elapsed_time = time() - start_time
    elapsed_time=round(float(elapsed_time),4)
    set_data(len(random_list_of_nums), elapsed_time)
    #print(elapsed_time)
    #elapsed_time=elapsed_time*1000
    #print(elapsed_time)
    del random_list_of_nums[:]