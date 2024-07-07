from collections import defaultdict, deque

def read_kmers(filename):
    with open(filename, 'r') as file:
        kmers = [line.strip() for line in file.readlines()]
    return kmers

def build_de_bruijn_graph(kmers):
    graph = defaultdict(list)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
    return graph

def find_eulerian_path(graph):
    def find_start_node(graph):
        in_degrees = defaultdict(int)
        out_degrees = defaultdict(int)
        
        for node in graph:
            out_degrees[node] = len(graph[node])
            for neighbor in graph[node]:
                in_degrees[neighbor] += 1
        
        start = None
        for node in out_degrees:
            if out_degrees[node] - in_degrees[node] == 1:
                start = node
                break
            elif out_degrees[node] > 0:
                start = node
                
        return start
    
    def dfs(graph, start):
        stack = [start]
        path = deque()
        while stack:
            u = stack[-1]
            if u in graph and graph[u]:
                stack.append(graph[u].pop())
            else:
                path.appendleft(stack.pop())
        return list(path)
    
    start_node = find_start_node(graph)
    return dfs(graph, start_node)

def assemble_genome(path):
    genome = path[0]
    for kmer in path[1:]:
        genome += kmer[-1]
    return genome

def write_output(genome, filename='output.txt'):
    with open(filename, 'w') as file:
        file.write(genome)

def main(input_file):
    kmers = read_kmers(input_file)
    graph = build_de_bruijn_graph(kmers)
    path = find_eulerian_path(graph)
    genome = assemble_genome(path)
    write_output(genome)

input_file = 'input.txt'  
main(input_file)
