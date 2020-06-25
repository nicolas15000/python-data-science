""" 
Introduction 


On a 3 documents 

On veut calculer

1. La fréquence des termes tf(t,d)=nt,d

2. L'idf

3. la similarité cosinus.



Sources 

http://b3d.bdpedia.fr/

https://medium.com/@imamun/creating-a-tf-idf-in-python-e43f05e4d424

 """



# 1. On importe les librairies .

import pandas as pd
import sklearn as sk
#(seulement pour l'idf)
import math 


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



# 3. on sépare les mots dans chaque fichier en se basant sur le caractère d'espacement, et on en crée une liste. 
docA = docA.read()
docA = docA.split(" ")
docA = list(map(lambda x:x.lower(),docA))
print(docA)

docB = docB.read()
docB = docB.split(" ")
docB = list(map(lambda x:x.lower(),docB))
print(docB)

docC = docC.read()
docC = docC.split(" ")
docC =list(map(lambda x:x.lower(),docC))
print(docC)

docD = docD.read()
docD = docD.split(" ")
docD = list(map(lambda x:x.lower(),docD ))
print(docD)





""" --------------------------------------------------------------------------------------------------
1. La fréquence des termes tf(t,d)=nt,d
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
 L'IDF'
-------------------------------------------------------------------------------------------------- """