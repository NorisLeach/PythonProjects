import MyPoint
import PointRepository
import matplotlib.pyplot as plt


print("For addPoint type 1")
print("For getAllPoints type 2")
print("For getPointAtIndex type 3")
print("For getPointAtColor type 4")
print("For pointsInsideSquare type 5")
print("For minimumDistanceBetweenTwoPoints type 6")
print("For update_point type 7")
print("For delete_point type 8")
print("For delete_points_from_square type 9")
print("For plotAllPoints type 10")
print("For maxiumDistanceBetweenTwoPoints type 11")
print("For shiftPointsOnXAxis type 12")
print("For deletPointsWithinACertainDistanceFromPoint type 13")
print("For numberOfPointsOfColor type 14")

repo = PointRepository.PointRepository()
"""
repo.addPoint(MyPoint.MyPoint(1, 2, "red"))
repo.addPoint(MyPoint.MyPoint(1, 3, "blue"))
repo.addPoint(MyPoint.MyPoint(5, 7, "yellow"))
repo.addPoint(MyPoint.MyPoint(10, 11, "black"))"""

def main():
    while True:
        x = int(input("   Enter a number between 1 and 14   "))
        if x == 1:
            repo.addPoint(MyPoint.MyPoint(int(input()), int(input()), str(input())))
        elif x == 2:
            repo.getAllPoints()
        elif x == 3:
            repo.getPointAtIndex(int(input()))
        elif x == 4:
            repo.getPointAtColor(str(input()))
        elif x == 5:
            repo.pointsInsideSquare(int(input()), int(input()), int(input()))
        elif x == 6:
            repo.minimumDistanceBetweenTwoPoints()
        elif x == 7:
            repo.update_point(int(input()), int(input()), int(input()), str(input()))
        elif x == 8:
            repo.delete_point(int(input()))
        elif x == 9:
            repo.delete_points_from_square(int(input()), int(input()), int(input()))
        elif x == 10:
            repo.plotAllPoints()
        elif x == 11:
            repo.maxiumDistanceBetweenTwoPoints()
        elif x == 12:
            repo.shiftPointsOnXAxis(int(input()))
        elif x == 13:
            repo.deletPointsWithinACertainDistanceFromPoint(int(input()), int(input()), int(input()))
        elif x == 14:
            repo.numberOfPointsOfColor(str(input()))
        elif x == 0:
            break
        else:
            print("Invalid value!")
            raise ValueError("the number must be from 1 to 14")

if __name__ == '__main__':
    try:
        main()
    except ValueError as er:
        print("exceptional case: ", er)

