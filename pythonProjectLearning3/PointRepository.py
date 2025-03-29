from MyPoint import MyPoint
import math
import matplotlib.pyplot as plt

class PointRepository:
    def __init__(self):
        self.points = []

    def __repr__(self, index):
        return f"MyPoint(x = {self.points[index].coord_x}, y = {self.points[index].coord_y}, color = {self.points[index].color})"

    def addPoint(self, point):
        self.points.append(point)

    def getAllPoints(self):
        return self.points

    def getPointAtIndex(self, index):
        return self.points[index]

    def getPointAtColor(self, color):
        for i in range(0,len(self.points)):
            if self.points[i].color == color:
                print(self.points[i])

    def pointsInsideSquare(self, up_left_corner_x, up_left_corner_y, length):
        for i in range(0, len(self.points)):
            if (self.points[i].coord_x >= up_left_corner_x) & (self.points[i].coord_x <= up_left_corner_x + length) & (self.points[i].coord_y >= up_left_corner_x - length) & (self.points[i].coord_x <= up_left_corner_y):
                print(self.points[i])

    def minimumDistanceBetweenTwoPoints(self):
        min_distance = float('inf')
        for i in range(0, len(self.points) - 1):
            for j in range(i+1, len(self.points)):
                distance = math.sqrt( (self.points[j].coord_x - self.points[i].coord_x) ** 2 + (self.points[j].coord_y - self.points[i].coord_y) ** 2 )
                if distance < min_distance:
                    min_distance = distance
        return min_distance

    def update_point(self, index, x, y, color):
        self.points[index].coord_x = x
        self.points[index].coord_y = y
        self.points[index].color = color

    def delete_point(self, index):
        del(self.points[index])

    def delete_points_from_square(self, up_left_corner_x, up_left_corner_y, length):
        for i in range(0, len(self.points)):
            if (self.points[i].coord_x >= up_left_corner_x) & (self.points[i].coord_x <= up_left_corner_x + length) & (self.points[i].coord_y >= up_left_corner_x - length) & (self.points[i].coord_x <= up_left_corner_y):
                del(self.points[i])

    def plotAllPoints(self):
        x = []
        y = []
        col = []
        for i in range(0, len(self.points)):
            x.append(self.points[i].coord_x)
            y.append(self.points[i].coord_y)
            col.append(self.points[i].color)
        plt.scatter(x, y, c=col)
        plt.show()


    def maxiumDistanceBetweenTwoPoints(self):
        max_distance = 0
        for i in range(0, len(self.points) - 1):
            for j in range(i+1, len(self.points)):
                distance = math.sqrt( (self.points[j].coord_x - self.points[i].coord_x) ** 2 + (self.points[j].coord_y - self.points[i].coord_y) ** 2 )
                if distance > max_distance:
                    max_distance = distance
        return max_distance

    def shiftPointsOnXAxis(self, value):
        for i in range(0, len(self.points)):
            self.points[i].coord_x = self.points[i].coord_x + value

    def deletPointsWithinACertainDistanceFromPoint(self, Xa, Ya, dist):
        for i in range(0, len(self.points)):
            distance = math.sqrt( (self.points[i].coord_x - Xa) ** 2 + (self.points[i].coord_y - Ya) ** 2 )
            if(distance == dist):
                del(self.points[i])

    def numberOfPointsOfColor(self, color):
        nr = 0
        for i in range(0, len(self.points)):
            if self.points[i].color == color:
                nr += 1
        return nr
"""
def TEST_number_of_points_test():
    assert PointRepository.numberOfPointsOfColor("red") == 4

def TEST_deletPointsWithinACertainDistanceFromPoint():
    assert PointRepository.deletPointsWithinACertainDistanceFromPoint(2, 4, 3) == [1, 2, 3, 5]

def TEST_shiftPointsOnXAxis():
    assert PointRepository.shiftPointsOnXAxis(4) == 5

def TEST_maxiumDistanceBetweenTwoPoints():
    assert  PointRepository.maxiumDistanceBetweenTwoPoints() == 4

def TEST_minimumDistanceBetweenTwoPoints():
    assert  PointRepository.minimumDistanceBetweenTwoPoints() == 1
"""

repo = PointRepository()

repo.addPoint(MyPoint(1, 2, "red"))
repo.addPoint(MyPoint(1, 3, "blue"))
repo.addPoint(MyPoint(5, 7, "yellow"))
repo.addPoint(MyPoint(10, 11, "black"))
repo.addPoint(MyPoint(2, 2, "red"))
repo.addPoint(MyPoint(1, 10, "red"))
repo.addPoint(MyPoint(7, 3, "blue"))
repo.addPoint(MyPoint(17, 7, "purple"))
repo.addPoint(MyPoint(10, 11, "black"))
repo.addPoint(MyPoint(2, 5, "red"))

"""
x = []
y = []
col = []

repo.plotAllPoints()

plt.scatter(x, y, c = col)
plt.show()"""

"""
PointRepository Class Documentation

The `PointRepository` class is designed to manage a collection of `MyPoint` objects. 
It provides functionality to add, retrieve, update, delete, and analyze points, as well as visualize them on a 2D plot.

Class: MyPoint
---------------
This class is assumed to represent a point in a 2D coordinate system with an additional `color` attribute.
Each `MyPoint` instance should have the following attributes:
    - coord_x (float): X-coordinate of the point.
    - coord_y (float): Y-coordinate of the point.
    - color (str): Color of the point, used in plotting and filtering points.

Class: PointRepository
-----------------------
A class that stores and manages a list of `MyPoint` objects.

Methods
-------
__init__():
    Initializes an empty list of points.

__repr__(index):
    Returns a string representation of the point at the specified `index`.

addPoint(point: MyPoint):
    Adds a `MyPoint` object to the repository.

getAllPoints() -> list:
    Returns a list of all `MyPoint` objects in the repository.

getPointAtIndex(index: int) -> MyPoint:
    Retrieves the point at a given `index`.

getPointAtColor(color: str):
    Prints all points with the specified `color`.

pointsInsideSquare(up_left_corner_x: float, up_left_corner_y: float, length: float):
    Prints all points that lie within a square defined by the top-left corner (x, y) and the specified side `length`.

minimumDistanceBetweenTwoPoints() -> float:
    Calculates and returns the minimum Euclidean distance between any two points in the repository.

maxiumDistanceBetweenTwoPoints() -> float:
    Calculates and returns the maximum Euclidean distance between any two points in the repository.

update_point(index: int, x: float, y: float, color: str):
    Updates the coordinates and color of the point at the specified `index`.

delete_point(index: int):
    Deletes the point at the specified `index`.

delete_points_from_square(up_left_corner_x: float, up_left_corner_y: float, length: float):
    Deletes all points within a square defined by the top-left corner (x, y) and the specified side `length`.

plotAllPoints():
    Plots all points on a 2D scatter plot using their coordinates and colors.

shiftPointsOnXAxis(value: float):
    Shifts all points along the x-axis by a specified `value`.

deletPointsWithinACertainDistanceFromPoint(Xa: float, Ya: float, dist: float):
    Deletes all points that are at an exact distance `dist` from a specified point (Xa, Ya).

numberOfPointsOfColor(color: str) -> int:
    Returns the count of points with a specified `color`.
"""
