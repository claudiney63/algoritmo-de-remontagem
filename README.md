# Projeto de Geração de K-mers e Montagem de Sequências com Grafos de Bruijn

 A reconstrução de strings no contexto de k-mers é um problema comum na bioinformática, especialmente na análise de sequências de DNA. Ele envolve reconstruir uma sequência original a partir de fragmentos conhecidos como k-mers.

 Este projeto contém duas funcionalidades principais:
 - Geração de k-mers a partir de uma sequência
 - Montagem de sequências a partir de k-mers utilizando grafos de Bruijn

 ## Uso
1. Geração de k-mers
O arquivo generate_kmers.py é responsável por gerar k-mers a partir de uma sequência fornecida.

### Estrutura do Arquivo de Entrada
O arquivo de entrada (generate-kmers-input.txt) deve conter a sequência na primeira linha e o valor de k na segunda linha. Exemplo:
```
AGGCATGCG
3
```

O arquivo de saída (generate-kmers-output.txt) conterá os k-mers gerados, separados por vírgulas.

2. Montagem de Sequências com Grafos de Bruijn
O arquivo assembler.py é responsável por montar a sequência original a partir dos k-mers utilizando grafos de Bruijn.

### Estrutura do Arquivo de Entrada
O arquivo de entrada (generate-kmers-output.txt) deve conter os k-mers gerados, separados por vírgulas. Exemplo:
```
AGGCA,ATGCG,CATGC,GCATG,GGCAT
```

O arquivo de saída (ClaudineySilva.txt) conterá a sequência montada.

 ![image](https://github.com/claudiney63/algoritmo-de-remontagem/assets/40923082/6ace394c-d8a0-4f6c-b928-9af6b676b23a)
