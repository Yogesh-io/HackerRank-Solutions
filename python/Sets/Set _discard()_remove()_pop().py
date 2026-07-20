n = int(input().strip())

s = set(map(int, input().split()))

num_commands = int(input().strip())

for _ in range(num_commands):
    command_input = input().split()
    command_name = command_input[0]
    
    if command_name == "pop":
        s.pop()
    else:
        value = int(command_input[1])
        
        if command_name == "remove":
            s.remove(value)
        elif command_name == "discard":
            s.discard(value)

print(sum(s))
