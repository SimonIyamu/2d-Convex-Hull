from sys import exit
import numpy as np
import matplotlib.pyplot as plt

def validity_check(user_input):
    """
        input:  user_input  --> string
        output: pointsNo    --> positive integer number

        The function checks if the argument user_input represents a positive integer.
            ===> If the user_input string represents a positive number, return that number.
            ===> If not, raise a ValueError exception, print a diagnostic message in stderr and terminate the application.
    """
    try:
        pointsNo = int(user_input)
        if pointsNo <= 0:
            raise ValueError
    except ValueError:
        print("Invalid user input. The given number of points must be a positive integer.")
        exit(1)
    return pointsNo

def random_points():
    """
        input:      -
        output:     points_2d   --> a numpy ndarray containg 2D-points

        The function asks for the user to insert the number of 2D points that will be randomly generated.
        The function asserts that the user's input is valid.
        Then the given number of 2D points is randomly generated and stored in points_2d numpy ndarray.
        The function returns the points_2d numpy ndarray.
    """
    user_input  =   input("Number of 2D points: ")
    pointsNo    =   validity_check(user_input)
    points_2d   =   np.random.rand(pointsNo,2)
    return points_2d

def find_1st_point(points_2d):
    """
        input:      points_2d           --> a numpy ndarray containing all the 2D-points
        output:     first_point         --> a tuple representing the coordinates of the fist point of the convex hull in the points_2d numpy ndarray

        The function finds the 2D-points with the minimum x-coordinate.
        If there are multiple 2D-points with the minimum x-coordinate, the function chooses the 2D-point with the minimum y-coordinate.
        This will be the first point of the convex hull.
        The function returns this point.  
    """
    minx = np.amin(points_2d[:,0])
    minx_index = np.where(points_2d[:,0] == minx)[0]
    miny_ar_index = np.argmin(points_2d[minx_index,1])
    first_point_ind = minx_index[miny_ar_index]
    first_point = tuple(points_2d[first_point_ind])
    return first_point

def det_sign(point0, point1, point2):
    """
        input:  point0      --> a tupple with the coordinates of p0
                point1      --> a tupple with the coordinates of p1
                point2      --> a tupple with the coordinates of p2
        output: 0           --> the determinant of (v1 = p1 - p0) and (v2 = p2 - p0) is 0
                1           --> the determinant of (v1 = p1 - p0) and (v2 = p2 - p0) is positive
                -1          --> the determinant of (v1 = p1 - p0) and (v2 = p2 - p0) is negative
        
        The function first calculates the v1 and v2 vectors. Then, it computes the determinant det[ [v1.x v1.y] [v2.x v2.y] ].
        Finally, the function returns 0/1/-1 based on the sign of the determinant.
    """
    v1 = ( point1[0] - point0[0], point1[1] - point0[1] )
    v2 = ( point2[0] - point0[0], point2[1] - point0[1] )
    det = v1[0] * v2[1] - v1[1] * v2[0]
    
    if det == 0:
        return 0
    elif det > 0:
        return 1
    else:
        return -1

def ordered(point0, point1, point2):
    assert(point0 != point1)
    assert(point0 != point2)
    assert(point1 != point2)

    v1 = ( point1[0] - point0[0], point1[1] - point0[1] )
    v2 = ( point2[0] - point0[0], point2[1] - point0[1] )

    l = v2[0]/v1[0]
    assert(abs(l - v2[1]/v1[1]) < 1.0e-15)

    return l>1

def gift_wrap(points_2d):
    if len(points_2d)<=2:
        convex_hull = list(map(tuple,points_2d))
        return convex_hull

    r0 = find_1st_point(points_2d)
    unused_points = set(map(tuple,points_2d))
    convex_hull = [r0]
    u = None
    while u != r0:
        it = iter(unused_points)

        r = convex_hull[-1]
        u = next(it)
        checked = 1

        if r == r0 and u == r0:
            u = next(it)
            checked = 2
        
        remove_list = [u]

        while checked < len(unused_points):
            t = next(it)
            if r == r0 and t == r0:
                checked = checked + 1
                continue 
            dsign = det_sign(r,u,t)
            if dsign < 0:
                u = t
                remove_list = [u]
            if dsign == 0:
                remove_list.append(t)
                if ordered(r,u,t):
                    u = t                
            checked = checked + 1
        
        for point in remove_list:
            unused_points.remove(point)

        if u != r0:
            convex_hull.append(u)

    return convex_hull


def convex_hull_plot(points_2d, convex_hull):
    convex_hull_polygon = convex_hull
    convex_hull_polygon.append(convex_hull[0])
    convex_hull_polygon = np.array(convex_hull)

    fig = plt.figure()

    plt.plot(points_2d[:,0], points_2d[:,1], 'o')
    plt.plot(convex_hull_polygon[:,0], convex_hull_polygon[:,1], 'r--')
    plt.title("Convex Hull produced by Gift Wrapping", fontweight="bold")

    print("\n\nClose the figure window to terminate the program.")
    fig.savefig('gift_wrap.png')
    plt.show()

def output(points_2d,convex_hull):
    print("\nThe generated points are: ", end="")
    print(list(map(tuple,points_2d)), end="\n\n")
    print("Using the gift wrap algorithm we found the convex hull to be: ", end="")
    print(convex_hull)


def main():
    points_2d = random_points()
    convex_hull = gift_wrap(points_2d)
    output(points_2d, convex_hull)
    convex_hull_plot(points_2d,convex_hull)

if __name__ == "__main__":
    main()

