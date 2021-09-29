#Problem 1

def all_sums(string):

    if len(string) == 2:
        return [int(string)]

    lines = string.split('\n')
    top = int(string[:2])
    lines2 = string.split('\n')
    '''a list of individual rows as strings'''

    lines.remove(lines[0])
    lines2.remove(lines2[0])
    lines = [s[3:] for s in lines]
    lines2 = [s[:-3] for s in lines2]
    lines = '\n'.join(lines)
    lines2 = '\n'.join(lines2)

    sums1 = all_sums(lines)
    sums1 = [i + top for i in sums1]
    sums2 = all_sums(lines2)
    sums2 = [i + top for i in sums2]

    for i in sums2:
        if i not in sums1:
            sums1.append(i)

    sums1.sort()
    return sums1

print(all_sums('''19
41 30
28 39 62
96 42 43 19
56 31 09 14 22
81 87 72 25 44 98
08 40 15 08 49 98 27
69 02 23 79 26 34 67 41
72 57 06 29 63 39 57 58 76
64 11 39 82 97 61 83 82 53 97'''))

#Problem 2
def max_path(string):
    lines = string.split('\n')
    str_grid = [line.split(' ') for line in lines]
    grid = [[int(entry) for entry in line] for line in str_grid]
    grid = list(reversed(grid))

    for i in range(len(grid)-1):
        for j in range(len(grid[i])-1):
            grid[i+1][j] += max(grid[i][j], grid[i][j+1])
    return grid[-1][0]

print(max_path('''19
41 30
28 39 62
96 42 43 19
56 31 09 14 22
81 87 72 25 44 98
08 40 15 08 49 98 27
69 02 23 79 26 34 67 41
72 57 06 29 63 39 57 58 76
64 11 39 82 97 61 83 82 53 97'''))

#Problem 3
def max_path_rect(string):
    lines = string.split('\n')
    str_grid = [line.split(' ') for line in lines]
    grid = [[int(entry) for entry in line] for line in str_grid]

    sums_row = grid[0]
    i = 1
    while i < len(sums_row):
        sums_row[i] += sums_row[i-1]
        i += 1
    for i in range(1, len(grid)):
        sums_row1 = grid[i]
        sums_row1[0] += sums_row[0]
        j = 1
        while j < len(sums_row1):
            sums_row1[j] += max(sums_row1[j-1], sums_row[j])
            j += 1
        sums_row = sums_row1
    return sums_row[-1]


print(max_path_rect('''11 17 46 78 73 22 82 91 37 90
59 19 47 80 26 24 15 26 74 44
63 92 71 35 95 75 17 53 06 62
54 29 53 67 35 71 97 63 95 68
03 20 23 82 33 15 90 42 77 05
77 62 15 93 80 16 58 75 21 07
80 90 65 97 74 98 85 13 16 03
87 16 79 33 37 08 85 82 21 91
78 27 42 18 79 04 63 27 13 94
18 83 81 45 40 93 76 76 61 83'''))
print(max_path_rect('''87 86 71 78 69 29 62 07 84 26 02 31 52 85 50 48 23 10 72 76
03 71 40 46 72 41 34 84 39 65 27 57 15 01 04 96 83 72 99 55
30 42 37 92 55 58 31 06 47 50 83 58 29 96 45 71 75 35 23 42
11 84 73 86 39 35 44 55 98 56 86 64 02 90 88 61 63 19 42 74
23 28 69 22 68 15 58 73 49 59 22 12 24 22 10 60 53 23 16 65
83 90 15 59 38 83 83 59 93 73 27 84 71 21 12 15 93 98 90 68
69 83 70 22 15 93 13 82 87 89 76 58 95 49 37 26 67 42 82 01
44 89 72 56 87 28 67 79 94 23 18 19 21 04 10 14 91 98 92 44
85 72 83 29 91 73 45 13 90 88 52 92 32 09 87 47 55 91 75 07
08 79 05 09 21 15 10 86 91 99 41 70 18 85 18 73 05 11 57 66
29 77 72 89 81 77 20 41 26 22 93 90 17 78 17 52 08 99 93 65
59 82 67 34 89 46 79 62 51 59 34 93 82 06 75 72 51 12 41 58
31 83 10 63 17 84 17 32 81 19 24 36 32 40 19 82 94 84 63 17
15 90 40 56 34 40 54 19 41 70 99 73 13 61 73 12 16 91 47 87
70 54 85 48 17 46 39 72 30 21 35 61 35 31 01 39 96 46 85 60
45 30 24 55 95 35 01 98 27 30 39 68 83 74 47 70 27 96 88 17
84 26 70 95 86 61 63 02 33 86 17 63 36 83 40 52 39 51 10 44
44 85 53 80 68 59 58 77 99 12 13 36 48 34 81 59 42 93 05 97
19 06 56 02 72 83 39 93 60 15 71 22 16 30 27 02 75 34 08 97
95 46 54 96 52 94 11 92 98 26 94 84 21 33 74 95 37 32 95 46'''))
