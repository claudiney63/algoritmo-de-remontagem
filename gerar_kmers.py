class KmerGenerator:
    def __init__(self, sequencia, k):
        self.sequencia = sequencia
        self.k = k

    def gerar_kmers(self):
        """Gera todos os k-mers de uma sequência e os retorna como uma string separada por vírgulas."""
        kmers = [self.sequencia[i:i+self.k] for i in range(len(self.sequencia) - self.k + 1)]
        kmers.sort()
        return ','.join(kmers)

class KmerFileHandler:
    def __init__(self, arquivo_entrada, arquivo_saida):
        self.arquivo_entrada = arquivo_entrada
        self.arquivo_saida = arquivo_saida

    def ler_sequencia_e_k(self):
        """Lê a sequência e o valor de k de um arquivo de entrada."""
        with open(self.arquivo_entrada, 'r') as arquivo:
            linhas = arquivo.readlines()
            sequencia = linhas[0].strip()
            k = int(linhas[1].strip())
            return sequencia, k

    def escrever_kmers_no_arquivo(self, kmers):
        """Escreve os k-mers em um arquivo de saída."""
        with open(self.arquivo_saida, 'w') as arquivo:
            arquivo.write(kmers)

    def processar(self):
        sequencia, k = self.ler_sequencia_e_k()
        gerador = KmerGenerator(sequencia, k)
        kmers = gerador.gerar_kmers()
        self.escrever_kmers_no_arquivo(kmers)

# Exemplo de uso:
arquivo_entrada = "generate-kmers-input.txt" # Arquivo de entrada com a sequência e o valor de k
arquivo_saida = "generate-kmers-output.txt" # Arquivo de saída com os k-mers separados por vírgula

processador = KmerFileHandler(arquivo_entrada, arquivo_saida)
processador.processar()
