from collections import defaultdict, deque

class DeBruijnGraph:
    def __init__(self):
        self.grafo = defaultdict(list)
        self.grau_entrada = defaultdict(int)
        self.grau_saida = defaultdict(int)

    def construir_grafo(self, kmers):
        """Constrói o grafo de Bruijn a partir dos k-mers."""
        for kmer in kmers:
            prefixo = kmer[:-1]
            sufixo = kmer[1:]
            self.grafo[prefixo].append(sufixo)
            self.grau_saida[prefixo] += 1
            self.grau_entrada[sufixo] += 1

    def encontrar_caminho_euleriano(self):
        """Encontra o caminho Euleriano no grafo de Bruijn."""
        no_inicio = None
        no_fim = None
        
        for no in self.grafo:
            if self.grau_saida[no] - self.grau_entrada[no] == 1:
                no_inicio = no
            elif self.grau_entrada[no] - self.grau_saida[no] == 1:
                no_fim = no

        if not no_inicio:
            no_inicio = list(self.grafo.keys())[0]
        
        pilha = [no_inicio]
        caminho = deque()

        while pilha:
            no_atual = pilha[-1]
            if self.grafo[no_atual]:
                proximo_no = self.grafo[no_atual].pop()
                pilha.append(proximo_no)
            else:
                caminho.appendleft(pilha.pop())
        
        return list(caminho)

class SequenciaAssembler:
    def __init__(self, arquivo_entrada, arquivo_saida):
        self.arquivo_entrada = arquivo_entrada
        self.arquivo_saida = arquivo_saida

    def ler_kmers(self):
        """Lê os k-mers de um arquivo de entrada."""
        with open(self.arquivo_entrada, 'r') as file:
            kmers = file.readline().strip().split(',')
        kmers = [kmer for kmer in kmers if kmer]
        return kmers

    def montar_sequencia_do_caminho(self, caminho):
        """Monta a sequência original a partir do caminho Euleriano."""
        sequencia = caminho[0]
        for no in caminho[1:]:
            sequencia += no[-1]
        return sequencia

    def escrever_sequencia_no_arquivo(self, sequencia):
        """Escreve a sequência montada em um arquivo de saída."""
        with open(self.arquivo_saida, 'w') as file:
            file.write(sequencia)

    def executar(self):
        kmers = self.ler_kmers()
        grafo = DeBruijnGraph()
        grafo.construir_grafo(kmers)
        caminho_euleriano = grafo.encontrar_caminho_euleriano()
        sequencia = self.montar_sequencia_do_caminho(caminho_euleriano)
        self.escrever_sequencia_no_arquivo(sequencia)

# Exemplo de uso:
arquivo_entrada = "output.txt" # Arquivo de entrada com os kmers separados por vírgula
arquivo_saida = "ClaudineySilva.txt"

assembler = SequenciaAssembler(arquivo_entrada, arquivo_saida)
assembler.executar()
