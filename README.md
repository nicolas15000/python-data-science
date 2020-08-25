# PYTHON DATA SCIENCE SCRIPTS EN FRANCAIS
<b>CAS D'UTILISATIONS .</b>
<br>
![Screenshot](iconb.jpg)<br>
<b>English</b><br>
Some ordered python regressions and linear solvers studies scripts, some are mine, others are from various authors and translated into french <br><br>
My wish is to call theses scripts from my node vue starter, later, with a Flask server.<br>

Thanks to this nice book : 
https://www.amazon.fr/Python-Data-Science-Dummies-Mueller/dp/1119547628
<br>
And <br>
Python Data Science Handbook<br>
https://jakevdp.github.io/PythonDataScienceHandbook/


<br>
Files with the C letter at the start of their names have confirmed status. <br>
Files with the KO letters at the beginning of their names have a result to check or fail.
<br> <br>

<b>Français/French</b><br>
Je stocke ici des scripts de data science et de mathématiques descriptives ou prédictives en Python.<br>
L'objectif de ce repos est de constituer au fil des années une "boite à outil" fiable et pratique de trames, en data science Python, afin de traiter un bon nombre de problèmes.
<br><br>
<b>Les scripts possédant la lettre C au début de leur noms ont un statut confirmé.</b><br>
<b>Les scripts possédant l'attribut BASE au début de leurs noms sont les plus simples et fiables.</b><br>
<b>Les scripts possédant la lettre KO au début de leurs noms ont un statut à vérifier ou en défaut.</b>
<br>
(Note : Confirmé, veut dire résultat bon, confirmé par comparaison, cependant, la méthode/stratégie pour obtenir le resultat n'est pas forcément encore la meilleure.)</br>
<br>

Je vais en ajouter un paquet au fil du temps, en particulier, de l'import CSV avec de l'utilisation de solveurs linéaires .<br>
L'idée étant de pouvoir résoudre un certain nombre de problèmes génériques, de les confirmer par comparaisons de résultats ( Par exemple, comparaison Excel solveur / Python Pulp), puis de pouvoir les dériver/adapter un peu avec N variables de décision pour les solveurs linéaires, par exemple. Certains scripts sont de moi, d'autres proviennent d'auteurs internet ou de livres.

<b>Librairies utilisées</b>
* numpy<br>
* matplotlib<br>
* pandas<br>
* scipy<br>
* sklearn<br>
* pulp (Solvers)<br>
* pyschedule https://github.com/timnon/pyschedule<br>
* Survival regression https://lifelines.readthedocs.io/en/latest/Survival%20Regression.html#the-dataset-for-regression <br><br>

<b>Datasets et notebooks à télécharger sur Kaggle ! </b><br>
https://www.kaggle.com/notebooks<br><br>

<b>Liens et références</b><br>
Merci au livre https://www.eyrolles.com/Informatique/Livre/programmation-lineaire-avec-excel-9782212126594/<br>
qui récapitule bien les principaux problèmes rencontrés avec le solveur. Je voudrais les transcrire en Python dès que possible ...Le problème étant que les modèles dans ce livre traitent souvent de plusieurs matériels en même temps ( exemple : Génération de 2 alliages en même temps, sous 4 contraintes divergentes ) , c'est assez difficile à retranscrire pour l'instant pour moi, je suis dessus. Normalement, à partir du moment ou le modèle mathématique est correct, on doit pouvoir entrer le P.L avec tous les solveurs ..<br>

Egalement le livre : <br>
https://www.springer.com/gp/book/9782287302787<br>
Conseillé pour l'UE STA001 du Cnam.<br>

Le site d'un professeur de l'ENSAE:<br>
http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a.html#machine-learning-les-briques-de-bases<br>

<b>Les Chaines Youtube Françaises:</b><br>
Machine Learnia https://www.youtube.com/channel/UCmpptkXu8iIFe6kfDK5o7VQ<br>
Clipedia : https://www.youtube.com/channel/UCNwWU1hqK3q-DclufllWCfg<br>
ProMath : https://www.youtube.com/channel/UC2flwAftkypBx2gLIamxwqg<br>
Nicolas Br https://www.youtube.com/channel/UCzsU0h6kxkSSCqpXTRUHubg<br>
Yvan Monka : https://www.youtube.com/user/YMONKA<br>
Saïd Chermak : https://www.youtube.com/channel/UCppNXkk1sgDguxe8fQK9tng<br>
Science4All : https://www.youtube.com/watch?v=Jf40Xd52NyQ

<br>



<b>Liens et références (Suite)</b><br>
A regarder également le super dépot Columbia-Intro-Data-Science avec tout le travail d'étudiants de Columbia dans ce domaine avec Python.<br>

https://github.com/Columbia-Intro-Data-Science<br>

Les cours sont ici : <br>
https://github.com/Columbia-Intro-Data-Science/APMAE4990-/tree/master/notebooks<br>

Un autre dépot sympa :<br>
https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers<br>


<b>Ecoles : </b><br>
1. S'inscrire à l'université de Brest : http://formations.univ-brest.fr/fr/index.html
2. S'inscrire à l'inversité de Rennes : https://formations.univ-rennes1.fr/master-1-data-science
3. S'inscrire à l'EICNAM : http://ecole-ingenieur.cnam.fr/hors-temps-de-travail/inscription-a-l-eicnam/
4. S'inscrire à l'ENSAE : https://www.ensae.fr/auditeurs-libres/
5. S'inscrire à L'université de Bordeaux : http://www.math.u-bordeaux.fr/~mchave100p/teaching/ https://www.math.u-bordeaux.fr/imb/spip.php<br><br>
6. S'inscrire au D.U de Statistiques à Toulouse : https://www.ut-capitole.fr/formations/se-former-autrement/formation-ouverte-et-a-distance/diplome-universitaire-statistique-appliquee-formation-a-distance--326811.kjsp?RH=1319186952079

<b>Moocs :</b><br>
Coursera <br>
Programmer en Python pour la Data Science de A à Z :https://www.udemy.com/course/data-science-avec-python/<br>
Les Data Sciences de A à Z  : https://www.udemy.com/course/les-data-sciences-de-a-a-z/<br>
Spécialisation Science des données appliquée avec Python : https://fr.coursera.org/specializations/data-science-python<br>
Modélisation financière : https://www.coursera.org/specializations/finance-quantitative-modeling-analysts#courses<br><br>
real-data-science-problems : https://www.udemy.com/course/real-data-science-problems-with-python/<br>
Finances : https://www.my-mooc.com/fr/mooc/python-and-statistics-for-financial-analysis/<br>

Tous les cours de programmation linéaire : <br>
https://www.udemy.com/courses/search/?q=%22LINEAR%20PROGRAMMING%22&src=sac&kw=linear%20programmaing<br><br>

Moocs de Maths:<br>
https://www.fun-mooc.fr/courses/course-v1:MinesTelecom+04008+session06/about<br><br>

Moocs de sciences Physique : <br>
https://www.my-mooc.com/fr/categorie/physique<br><br>


<b> Collabs : </b><br>
Vous désirez collaborer avec moi (Surtout sur les solveurs linéaires ( Monde agricole, productions alimentaires, production et j'espère... finance)) ... Ok ! envoyez moi un message<br>
