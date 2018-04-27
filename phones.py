
import kdtree
import sys
import smallestcircle

""" Cordless Phones
    Takes a set of points and finds the maximum range of only 11.
    Utilises Nearest Neighbour search and KD trees.
    Etude 8 COSC326 2018
    @author Nikolah Peaerce, Megan Seto, Kiri Lenagh-Glue, & Megan Hayes.
"""

#
# Take in a KDNode and return its coordinates
# Coordinates returns as list of [x, y]
#
def pull_coordinate(node):
    pstr =  str(node[0])
     
    string_cords = pstr[12:(len(pstr)-3)]
    first_q = string_cords.find(',') - 1
    second_q = first_q + 4

    xstr = string_cords[:first_q-1]
    ystr = string_cords[second_q:]
    
    pts = []
    pts.append(float(xstr))
    pts.append(float(ystr))

    return pts

#
# Take in a list of KDNodess and return a list of the coordinates only
# Coordinates returns as list of [[x, y], [x, y]]
#
def pull_all_coordinates(all_nodes):
    i = 0
    nn_points = []
    while i < len(all_nodes):
        nn_p = pull_coordinate(all_nodes[i])
        nn_points.append(nn_p)
        i+=1
    return nn_points

#
# Loop through every point and check its K neighbours.
# Keep track of which point has the smallest largest distance.
# Return a list [[x, y], [x, y]] of these minimum points.
#
def find_minimum_set(tree, max_phones, points):
    #Set the two arrays as arbitrarily the first check
    n = points[0]
    print("The point first is", n)
    print("Points:", n[0], n[1])

    # 2D array [[node, dist], [node, dist]]
    min_set_nodes = tree.search_knn(n, max_phones)
    # 2D array [[x, y], [x, y]]
    min_set_points = pull_all_coordinates(min_set_nodes)

    i = 1
    while i < len(points):
        curr_pt = points[i]
        curr_nn_nodes = tree.search_knn(curr_pt, max_phones)

        # if the last distance in this point, is less than the current minimum last distance
        if curr_nn_nodes[len(curr_nn_nodes) - 1][1] < min_set_nodes[len(curr_nn_nodes) - 1][1]:
            # Copy all of these points and set them as the current min
            min_set_points = pull_all_coordinates(curr_nn_nodes)
            min_set_nodes = curr_nn_nodes
        i+=1

    #print("MINIMUM SET OF THE NODES:", min_set_nodes, sep="\n")
    return min_set_points

#
# Takes a set of points and turns them into the smallest enclosing circle.
#
def find_smallest_circle(points):
    '''
    megiddo algorithm:
    welzl algoirthm:
    algorithm welzl: #PSEUDO CODE FROM WIKIPEDIA
    
    input: Finite sets P and R of points in the plane
    output: Minimal disk enclosing P with R on the boundary, or undefined if no such disk exists
    
    if P is empty or |R| ≥ 3:
        if the points of R are cocircular:
            return the ball they determine
        else:
            return undefined

    choose p in P (randomly and uniformly)
    D := welzl(P - { p }, R)
    if p is in D:
        return D
    return welzl(P - { p }, R ∪ { p })
    '''
    range = 0

    return range

#
# Main method runs all the input and methods called.
#
def main():
    #Make a list of point lists
    points = []
    max_phones = 12

    #Loop until no further input, adding in each point
    while (True):
        try:
            inp = input()
        except EOFError:
            break
        if inp == "Telephone sites":
            continue
        else:
            ps = inp.split(" ")
            points.append(ps)

    #Print out all the points in the 2D list
    for p in points:
        x = p[0]
        y = p[1]
        #print("East:", y, "and North:", x)

    #print(points)

    # If there aren't enough points, abort the check
    if len(points) < max_phones:
        print("Range is infinite! There are less than the maximum", max_phones, " phones.")
        sys.exit(0)

    tree = kdtree.create(points)
    #kdtree.visualize(tree)
    #inord_tree = list(tree.inorder())
    #print(inord_tree)

    #print_if_balanced(tree)
    pt = [125.13,122.56]
    nn_node = tree.search_nn(pt)
    print("Nearest Neighbour is:\n", nn_node, sep="")
    minimum_nn_points = find_minimum_set(tree, max_phones, points)
    print("\nThe minimum points OF EVERYTHING found:", minimum_nn_points, sep="\n")

    #answer = find_smallest_circle(minimum_nn_points)
    #print("Range found:", answer)

    copy = minimum_nn_points[:]

    #circle = smallestcircle()
    c = smallestcircle.make_circle(copy)
    print("Range found\nx:", c[0], "y:", c[1], "r:", c[2])

    # Reduce by some arbitrarily small amount to go from min of 12 to max of at most 11
    r = c[2]
    true_r = (r - 0.1)
    print("New radius found! Radius:", true_r)



if __name__ == '__main__':
    main()

