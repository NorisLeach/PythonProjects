from MyVector import MyVector
import matplotlib.pyplot as plt

class VectorRepository:

    def __init__(self):
        self.vectors = []

    def addVector(self, vector):
        self.vectors.append(vector)

    def getAllVectors(self):
        for i in range(0, len(self.vectors)):
            print(self.vectors[i])

    def getVectorAtGivenIndex(self, index):
        return self.vectors[index]

    def updateVectorAtGivenIndex(self, index, newVector):
        self.vectors[index] = newVector

    def updateVectorIdentifiedBy_name_id(self, nameId, newVector):
        for i in range(0, len(self.vectors)):
            if self.vectors[i].name_id == nameId:
                self.vectors[i] = newVector

    def deleteVectorByIndex(self, index):
        del(self.vectors[index])

    def deleteVectorBy_name_id(self, nameId):
        for i in range(len(self.vectors)-1, -1, -1):
            if self.vectors[i].name_id == nameId:
                del(self.vectors[i])

    def plotAllVectors(self):
        for i in range(0, len(self.vectors)):

            x = list(range(len(self.vectors[i].values)))
            y = self.vectors[i].values

            if self.vectors[i].type == 1:
                marker = 'o'  # Circle
            elif self.vectors[i].type == 2:
                marker = 's'  # Square
            elif self.vectors[i].type == 3:
                marker = '^'  # Triangle
            else:
                marker = 'D'  # Diamond for other values

            plt.scatter(x, y, marker=marker, color=self.vectors[i].color, label=self.vectors[i].name_id)

        plt.title("Vector Plot Based on Type and Color")
        plt.xlabel("Index of Values")
        plt.ylabel("Vector Values")
        plt.show()

    def nreg(self):
        return 59%3+21  #12 20 23

    def list_of_vectors_with_minimum_less_than_GivenValue(self, value): #12
        result = []
        for i in range(0, len(self.vectors)):
            if self.vectors[i].minimum_of_a_vector() < value:
                result.append(self.vectors[i])

    def delete_all_vectors_with_max_value_equal_to_GivenValue(self, value): #20
        for i in range(0, len(self.vectors)):
            if self.vectors[i].maximum_of_a_vector() == value:
                del(self.vectors[i])

    def update_vectors_by_type_color(self, vector_type, new_color):
        for i in range(0, len(self.vectors)):
            if self.vectors[i].type == vector_type:
                self.vectors[i].color = new_color


#//////////////////////////////////////

def test_addVector():
    repo = VectorRepository()
    vector = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])
    repo.addVector(vector)
    assert len(repo.vectors) == 1


def test_getAllVectors():
    repo = VectorRepository()
    repo.addVector(MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3]))
    repo.addVector(MyVector(name_id="v2", color='g', type=2, values=[4, 5, 6]))
    repo.addVector(MyVector(name_id="v3", color='b', type=3, values=[7, 8, 9]))

    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    repo.getAllVectors()
    sys.stdout = sys.__stdout__

    assert "v1" in captured_output.getvalue()
    assert "v2" in captured_output.getvalue()


def test_getVectorAtGivenIndex():
    repo = VectorRepository()
    vector = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])
    repo.addVector(vector)
    result = repo.getVectorAtGivenIndex(0)
    assert result.name_id == "v1"


def test_updateVectorAtGivenIndex():
    repo = VectorRepository()
    vector = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])
    new_vector = MyVector(name_id="v1", color='b', type=2, values=[4, 5, 6])
    repo.addVector(vector)
    repo.updateVectorAtGivenIndex(0, new_vector)
    result = repo.getVectorAtGivenIndex(0)
    assert result.color == 'b'


def test_updateVectorIdentifiedBy_name_id():
    repo = VectorRepository()
    vector = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])
    new_vector = MyVector(name_id="v1", color='b', type=2, values=[4, 5, 6])
    repo.addVector(vector)
    repo.updateVectorIdentifiedBy_name_id("v1", new_vector)
    result = repo.getVectorAtGivenIndex(0)
    assert result.color == 'b'


