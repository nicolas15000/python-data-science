""" 
Introduction 


On a 3 documents 

On veut calculer

1. La fréquence des termes dans chaque document tf(t,d)=nt,d avec t = terme et d = document et créer la matrice d'incidence .
La fréquence d’un terme t dans un document d est le nombre d’occurrences de t dans d . 
    1.1 Avec la lib skLearn
    1.2 Avec un code 

2. L'idf

3. la similarité cosinus.



Sources 

Eicnam Nfe 204

http://b3d.bdpedia.fr/

https://towardsdatascience.com/natural-language-processing-feature-engineering-using-tf-idf-e8b9d00e7e76

https://medium.com/@imamun/creating-a-tf-idf-in-python-e43f05e4d424

https://scikit-learn.org/stable/modules/feature_extraction.html

 """



# 1. On importe les librairies .

import pandas as pd
import sklearn as sk
#(seulement pour l'idf)
import math 


""" --------------------------------------------------------------------------------------------------
1. La fréquence des termes pour chaque document : tf(t,d)=nt,d avec t = terme et d = document .
1.1 Avec skLearn
-------------------------------------------------------------------------------------------------- """

# on importe la librairie

from sklearn.feature_extraction.text import CountVectorizer

# Premier exemple avec un tableau contnant des docs
vectorizer = CountVectorizer()
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]
X = vectorizer.fit_transform(corpus)

# Créer la matrice d'incidence , on voit qu'il y 2 fois le mot second dans le 2 ème doc
k = X.toarray()
print(k)
""" 
[[0 1 1 1 0 0 1 0 1]
 [0 1 0 1 0 2 1 0 1]
 [1 0 0 0 1 0 1 1 0]
 [0 1 1 1 0 0 1 0 1]] """

# Voir le dictionnaire créé pour comprendre la matrice d'incidence.
X = vectorizer.get_feature_names()
print(X)
# ['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this'] 



# Deuxième exemple avec les documents .txt pour source 

"""  
    A: Le loup est dans la bergerie.
    B: Les moutons sont dans la bergerie.
    C: Un loup a mangé un mouton, les autres loups sont restés dans la bergerie.
    D: Il y a trois moutons dans le pré, et un mouton dans la gueule du loup. 
"""

with open('datasets/A.txt', 'r', encoding="utf-8") as file:
    docA = file.read().replace('\n', '')
with open('datasets/B.txt', 'r', encoding="utf-8") as file:
    docB = file.read().replace('\n', '')
with open('datasets/C.txt', 'r', encoding="utf-8") as file:
    docC = file.read().replace('\n', '')
with open('datasets/D.txt', 'r', encoding="utf-8") as file:
    docD = file.read().replace('\n', '')

corpus = [docA,docB,docC,docD]
print(corpus)
X = vectorizer.fit_transform(corpus)

# Créer la matrice d'incidence , on voit qu dans le doc 4 il y a 2 fois le mot 'dans' dans le 4ème doc
k = X.toarray()
print(k)
""" 
[[0 1 1 0 1 0 0 0 1 1 0 1 0 0 0 0 0 0 0 0 0]
 [0 1 1 0 0 0 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0]
 [1 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 1 1 0 2]
 [0 0 2 1 0 1 1 1 1 1 0 1 0 0 1 1 1 0 0 1 1]]
 """
# Voir le dictionnaire créé pour comprendre la matrice d'incidence.
X = vectorizer.get_feature_names()
print ("Les mots présents dans mes 4 fichiers, sans doublons,  sont: ")
print(X)
# ['autres', 'bergerie', 'dans', 'du', 'est', 'et', 'gueule', 'il', 'la', 'le', 'les', 'loup', 'loups', 'mangé', 'mouton', 'moutons', 'pré', 'restés', 'sont', 'trois', 'un']


""" --------------------------------------------------------------------------------------------------
1. La fréquence des termes pour chaque document : tf(t,d)=nt,d avec t = terme et d = document .
1.2 Avec un code
-------------------------------------------------------------------------------------------------- """

# 2. On importe les 4 fichiers
# Voici le contenu des fichiers : 
"""  
    A: Le loup est dans la bergerie.
    B: Les moutons sont dans la bergerie.
    C: Un loup a mangé un mouton, les autres loups sont restés dans la bergerie.
    D: Il y a trois moutons dans le pré, et un mouton dans la gueule du loup. 
"""

docA = open("datasets/A.txt", "r", encoding="utf-8-sig")
docB = open("datasets/B.txt", "r", encoding="utf-8-sig")
docC = open("datasets/C.txt", "r", encoding="utf-8-sig")
docD = open("datasets/D.txt", "r", encoding="utf-8-sig")



