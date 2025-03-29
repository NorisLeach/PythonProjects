class MyPoint:

    def __init__(self, coord_x, coord_y, color):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.color = color


    def set_coord_x(self, x):
        self.coord_x = x

    def set_coord_y(self, y):
        self.coord_y = y

    def set_color(self, color):
        self.color = color

    def get_coord_x(self):
        return self.coord_x

    def get_coord_y(self):
        return self.coord_y

    def get_color(self):
        return self.color

    def stringRepresentation(self):
        print("Point (" + str(self.coord_x), "," + str(self.coord_y), "\b) of color " + self.color, "\b.")


"""
   MyPoint Class

   Represents a point in 2D space with an associated color.

   Attributes:
       coord_x (float/int): The x-coordinate of the point.
       coord_y (float/int): The y-coordinate of the point.
       color (str): The color of the point.

   Methods:
       __init__(coord_x, coord_y, color):
           Initializes a new instance of MyPoint with specified x-coordinate, y-coordinate, and color.

       set_coord_x(x):
           Updates the x-coordinate of the point.

       set_coord_y(y):
           Updates the y-coordinate of the point.

       set_color(color):
           Updates the color of the point.

       get_coord_x():
           Returns the x-coordinate of the point.

       get_coord_y():
           Returns the y-coordinate of the point.

       get_color():
           Returns the color of the point.

       stringRepresentation():
           Prints a string representation of the point in the format: 
           "Point (x, y) of color <color>."
   """