def test_deleteVectorByIndex():
    repo = VectorRepository()
    vector = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])
    repo.addVector(vector)
    repo.deleteVectorByIndex(0)
    assert len(repo.vectors) == 0


def test_deleteVectorBy_name_id():
    repo = VectorRepository()
    vector = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])
    repo.addVector(vector)
    repo.deleteVectorBy_name_id("v1")
    assert len(repo.vectors) == 0


def test_nreg():
    repo = VectorRepository()
    result = repo.nreg()
    assert result == 23


def test_list_of_vectors_with_minimum_less_than_GivenValue():
    repo = VectorRepository()
    vector1 = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])
    vector2 = MyVector(name_id="v2", color='g', type=2, values=[4, 5, 6])
    repo.addVector(vector1)
    repo.addVector(vector2)
    result = repo.list_of_vectors_with_minimum_less_than_GivenValue(4)
    assert len(result) == 1
    assert result[0].name_id == "v1"


def test_delete_all_vectors_with_max_value_equal_to_GivenValue():
    repo = VectorRepository()
    vector1 = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])
    vector2 = MyVector(name_id="v2", color='g', type=2, values=[4, 5, 6])
    repo.addVector(vector1)
    repo.addVector(vector2)
    repo.delete_all_vectors_with_max_value_equal_to_GivenValue(6)
    assert len(repo.vectors) == 1
    assert repo.vectors[0].name_id == "v1"


def test_update_vectors_by_type_color():
    repo = VectorRepository()
    vector1 = MyVector(name_id="v1", color='r', type=1, values=[1, 2, 3])
    vector2 = MyVector(name_id="v2", color='b', type=2, values=[4, 5, 6])
    repo.addVector(vector1)
    repo.addVector(vector2)
    repo.update_vectors_by_type_color(1, 'g')
    assert repo.vectors[0].color == 'g'


#/////////////////////////////////////////


    """
    A repository for managing and manipulating a collection of vectors. 
    Provides advanced operations for querying, updating, and visualizing vector data.

    Attributes:
    ----------
    vectors : list of MyVector
        A list that holds vector objects.

    Methods:
    -------
    addVector(vector):
        Adds a new vector to the repository.

    getAllVectors():
        Prints all vectors currently stored in the repository.

    getVectorAtGivenIndex(index):
        Retrieves the vector stored at the given index.
        Raises IndexError if the index is out of bounds.

    updateVectorAtGivenIndex(index, newVector):
        Replaces the vector at the specified index with a new vector.

    updateVectorIdentifiedBy_name_id(nameId, newVector):
        Searches for a vector by its name_id and updates it with the new vector.
        Does nothing if no match is found.

    deleteVectorByIndex(index):
        Deletes the vector at the specified index.
        Raises IndexError if the index is out of bounds.

    deleteVectorBy_name_id(nameId):
        Deletes all vectors with a matching name_id. 
        Handles duplicate name_ids if present.

    plotAllVectors():
        Visualizes all vectors using matplotlib. 
        Plots are styled based on vector type and color:
            - Type 1: Circle marker
            - Type 2: Square marker
            - Type 3: Triangle marker
            - Other: Diamond marker

    list_of_vectors_with_minimum_less_than_GivenValue(value):
        Returns a list of vectors whose minimum element is less than the specified value.

    delete_all_vectors_with_max_value_equal_to_GivenValue(value):
        Deletes all vectors where the maximum element matches the specified value.

    update_vectors_by_type_color(vector_type, new_color):
        Updates the color of all vectors that match the given type.

    nreg():
        A simple utility function for a specific modulo operation.

    Examples:
    --------
    # Create a repository
    repo = VectorRepository()

    # Add vectors
    vector1 = MyVector("v1", "red", 1, [1, 2, 3])
    vector2 = MyVector("v2", "blue", 2, [4, 5, 6])
    repo.addVector(vector1)
    repo.addVector(vector2)

    # Visualize vectors
    repo.plotAllVectors()

    # Update a vector
    repo.updateVectorIdentifiedBy_name_id("v1", MyVector("v1", "green", 1, [10, 20, 30]))
    """
