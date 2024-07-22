from collections import defaultdict, deque

def read_kmers(input_file):
    with open(input_file, 'r') as file:
        kmers = file.readline().strip().split(',')
    kmers = [kmer for kmer in kmers if kmer]
    return kmers

def bruijn_graph(kmers):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
        out_degree[prefix] += 1
        in_degree[suffix] += 1
    
    return graph, in_degree, out_degree

def find_eulerian_path(graph, in_degree, out_degree):
    start_node = None
    end_node = None
    
    for node in graph:
        if out_degree[node] - in_degree[node] == 1:
            start_node = node
        elif in_degree[node] - out_degree[node] == 1:
            end_node = node

    if not start_node:
        start_node = list(graph.keys())[0]
    
    stack = [start_node]
    path = deque()

    while stack:
        current_node = stack[-1]
        if graph[current_node]:
            next_node = graph[current_node].pop()
            stack.append(next_node)
        else:
            path.appendleft(stack.pop())
    
    return list(path)

def assemble_sequence_from_path(path):
    sequence = path[0]
    for node in path[1:]:
        sequence += node[-1]
    return sequence

def write_sequence_to_file(sequence, output_file):
    with open(output_file, 'w') as file:
        file.write(sequence)

# Exemplo de uso:
input_file = "kmers.txt"
output_file = "ClaudineySilva.txt"
kmers = read_kmers(input_file)

graph, in_degree, out_degree = bruijn_graph(kmers)
eulerian_path = find_eulerian_path(graph, in_degree, out_degree)
sequence = assemble_sequence_from_path(eulerian_path)

write_sequence_to_file(sequence, output_file)
