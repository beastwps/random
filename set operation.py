
'''
Functions it can do
1) Add element to the SET.
2) Remove element from the the SET.
3) Search element in the SET.
4) Return size and all element from SET.
5) Intersect two SETs.
6) Union of two SETs.
7) Difference between two SETs.
8) Return true if B is SUBSET of A.
'''

import random
import itertools   #Itertools is a python library which helps to perform basic operation on SETs.

SET = set(())

def add_ele(user_ele):
    SET.update((user_ele,))
    
def rem_ele(user_ele):
    list_SET = list(SET)
    if user_ele in list_SET:
        SET.remove(user_ele)
        print("SET updated! New SET is {}".format(SET))
    else:
        print("No matching element found!")

def search_ele(user_ele):
    list_SET = list(SET)
    if user_ele in list_SET:
        print("{} is in given SET : {}".format(user_ele,SET))
    else:
        print("No matching element found!") 
   
def size_set():
    list_SET = list(SET)
    print("Size of given SET is {}".format(len(list_SET)))   
    
def print_set():
    print("Given set is {}".format(SET))
         
def intersect_sets():
    SET_b = set(())
    for i in range(random.randint(10,19)):
        temp = random.randint(1,999)
        SET_b.update((temp,))
    print("Given SET A is {}\nGiven SET B is {}".format(SET, SET_b))
    inter = SET.intersection(SET_b)
    print("Intersection of SET A and SET B is {}".format(inter))
    
def uni_sets():
    SET_b = set(())
    for i in range(random.randint(10,19)):
        temp = random.randint(1,999)
        SET_b.update((temp,))
    print("Given SET A is {}\nGiven SET B is {}".format(SET, SET_b))
    uni = SET.union(SET_b)
    print("Union of SET A and SET B is {}".format(uni))
    
def diff_sets():
    SET_b = set(())
    for i in range(random.randint(10,19)):
        temp = random.randint(1,999)
        SET_b.update((temp,))
    print("Given SET A is {}\nGiven SET B is {}".format(SET, SET_b))
    a_b = SET.difference(SET_b)
    b_a = SET_b.difference(SET)
    print("For A-B we have {}.\nFor B-A we have {}.".format(a_b,b_a))
    
def sub_set(user_sets, size):   
    print("Possible subsets of length {} are {}".format(size,list(map(set, itertools.combinations(user_sets, size)))))
    
# Main work function...
exit = 0

while exit != 1:
    choice = int(input("\n1 = Add element\n2 = Remove element\n3 = Search element\n4 = Display size of SET\n5 = Display SET element\n6 = Intersect between two SETs\n7 = Union between two SETs\n8 = Difference between two SETs\n9 = Display subsets of A\n0 = Exit\nEnter choice : "))
    
    if choice == 1:
        chc2 = int(input("1 = Enter manually\n2 = Add randomly\nChoice : "))
        if chc2 == 1:
            get_ele = int(input("Enter element to add : "))
            add_ele(get_ele)
            print("SET updated! New SET is {}".format(SET))
        elif chc2 == 2:
            how_many = int(input("How many element to add : "))
            for i in range(how_many):
                add_ele(random.randint(1,999))  
            print("SET updated! New SET is {}".format(SET))
        else:
            print("Invalid Choice!")
            
    elif choice == 2:
        print("This are elements from SET {}.".format(SET))
        get_ele = int(input("Enter element to remove : "))
        rem_ele(get_ele)
        
    elif choice == 3:
        get_ele = int(input("Enter element to search : "))
        search_ele(get_ele)
        
    elif choice == 4:
        size_set()
        
    elif choice == 5:
        print_set()
    
    elif choice == 6:
        intersect_sets()
        
    elif choice == 7:
        uni_sets()
        
    elif choice == 8:
        diff_sets()
        
    elif choice == 9:
        list_SET = list(SET)
        print("Given set is {}".format(SET))
        n1 = len(list_SET)
        print("There are {} possible subsets.".format(2**n1))
        while n1 != 0:
            sub_set(SET, n1)
            n1 -= 1
        if n1 == 0:
            print("Possible subsets of length 0 are [{}]")

    elif choice == 0:
        exit += 1
1 = Add element
2 = Remove element
3 = Search element
4 = Display size of SET
5 = Display SET element
6 = Intersect between two SETs
7 = Union between two SETs
8 = Difference between two SETs
9 = Display subsets of A
0 = Exit
Enter choice : 1
1 = Enter manually
2 = Add randomly
Choice : 2
How many element to add : 3
SET updated! New SET is {455, 802, 655}

1 = Add element
2 = Remove element
3 = Search element
4 = Display size of SET
5 = Display SET element
6 = Intersect between two SETs
7 = Union between two SETs
8 = Difference between two SETs
9 = Display subsets of A
0 = Exit
Enter choice : 9
Given set is {455, 802, 655}
There are 8 possible subsets.
Possible subsets of length 3 are [{655, 802, 455}]
Possible subsets of length 2 are [{802, 455}, {655, 455}, {802, 655}]
Possible subsets of length 1 are [{455}, {802}, {655}]
Possible subsets of length 0 are [{}]

1 = Add element
2 = Remove element
3 = Search element
4 = Display size of SET
5 = Display SET element
6 = Intersect between two SETs
7 = Union between two SETs
8 = Difference between two SETs
9 = Display subsets of A
0 = Exit
Enter choice : 0