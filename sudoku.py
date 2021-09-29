#Lab 5
#Problem 1
def convert(string):
    '''converts a string of 81 digits into
    a one dimensional array of 81 numbers'''
    return [int(i) for i in string]

num = "400870020080000400006300801700100080612098734000060019193427500807010302020003000"
numbers = convert(num)
print(numbers)



#Problem 2
def entry(a, b, grid):
    '''returns the (a, b) entry
    of the Sudoku grid'''
    x = 9 * (a - 1) + b - 1
    return grid[x]

print(entry(5, 3, numbers))



# Problem 3
def ispossible(a, b, n, grid):
    '''returns True if n is a possible value for the (a, b) entry
    of grid, and False otherwise'''
    for i in range(1,10):
        if b != i and n == entry(a, i, grid):
            return False
        if a != i and n == entry(i, b, grid):
            return False
    a_lower_limit = (a-1)//3*3+1
    b_lower_limit = (b-1)//3*3+1
    for k in range(a_lower_limit, a_lower_limit + 3):
        for l in range(b_lower_limit, b_lower_limit + 3):
            if (a != k or b != l) and n == entry(k, l, grid):
                return False

    return True

print(ispossible(5, 4, 5, numbers))
print(ispossible(7, 2, 4, numbers))



#Problem 4
def computepossibilities(a, b, grid):
    '''returns a list of all possible n for which
    ispossible(a, b, n, grid) is True'''
    inputs = []
    for i in range(1, 10):
        if ispossible(a, b, i, grid) == True:
            inputs.append(i)
    return inputs

print(computepossibilities(5, 4, numbers))
print(computepossibilities(9, 3, numbers))



#Problem 5
def insert(a, b, n, grid):
    '''sets the (a, b) entry of the grid to the number n'''
    grid1 = grid
    if entry(a, b, grid1) != 0:
        return False
    elif n not in computepossibilities(a, b, grid1):
        return False
    else:
        index = 9 * (a - 1) + b - 1
        grid1[index] = n
    return True



#Problem 6
def singletons(grid):
    '''checks each of the entries of the grid: if the entry
    is empty and has only one possible value, fill it in
    with the only possible value; if there are no such entries,
    return False'''
    grid2 = grid
    changed = False #create a boolean variable
    for a in range(1, 10):
        for b in range(1, 10):
            p = computepossibilities(a, b, grid2)
            if len(p) == 1 and entry(a, b, grid2) == 0:
                i = 9 * (a - 1) + b - 1
                grid2[i] = p[0]
                changed = True #don't return True/False, otherwise the loops ends after examining the first entry
    return changed



#Problem 7
def simplesolve(grid):
    '''runs singletons(grid) until False is returned'''
    while singletons(grid) == True:
        singletons(grid)
    return grid

print(simplesolve(numbers))



#Lab 7
#Problem 1
def issolved(grid):
    '''checks to see if a sudoku grid is completely filled out'''
    for i in grid:
        if i == 0:
            return False
    return True

print(issolved(simplesolve(numbers)))

#Problem 2
def issolvable(grid):
    '''checks to see if every entry that has not been filled out
    still has values that could possibly be put into it'''
    for a in range(1, 10):
        for b in range(1, 10):
            if entry(a, b, grid) == 0:
                if len(computepossibilities(a, b, grid)) == 0:
                    return False
    return True

print(issolvable(numbers))

#Problem 3
def solve(grid):
    grid1 = simplesolve(grid)
    if issolved(grid1) == True:
        return grid1
    if issolvable(grid1) == False:
        return False
    #u = 0
    #v = 0
    for a in range(1, 10):
        for b in range(1, 10):
            if entry(a, b, grid1) == 0:
                #u = a
                #v = b
                possibilities = computepossibilities(a, b, grid1)
                for p in possibilities:
                    grid2 = grid1.copy()
                    insert(a, b, p, grid2)
                    if issolvable(grid2) == True:
                        grid2 = solve(grid2)
                        if grid2 != False:
                            return grid2
                return False

print(solve(convert("708000300000201000500000000040000026300080000000100090090600004000070500000000000")))
