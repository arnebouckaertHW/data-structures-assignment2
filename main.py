from serialsearch import *

list1 = ['E', 'B', 'E', 'F', 'A', 'F']
list2 = ['E', 'B', 'E', 'F', 'A', 'F']
list3 = ['E', 'B', 'E', 'F', 'A', 'C']
list4 = ['E', 'B', 'E', 'F', 'A', 'F', 'C']

def main(list1, list2):
    if(len(list1) != len(list2)):
        print("Two lists aren't strictly identical!")
        print(list1)
        print(list2)
        return
    
    for i in range(len(list1)):
        if(search(list2, i, 1, list1[i]) == -1):
            print("Two lists aren't strictly identical!")
            print(list1)
            print(list2)
            return
    
    print("Two lists are strictly identical!")
    print(list1)
    print(list2)

if __name__ == "__main__":
    main(list1, list2)
    main(list3, list1)
    main(list4, list1)