vetor = [11, 61, 9, 3, 15, 47, 23, 51, 43, 13, 
57, 45, 19, 35, 49, 5, 25, 31, 27, 41, 
1, 55, 29, 37, 33, 53, 39, 17, 7, 21]

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step -1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

print("Elementos do vetor: ")
print(vetor)

insertionSort(vetor)
print("\nElementos do vetor em ordem crescente: ")
print(vetor)

