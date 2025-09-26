coordinates = (0, 0, 0)

maxX = 10
maxY = 10
maxZ = 10

def in_bounds(coords):
    x, y, z = coords
    return 0 <= x <= maxX and 0 <= y <= maxY and 0 <= z <= maxZ

def move_rover(s, coordinates, obstacles):
    instruction = s.split()
    direction = instruction[0]
    units = int(instruction[1])
    moveDirection = (0, 0, 0)

    if direction == "up":
        moveDirection = (0, 0, 1)
    elif direction == "down":
        moveDirection = (0, 0, -1)
    if direction == "left":
        moveDirection = (0, 1, 0)
    elif direction == "right":
        moveDirection = (0, -1, 0)
    if direction == "forward":
        moveDirection = (1, 0, 0)
    elif direction == "backward":
        moveDirection = (-1, 0, 0)

    for i in range(units):
        next = tuple(x + y for x, y in zip(moveDirection, coordinates))
        if not in_bounds(next): 
            print("oops, you're going out of bounds here")
            print(f"Remaining here: {coordinates[0]} {coordinates[1]} {coordinates[2]}")
            break
        elif next in obstacles:
            print("oops, you're running into an obstacle")
            print(f"Remaining here: {coordinates[0]} {coordinates[1]} {coordinates[2]}")
            break

        coordinates = next
        print(f"Current coordinates: {coordinates[0]} {coordinates[1]} {coordinates[2]}")

    return coordinates



m = int(input()) # number of obstacles
obstacles = set()
for i in range(m):
    obstacle = input()
    x, y, z = map(int, obstacle.split())
    obstacles.add((x, y, z))

n = int(input()) # number of instructions
for i in range(n):
    s = input()
    coordinates = move_rover(s, coordinates, obstacles)
