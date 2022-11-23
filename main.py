import numpy as np
import nltk
import spacy
import requests
from bs4 import BeautifulSoup
nltk.download('punkt')
import re
import heapq
from numpy.linalg import norm
from collections import Counter
import pandas as pd
from nltk.tokenize import MWETokenizer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize

nlp=spacy.load("en_core_web_sm")
url = ["https://en.wikipedia.org/wiki/Natural_language_processing", "https://www.gyansetu.in/what-is-natural-language-processing/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8120048/", "https://languagelog.ldc.upenn.edu/nll/?p=2946", "https://www.fcg-net.org/"]
  
def texto(x):
  result = requests.get(x).text
  soup = BeautifulSoup(result, 'lxml')

  text = "".join([i.text for i in soup.find_all('p')])
  return text

def sentencas(text):
  return sent_tokenize(text)


def main():
  # lista = ["A carteira colocou a carteira na carteira", "O carteiro não tem carteira", "O carteiro comprou uma carteira nova"]
  lista = []
  for z in url:
    lista2 = sentencas(texto(z))
    lista += lista2
  

  corpus = " ".join(lista)
  z = nltk.sent_tokenize(corpus)
  vocab = vocabulario(corpus)
  listaTfidf = []
  contagem = []
  for x in lista:
    contagem2 = vetor(x, vocab)
    contagem.append(contagem2) 

  matrizSimilaridade(vocab, contagem)
    
  
def vocabulario(corpus):
  palavras = corpus.split()
  seen = set()
  result = []
  for item in palavras:
      if item not in seen:
          seen.add(item)
          result.append(item)

  # print("Vocabulario: ", result)
  # print(result)
  return result

def vetor(lista, vocabulario):
  contador = []

  tokenizer = MWETokenizer()
  result = tokenizer.tokenize(word_tokenize(lista))

  fdist = FreqDist(result)
  # print(fdist.keys())
  lista = list(fdist.keys())

  for x in vocabulario:
    contador.append(fdist[x])

  # print(f"Frequencia: {contador}")
  # print(contador)
  return contador

def matrizSimilaridade(vocabulario, frequencia):
  df = pd.DataFrame(columns= vocabulario, index=range(1, len(frequencia) + 1))
  # print(frequencia)
  for i in df.index:
    df.loc[i] = frequencia[i-1]

  display(df)


main()
