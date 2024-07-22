def read_kmers_from_file(input_file):
    with open(input_file, 'r') as file:
        kmers = file.readline().strip().split(',')
    # Remover qualquer k-mer vazio resultante de uma vírgula no final
    kmers = [kmer for kmer in kmers if kmer]
    return kmers

def assemble_sequence(kmers):
    sequence = kmers[0]
    k = len(kmers[0])
    for i in range(1, len(kmers)):
        sequence += kmers[i][-1]
    return sequence

def write_sequence_to_file(sequence, output_file):
    with open(output_file, 'w') as file:
        file.write(sequence)

# Exemplo de uso:
input_file = "kmers.txt"
output_file = "ClaudineySilva.txt"
kmers = read_kmers_from_file(input_file)
sequence = assemble_sequence(kmers)
write_sequence_to_file(sequence, output_file)
