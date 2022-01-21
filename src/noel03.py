with open('noel03data.txt') as file:
    horizontal_position = 0
    depth = 0
    data = file.readlines()
    for d in data :
        action = d.split()
        if action[0] == 'down':
            depth += int(action[1])
        elif action[0] == 'up':
            depth -= int(action[1])
        elif action[0] == 'forward':
            horizontal_position += int(action[1])
print(horizontal_position*depth)

