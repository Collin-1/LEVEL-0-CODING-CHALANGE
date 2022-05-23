from math import sqrt


def area_of_triangle(side_a, side_b, side_c):
    semi = 1 / 2 * (side_a + side_b + side_c)
    area = sqrt(semi * (semi - side_a) * (semi - side_b) * (semi - side_c))
    return area


print(area_of_triangle(3, 4, 5))
