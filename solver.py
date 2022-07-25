import string


f1 = open("puzzle1.txt", "r")
Lines1 = f1.readlines()
f1.close()
puzzle = []
for Line in Lines1:
    puzzle.append(''.join(Line.split()))
height = len(puzzle)
width = len(puzzle[0])

f2 = open("words_reduced.txt", "r")
Lines2 = f2.readlines()
f2.close()
Words = []
for Line in Lines2:
    Words.append(Line.strip())
    Words.append(Line.strip()[::-1])

for line in puzzle:
    for word in Words:
        if word in line:
            pass

flags =  [[False for i in range(width)] for j in range(height)]

strings_to_check = []
coordinates = [] #starting y, starting x, y increment, x increment

for i in range(height): #add horizontal strings from puzzle
    strings_to_check.append(puzzle[i])
    coordinates.append([i, 0, 0, 1])

for j in range(width): #add vertical strings from puzzle
    strings_to_check.append(''.join([line[j] for line in puzzle]) )
    coordinates.append([0, j, 1, 0])

for i in range (height): #add diagonal strings starting from the left and right
    NE, SE, NW, SW = [], [], [], []
    for j in range(i+1):
        NE.append(puzzle[i-j][j])
    strings_to_check.append(''.join(NE) )
    coordinates.append([i, 0, -1, 1])

    for j in range(height-i):
        SE.append(puzzle[i+j][j])
    strings_to_check.append(''.join(SE) )
    coordinates.append([i, 0, 1, 1])

    for j in range(i+1):
        NW.append(puzzle[i-j][width-j-1])
    strings_to_check.append(''.join(NW) )
    coordinates.append([i, width-1, -1, -1])

    for j in range(height-i):
        SW.append(puzzle[i+j][width-j-1])
    strings_to_check.append(''.join(SW) )
    coordinates.append([i, width-1, 1, -1])

count = 0
#print(flags)
for k in range(len(strings_to_check)):
    string = strings_to_check[k]
    for word in Words:
        if word in string:
            start = string.find(word)
            length = len(word)
            current = coordinates[k]
            y = current[0] + (start)*current[2]
            x = current[1] + (start)*current[3]
            flags[y][x] = 1
            for l in range(length):
                flags[ current[0] + (start+l)*current[2] ][ current[1] + (start+l)*current[3] ] = True
                pass
    
for i in range(height):
    for j in range(width):
        if not flags[i][j]:
            puzzle[i] = puzzle[i][:j] + puzzle[i][j].lower() + puzzle[i][j+1:]

f3 = open("solved1.txt", "w")
for Line in puzzle:
    f3.write(' '.join(Line) + "\n")
f3.close()