lista = ["A carteira colocou a carteira na carteira", "O carteiro nao tem carteira",
         "O carteiro comprou uma carteira nova"]
print("Lista: ", lista)

sentenca = " ".join(lista)
print("Sentença: " + sentenca)

palavras = sentenca.split()
vocabulario = (" ".join(sorted(set(palavras), key=palavras.index)))
print("Vocabulario: " + vocabulario)

tamanhoVocab = len(vocabulario.split())
print("Tamanho Vocabulario: ", tamanhoVocab)

vocab = vocabulario.split()


def vetorizar(numero):
    vetor = [0] * tamanhoVocab
    for i in lista[numero].split():
        index = vocab.index(i)
        # print("index do termo", i , ":", index)
        vetor[index] += 1
    return vetor


count = 0
while count < len(lista):
    print(vetorizar(count))
    count += 1
