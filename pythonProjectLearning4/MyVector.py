class MyVector:
    def __init__(self, name_id, color, type, values):

        self.name_id = name_id
        self.color = color
        self.type = type
        self.values = values

    def __str__(self):
        # Simple string representation
        return f"MyVector(name_id={self.name_id}, color={self.color}, type={self.type}, values={self.values})"


    def add_scalar(self, scalar):
        for i in range(0, len(self.values)):
            self.values[i] = self.values[i] + scalar

    def add(self, vector):
        for i in range(0, len(self.values)):
            self.values[i] = self.values[i] + vector.values[i]

    def subtract(self, vector):
        for i in range(0, len(self.values)):
            self.values[i] = self.values[i] - vector.values[i]

    def multiplication(self, vector):
        product = 0
        for i in range(0, len(self.values)):
            product = product + self.values[i] * vector.values[i]
        return  product

    def sum_of_vector_elements(self):
        sum = 0
        for i in range(0, len(self.values)):
            sum = sum + self.values[i]
        return sum

    def product_of_vector_elements(self):
        product = 1
        for i in range(0, len(self.values)):
            product = product * self.values[i]
        return product

    def average_of_vector_elements(self):
        return self.sum_of_vector_elements() / len(self.values)

    def minimum_of_a_vector(self):
        minimum = self.values[0]
        for i in range(0, len(self.values)):
            if self.values[i] < minimum:
                minimum = self.values[i]
        return minimum

    def maximum_of_a_vector(self):
        maximum = self.values[0]
        for i in range(0, len(self.values)):
            if self.values[i] > maximum:
                maximum = self.values[i]
        return maximum

#/////////////////////////////////////////////////

def test_add_scalar():
    vector = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])  # Updated to 'color'
    vector.add_scalar(2)  # Adding 2 to each value
    assert vector.values == [3, 4, 5]

def test_add():
    vector1 = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])  # Updated to 'color'
    vector2 = MyVector(name_id="v2", color='g', type=2, values=[4, 5, 6])  # Updated to 'color'
    vector1.add(vector2)
    assert vector1.values == [5, 7, 9]

def test_subtract():
    vector1 = MyVector(name_id="v1", color='r', type=1, values=[10, 20, 30])  # Updated to 'color'
    vector2 = MyVector(name_id="v2", color='g', type=2, values=[1, 2, 3])  # Updated to 'color'
    vector1.subtract(vector2)
    assert vector1.values == [9, 18, 27]

def test_multiplication():
    vector1 = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])  # Updated to 'color'
    vector2 = MyVector(name_id="v2", color='b', type=2, values=[4, 5, 6])  # Updated to 'color'
    result = vector1.multiplication(vector2)
    assert result == 32

def test_sum_of_vector_elements():
    vector = MyVector("v1", color='r', type=1, values=[1, 2, 3])  # Updated to 'color'
    result = vector.sum_of_vector_elements()
    assert result == 6

def test_product_of_vector_elements():
    vector = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])  # Updated to 'color'
    result = vector.product_of_vector_elements()
    assert result == 6

def test_average_of_vector_elements():
    vector = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])  # Updated to 'color'
    result = vector.average_of_vector_elements()
    assert result == 2.0

def test_minimum_of_a_vector():
    vector = MyVector(name_id="v1", color='r', type=1, values=[10, 5, 3, 8])  # Updated to 'color'
    result = vector.minimum_of_a_vector()
    assert result == 3

def test_maximum_of_a_vector():
    vector = MyVector(name_id="v1", color='r', type=1, values=[10, 5, 3, 8])  # Updated to 'color'
    result = vector.maximum_of_a_vector()
    assert result == 10


#///////////////////////////////////////////////////


    """
    A class to represent and manipulate a mathematical vector.

    Attributes:
    ----------
    name_id : str
        A unique identifier for the vector.
    color : str
        A descriptive attribute for the vector's color.
    type : str
        Specifies the category or type of the vector.
    values : list of int/float
        A list of numerical values representing the vector's components.

    Methods:
    -------
    __str__():
        Returns a string representation of the vector.
    add_scalar(scalar):
        Adds a scalar value to each element of the vector.
    add(vector):
        Performs element-wise addition with another vector.
    subtract(vector):
        Performs element-wise subtraction with another vector.
    multiplication(vector):
        Computes the dot product of the vector with another vector.
    sum_of_vector_elements():
        Calculates the sum of all elements in the vector.
    product_of_vector_elements():
        Calculates the product of all elements in the vector.
    average_of_vector_elements():
        Computes the average of the vector's elements.
    minimum_of_a_vector():
        Finds the smallest element in the vector.
    maximum_of_a_vector():
        Finds the largest element in the vector.
    """
