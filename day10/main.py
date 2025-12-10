with open("input.txt") as f:
    ls = f.read().strip().split("\n")

tasks = []
for l in ls:
    toggles, *buttons, counters = l.split()
    toggles = [x == "#" for x in toggles[1:-1]]
    moves = [set(map(int, b[1:-1].split(","))) for b in buttons]
    counters = list(map(int, counters[1:-1].split(",")))
    tasks.append((toggles, moves, counters))

def press_button(state: tuple[bool, ...], button: set[int]) -> tuple[bool, ...]:
    return tuple(not v if i in button else v for i, v in enumerate(state))

def bidirectional_bfs(initial: tuple[bool, ...], target: tuple[bool, ...], buttons: list[set[int]]) -> int:
    if initial == target:
        return 0
    
    forward = {initial: 0}
    backward = {target: 0}
    
    forward_queue = [initial]
    backward_queue = [target]
    
    while forward_queue or backward_queue:
        if forward_queue:
            new_forward_queue = []
            for state in forward_queue:
                dist = forward[state]
                for button in buttons:
                    new_state = press_button(state, button)
                    
                    if new_state in backward:
                        return dist + 1 + backward[new_state]
                    
                    if new_state not in forward:
                        forward[new_state] = dist + 1
                        new_forward_queue.append(new_state)
            
            forward_queue = new_forward_queue
        
        if backward_queue:
            new_backward_queue = []
            for state in backward_queue:
                dist = backward[state]
                for button in buttons:
                    new_state = press_button(state, button)
                    
                    if new_state in forward:
                        return forward[new_state] + dist + 1
                    
                    if new_state not in backward:
                        backward[new_state] = dist + 1
                        new_backward_queue.append(new_state)
            
            backward_queue = new_backward_queue
    
    return -1

part1 = sum(
    bidirectional_bfs(
        tuple([False] * len(toggles)),
        tuple(toggles),
        moves
    ) for toggles, moves, counters in tasks
)

print(f"part1: {part1}")