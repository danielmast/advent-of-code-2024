import heapq
import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

graph = defaultdict(dict)
seen = set()


def main():
    global graph, seen

    map, start_pos, end_pos = read_file('input.txt')
    start_dir = 'east'

    build_graph(map, (start_pos, start_dir), start_pos, end_pos)

    answer = lowest_score(start_pos, start_dir, end_pos)
    print(f'The answer: {answer}')


def lowest_score(start_pos, start_dir, end_pos):
    global graph

    distances = dijkstra(graph, (start_pos, start_dir))
    answer = 1000000000000000000

    for dir in ['north', 'east', 'south', 'west']:
        if (end_pos, dir) in distances.keys():
            answer = min(answer, distances[(end_pos, dir)])

    return answer


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
def dijkstra(graph, start):
    priority_queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def get_neighbours(pos_dir, map):
    pos, dir = pos_dir
    neighbours = []

    for neighbour_dir in ['north', 'east', 'south', 'west']:
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
