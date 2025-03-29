import MyVector
from MyVector import MyVector

import VectorRepository
from VectorRepository import VectorRepository

import matplotlib.pyplot as plt

from VectorRepository import VectorRepository

print("For add_scalar function type 1")
print("For add function type 2")
print("For subtract function type 3")
print("For multiplication function type 4")
print("For sum_of_vector_elements function type 5")
print("For product_of_vector_elements function type 6")
print("For average_of_vector_elements function type 7")
print("For minimum_of_a_vector function type 8")
print("For maximum_of_a_vector function type 9")

repo = VectorRepository()

repo.addVector(MyVector("v1", 'r', 2, [1, 2, 3]))
repo.addVector(MyVector("v2", 'b', 1, [2, 4, 6]))
repo.addVector(MyVector("v3", 'g', 3, [3, 5, 7]))
repo.addVector(MyVector("v4", 'y', 99, [4, 8, 12]))
repo.addVector(MyVector("v5", 'm', 22, [11, 2, 3]))
repo.addVector(MyVector("v6", 'b', 10, [22, 44, 6]))
repo.addVector(MyVector("v7", 'g', 13, [33, 50, 7]))
repo.addVector(MyVector("v8", 'm', 1, [44, 80, 12]))
repo.addVector(MyVector("v9", 'g', 3, [13, 5, 70]))
repo.addVector(MyVector("v10", 'm', 99, [9, 8, 12]))

print("For addVector function type 10")
print("For getAllVectors function type 11")
print("For getVectorAtGivenIndex function type 12")
print("For updateVectorAtGivenIndex function type 13")
print("For updateVectorIdentifiedBy_name_id function type 14")
print("For deleteVectorByIndex function type 15")
print("For deleteVectorBy_name_id function type 16")
print("For plotAllVectors function type 17")
print("For list_of_vectors_with_minimum_less_than_GivenValue function type 18")
print("For delete_all_vectors_with_max_value_equal_to_GivenValue function type 19")
print("For update_vectors_by_type_color function type 20")

def main():
    while True:
        x = int(input("   Enter a number between 1 and 20   "))
        if x == 1:
            MyVector.add_scalar(int(input()))
        elif x == 2:
            MyVector.add(MyVector(input(), input(), int(input()), input()))
        elif x == 3:
            MyVector.subtract(MyVector(input(), input(), int(input()), input()))
        elif x == 4:
            MyVector.multiplication(MyVector(input(), input(), int(input()), input()))
        elif x == 5:
            MyVector.sum_of_vector_elements()
        elif x == 6:
            MyVector.product_of_vector_elements()
        elif x == 7:
            MyVector.average_of_vector_elements()
        elif x == 8:
            MyVector.minimum_of_a_vector()
        elif x == 9:
            MyVector.maximum_of_a_vector()
        elif x == 10:
            repo.addVector(MyVector(input(), input(), int(input()), input()))
        elif x == 11:
            repo.getAllVectors()
        elif x == 12:
            repo.getVectorAtGivenIndex(int(input()))
        elif x == 13:
            repo.updateVectorAtGivenIndex(int(input()), MyVector(input(), input(), int(input()), input()))
        elif x == 14:
            repo.updateVectorIdentifiedBy_name_id(input(), MyVector(input(), input(), int(input()), input()))
        elif x == 15:
            repo.deleteVectorByIndex(int(input()))
        elif x == 16:
            repo.deleteVectorBy_name_id(input())
        elif x == 17:
            repo.plotAllVectors()
        elif x == 18:
            repo.list_of_vectors_with_minimum_less_than_GivenValue(int(input()))
        elif x == 19:
            repo.delete_all_vectors_with_max_value_equal_to_GivenValue(int(input()))
        elif x == 20:
            repo.update_vectors_by_type_color(1, input())
        elif x == 0:
            break
        else:
            print("Invalid value!")
            raise ValueError("the number must be from 1 to 20")



if __name__ == '__main__':
    try:
        main()
    except ValueError as er:
        print("exceptional case: ", er)








