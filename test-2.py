# Les listes :
maListeDeMeubles = ['table','chaise','frigo']
maListeDeMeubles.sort()  #Tri de la liste
for unMeuble in maListeDeMeubles:
   print('longueur de la chaîne ', unMeuble, '=', len(unMeuble))

#les listes imbriquées:
laListeDesNombresPairs = [unNombre for unNombre in xrange(1000) if unNombre % 2 == 0]
print (laListeDesNombresPairs)

#Les dictionnaires :
unAnnuaire = {'Laurent': 6389565, 'Paul': 6356785}
for unNom, x in unAnnuaire.items():
   print("le nom %s a pour numéro de téléphone %d" %(unNom, x))


#Les tuples (n-uplet) : séquence constante
Couleur = ('Rouge', 'Bleu', 'Vert')
print(Couleur[0], Couleur[1],  Couleur[2])

PointDeReference = (100, 200)
print(" x0 = %d   y0 = %d "  %(PointDeReference[0],PointDeReference[1]))