# 3. on sépare les mots dans chaque fichier en se basant sur le caractère d'espacement, et on en crée une liste BAG OF WORDS. 

docA = docA.read()
docA = docA.split(" ")
# On passe chaque mot en minuscule
docA = list(map(lambda x:x.lower(),docA))
print(docA)

docB = docB.read()
docB = docB.split(" ")
# On passe chaque mot en minuscule
docB = list(map(lambda x:x.lower(),docB))
print(docB)

docC = docC.read()
docC = docC.split(" ")
# On passe chaque mot en minuscule
docC =list(map(lambda x:x.lower(),docC))
print(docC)

docD = docD.read()
docD = docD.split(" ")
# On passe chaque mot en minuscule
docD = list(map(lambda x:x.lower(),docD ))
print(docD)





""" --------------------------------------------------------------------------------------------------
1. La fréquence des termes pour chaque document : tf(t,d)=nt,d avec t = terme et d = document .
1.1 Avec des boucles
-------------------------------------------------------------------------------------------------- """

""" 4. 
ON se crée une liste "total" de tous les mots compris dans les 4 documents 
-> On joint les 4 documents ensemble et on enleve les mots dupliqués
 """
total= set(docA).union(set(docB)).union(set(docC)).union(set(docD))
print("Voici tous les mots trouvés dans les 4 documents, sans doublons : ")
print(total)


wordDictA = dict.fromkeys(total, 0) 
wordDictB = dict.fromkeys(total, 0)
wordDictC = dict.fromkeys(total, 0)
wordDictD = dict.fromkeys(total, 0)

# 5. On vérifie si les mots de la liste 'total' sont présents dans chaque document ou pas, si oui, on incrémente son compteur ++ .
for word in docA:
    wordDictA[word]+=1
    
for word in docB:
    wordDictB[word]+=1

for word in docC:
    wordDictC[word]+=1

for word in docD:
    wordDictD[word]+=1

# 6. On place le résultat dans un data frame pour voir le résultat.
resultat = pd.DataFrame([wordDictA, wordDictB,wordDictC,wordDictD])

print(resultat)

"""    
résultat : 
   moutons  a  dans  loup  sont  il  bergerie.  mangé  trois  pré,  gueule  loups  un  est  mouton,  autres  la  restés  et  y  les  du  le  loup.  mouton
0        0  0     1     1     0   0          1      0      0     0       0      0   0    1        0       0   1       0   0  0    0   0   1      0       0
1        1  0     1     0     1   0          1      0      0     0       0      0   0    0        0       0   1       0   0  0    1   0   0      0       0
2        0  1     1     1     1   0          1      1      0     0       0      1   2    0        1       1   1       1   0  0    1   0   0      0       0
3        1  1     2     0     0   1          0      0      1     1       1      0   1    0        0       0   1       0   1  1    0   1   1      1       1

 """










""" --------------------------------------------------------------------------------------------------
 L'IDF
-------------------------------------------------------------------------------------------------- """



from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print ("Le calcul des tfs sur mes 4 documents est : ")
print(X)
""" 
  (0, 1)        0.36968460723585306
  (0, 8)        0.3022413900957451
  (0, 2)        0.3022413900957451
  (0, 4)        0.5791823746292374
  (0, 11)       0.36968460723585306
  (0, 9)        0.4566340367193042
  (1, 18)       0.46975669212524207
  (1, 15)       0.46975669212524207
  (1, 10)       0.46975669212524207
  (1, 1)        0.38030852774885165
  (1, 8)        0.3109271412502876
  (1, 2)        0.3109271412502876
  (2, 17)       0.3209052503464512
  (2, 12)       0.3209052503464512
  (2, 0)        0.3209052503464512
  (2, 14)       0.25300538533121597
  (2, 13)       0.3209052503464512
  (2, 20)       0.5060107706624319
  (2, 18)       0.25300538533121597
  (2, 10)       0.25300538533121597
  (2, 1)        0.20482966442166697
  (2, 8)        0.1674616721819669
  (2, 2)        0.1674616721819669
  (2, 11)       0.20482966442166697
  (3, 3)        0.3122656795619237
  (3, 6)        0.3122656795619237
  (3, 5)        0.3122656795619237
  (3, 16)       0.3122656795619237
  (3, 19)       0.3122656795619237
  (3, 7)        0.3122656795619237
  (3, 14)       0.24619384848949769
  (3, 20)       0.24619384848949769
  (3, 15)       0.24619384848949769
  (3, 8)        0.162953185739475
  (3, 2)        0.32590637147895
  (3, 11)       0.19931513830334552
  (3, 9)        0.24619384848949769
 """

