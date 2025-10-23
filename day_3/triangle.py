# # Returns the area of a triangle given its base and height
# def triangle_area(base, height):
#     return 0.5 * base * height
# print(triangle_area(int(input("Base: ")), int(input("Height: "))))

# # Returns the perimeter of a triangle given the lengths of its three sides
# def triangle_perimeter():
#     side_a = int(input("Side A: "))
#     side_b = int(input("Side B: "))
#     side_c = int(input("Side C: "))
#     return side_a + side_b + side_c

# print(triangle_perimeter())

# Return the area and perimeter of a rectangle given its length and width
# def rect_area(length, width):
#     return length * width

# def rect_perimeter(length, width):
#     return 2 * (length + width)

# length = int(input("Length: "))
# width = int(input("Width: "))

# print("Area:", rect_area(length, width))
# print("Perimeter:", rect_perimeter(length, width))

# rad = float(input("Radius: "))
# pi = 3.1415
# def circle_area(radius):
#     return pi * radius ** 2
# def circle_circumference(radius):
#     return (2 * pi * radius)
# print("Area:", round(circle_area(rad),4))
# print("Circumference:", round(circle_circumference(rad)))

# calculate slope, x-intercept and y-intercept of y = 2x -2
# its in slope intercept form y = mx + b so i dont need to calculate m and b,
# so for this exercise i will calculate x and y intercepts

## Question 8
# Uncomment below to take user input
# m = float(input("m: "))
# b = float(input("b: "))


# m = 2
# b = -2

# def x_intercept(m, b):
#     return -b / m

# def y_intercept(b):
#     return b

# print("X-Intercept:", x_intercept(m, b))
# print("Y-Intercept:", y_intercept(b))
# print("Slope:", m)
# #store slope for later
# q8m = m

# ## Queston 9
# #Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between 
# # point (2, 2) and point (6,10)

# y=0
# x=0

# def slope(x1, y1, x2, y2):
#     return (y2 - y1) / (x2 - x1)    

# def euclidean_distance(x1, y1, x2, y2):
#     return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# x1, y1 = 2, 2
# x2, y2 = 6, 10

# print("Slope:", slope(x1, y1, x2, y2))
# print("Euclidean Distance:", euclidean_distance(x1, y1, x2, y2))


#question 23
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
write a python script to print the table above

"""
def generate_row(n):
    """
    Generates a row for the table in Q23.
    """
    return f"{n} {1} {n} {n**2} {n**3}"

def print_table():
    """
    Prints the table for Q23.
    """
    for i in range(1, 6):
        print(generate_row(i))  

print_table()
