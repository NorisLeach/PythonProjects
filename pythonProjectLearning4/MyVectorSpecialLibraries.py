import numpy as np

class MyVector:
    def __init__(self, name_id, color, type, values):

        self.name_id = name_id
        self.color = color
        self.type = type
        self.values = np.array(values)

    def __str__(self):
        # Simple string representation
        return f"MyVector(name_id={self.name_id}, color={self.colour}, type={self.type}, values={self.values})"


    def add_scalar(self, scalar):
        self.values += scalar

    def add(self, vector):
        self.values += vector.values

    def subtract(self, vector):
        self.values -= vector.values

    def multiplication(self, vector):
        return np.dot(self.values, vector.values)

    def sum_of_vector_elements(self):
        return np.sum(self.values)

    def product_of_vector_elements(self):
        return np.prod(self.values)

    def average_of_vector_elements(self):
        return np.mean(self.values)

    def minimum_of_a_vector(self):
        return np.min(self.values)

    def maximum_of_a_vector(self):
        return np.max(self.values)

#//////////////////////////////////////////////////////

def test_add_scalar():
    vector = MyVector("v1", "r", 1, [1, 2, 3])
    vector.add_scalar(2)
    assert np.all(vector.values == [3, 4, 5])

def test_add():
    vector1 = MyVector("v1", "r", 1, [1, 2, 3])
    vector2 = MyVector("v2", "b", 2, [4, 5, 6])
    vector1.add(vector2)
    assert np.all(vector1.values == [5, 7, 9])

def test_subtract():
    vector1 = MyVector("v1", "r", 1, [5, 6, 7])
    vector2 = MyVector("v2", "b", 2, [1, 2, 3])
    vector1.subtract(vector2)
    assert np.all(vector1.values == [4, 4, 4])

def test_multiplication():
    vector1 = MyVector("v1", "r", 1, [1, 2, 3])
    vector2 = MyVector("v2", "b", 2, [4, 5, 6])
    result = vector1.multiplication(vector2)
    assert result == (1*4 + 2*5 + 3*6)

def test_sum_of_vector_elements():
    vector = MyVector("v1", "r", 1, [1, 2, 3])
    result = vector.sum_of_vector_elements()
    assert result == sum([1, 2, 3])

def test_product_of_vector_elements():
    vector = MyVector("v1", "r", 1, [1, 2, 3])
    result = vector.product_of_vector_elements()
    assert result == np.prod([1, 2, 3])

def test_average_of_vector_elements():
    vector = MyVector("v1", "r", 1, [1, 2, 3])
    result = vector.average_of_vector_elements()
    assert result == np.mean([1, 2, 3])

def test_minimum_of_a_vector():
    vector = MyVector("v1", "r", 1, [1, 2, 3])
    result = vector.minimum_of_a_vector()
    assert result == np.min([1, 2, 3])

def test_maximum_of_a_vector():
    vector = MyVector("v1", "r", 1, [1, 2, 3])
    result = vector.maximum_of_a_vector()
    assert result == np.max([1, 2, 3])