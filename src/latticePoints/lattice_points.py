from sys import exit
import math
import numpy as np
import matplotlib.pyplot as plt

def validity_check(user_input):
    """
        input:  user_input  --> string
        output: R           --> positive number

        The function checks if the argument user_input represents a positive number (either float or integer).
            ===> If the user_input string represents a positive number, return that number.
            ===> If not, raise a ValueError exception, print a diagnostic message in stderr and terminate the application.
    """
    try:
        R = float(user_input)
        if R <= 0.0:
            raise ValueError
    except ValueError:
        print("Invalid user input. Radius must be a positive number.")
        exit(1)
    return R

def lattice_points(R):
    """
        input:  R       -->  positve number
        output: lpoints -->  list

        The function finds the lattice points of the lattice points of the circle with center (0,0) and radius R, stores them in a list and returns that list.
    """
    lpoints = []
    if R != int(R):
        return lpoints

    max_abs_x = int(math.floor(R / math.sqrt(2)))
    for int_x in range(max_abs_x + 1):
        y = math.sqrt( R * R - int_x * int_x )
        int_y = int(y)
        if y == int_y:
            lpoints.append( (int_x,int_y) )
            lpoints.append( (int_y,int_x) )
            lpoints.append( (int_x,-int_y) )
            lpoints.append( (-int_y,int_x) )

            if int_x > 0:
                lpoints.append( (-int_x, int_y) )
                lpoints.append( (int_y, -int_x) )
                lpoints.append( (-int_x, -int_y) )
                lpoints.append( (-int_y, -int_x) )
                
    return lpoints

def output(lpoints):
    """
        input: lpoints -->  list
        output:   -

        The function prints the number of the lattice points stored in the list and then the list itself.
    """
    print("#Lattice points = " + str(len(lpoints)))
    print("Lattice points = ", end="")
    print(lpoints)

def lattice_points_plot(R, lpoints):
    """
        input:  R       -->  positve number
                lpoints -->  list
        output: -
        
        Create a plot of the circle with center (0,0) and radius R. Also draw the lattice points of the circle.
        Show the plot and wait unitl the user closes the figure window to continue with the execution of the program.
        Save the figure as "lattice_points.png".
    """
    fig = plt.figure()
    ax = fig.gca()
    ax.set_aspect('equal')

    circle = plt.Circle((0,0), R)
    ax.add_artist(circle)

    x_coords = []
    y_coords = []
    for point in lpoints:
        x_coords.append(point[0])
        y_coords.append(point[1])

    ax.scatter(x_coords, y_coords, color='red')
    for i_x, i_y in zip(x_coords, y_coords):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
    plt.text(0, 0, '({}, {})'.format(0, 0))

    plt_size = 1.1 * R
    ax.set_xlim((- plt_size, plt_size))
    ax.set_ylim((- plt_size, plt_size))

    if x_coords == []:
        x_coords = [-R,  0, 0, R]
        y_coords = [ 0, -R, R, 0]   
    ax.set_xticks(x_coords)
    ax.set_yticks(y_coords)
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)
    ax.tick_params(axis='both', which='major', labelsize=7)
    plt.grid()
    
    plt.title("Lattice points of circle with center (0,0) and radius R = " + str(R), fontweight="bold")

    fig.savefig('lattice_points.png')
    print("\n\nClose the figure window to terminate the program.")
    plt.show()

def main():
    user_input = input("Radius: ")      #Get user input for the circle radius
    R = validity_check(user_input)      #Check if it is valid
    lpoints = lattice_points(R)         #Find the lattice points of the circle
    output(lpoints)                     #Output the number of the lattice points and the lattice points
    lattice_points_plot(R,lpoints)      #Plot the circle with its lattice points.

if __name__ == "__main__":
    main()