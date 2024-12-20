import heapq
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10000)

graph = defaultdict(dict)
seen = set()


def main():
    global graph, seen

    map, start_pos, end_pos = read_file('input.txt')
    start_dir = 'east'

    build_graph(map, (start_pos, start_dir), start_pos, end_pos)

    distances, paths, min_distance = dijkstra((start_pos, start_dir), end_pos)

    positions_on_shortest_paths = set()
    for path in paths:
        for pos, dir in path:
            positions_on_shortest_paths.add(pos)

    print(f'The answer: {len(positions_on_shortest_paths)}')


def build_graph(map, pos_dir, start, end):
    global graph, seen

    if pos_dir in seen:
        return

    seen.add(pos_dir)

    for neighbour in get_neighbours(pos_dir, map):
        graph[pos_dir][neighbour] = get_distance(pos_dir, neighbour)
        build_graph(map, neighbour, start, end)


def get_distance(pos_dir1, pos_dir2):
    if pos_dir1[0] == pos_dir2[0]:
        return 1000
    return 1


# ChatGPT implemented Dijkstra for me
# I did it before, but felt lazy
def dijkstra(start_pos_dir, end_pos):
    global graph

    priority_queue = [(0, start_pos_dir)]
    distances = {node: float('inf') for node in graph}
    distances[start_pos_dir] = 0
    previous_nodes = defaultdict(list)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = [current_node]
                heapq.heappush(priority_queue, (distance, neighbor))

            elif distance == distances[neighbor]:
                previous_nodes[neighbor].append(current_node)


    min_distance = 1000000000000000000
    for end_dir in dirs():
        if (end_pos, end_dir) in distances.keys():
            min_distance = min(min_distance, distances[(end_pos, end_dir)])

    paths = []
    for end_dir in dirs():
        if (end_pos, end_dir) in distances.keys():
            end_pos_dir = (end_pos, end_dir)
            if distances[end_pos_dir] == min_distance:
                paths += reconstruct_paths(previous_nodes, start_pos_dir, end_pos_dir)

    return distances, paths, min_distance


# ChatGPT also did this for me: reconstruct all possible shortest paths
def reconstruct_paths(previous_nodes, start, end_pos_dir):
    paths = []
    queue = deque([[end_pos_dir]])

    while queue:
        path = queue.popleft()
        current_node = path[0]

        if current_node == start:
            paths.append(path)
        else:
            for prev in previous_nodes[current_node]:
                new_path = [prev] + path
                queue.append(new_path)

    return [path for path in paths if path[0] == start]


def get_neighbours(pos_dir, map):
    pos, dir = pos_dir
    neighbours = []

    for neighbour_dir in dirs():
        if neighbour_dir not in [dir, get_opposite(dir)]:
                    neighbours.append((pos, neighbour_dir))

    if dir == 'north':
        next_pos = (pos[0] - 1, pos[1])
    elif dir == 'south':
        next_pos = (pos[0] + 1, pos[1])
    elif dir == 'west':
        next_pos = (pos[0], pos[1] - 1)
    else:  # east
        next_pos = (pos[0], pos[1] + 1)

    if map[next_pos[0]][next_pos[1]] != '#':
        neighbours.append((next_pos, dir))

    return neighbours

def dirs():
    return ['north', 'south', 'east', 'west']

def get_opposite(dir):
    opposites = {
        'north': 'south',
        'south': 'north',
        'east': 'west',
        'west': 'east'
    }

    return opposites[dir]


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    start = end = None
    map = []
    for y, line in enumerate(lines):
        map.append(line.strip())
        if 'S' in line:
            start = (y, line.index('S'))
        elif 'E' in line:
            end = (y, line.index('E'))

    return map, start, end


if __name__ == "__main__":
    main()
