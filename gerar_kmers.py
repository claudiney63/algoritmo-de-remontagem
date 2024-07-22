def generate_kmers(sequence, k):
    kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
    kmers.sort()
    return ','.join(kmers)

def write_kmers_to_file(sequence, k, output_file):
    kmers = generate_kmers(sequence, k)
    with open(output_file, 'w') as file:
        file.write(kmers)

# Exemplo de uso:
sequence = "AGGCATGCG"
k = 5
output_file = "kmers.txt"
write_kmers_to_file(sequence, k, output_file)
