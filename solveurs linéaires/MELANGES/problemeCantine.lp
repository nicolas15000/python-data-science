\* Je_minimise *\
Minimize
OBJ: 0.45 aliment_Bananes + 0.48 aliment_Broccolis + 0.81 aliment_Bœuf
 + 0.09 aliment_Cookie_au_chocoloat + 0.27 aliment_Cookie_poire
 + 0.18 aliment_Haricots + 0.45 aliment_Jambon + 0.06 aliment_Laitue_Iceberg
 + 0.04 aliment_Mais + 0.15 aliment_Pain_blanc + 0.18 aliment_Pain_complet
 + 0.72 aliment_Pommes + 2.52 aliment_Poulet_grillé
 + 2.34 aliment_Spaghettis_en_sauce + 0.48 aliment_Tarte_aux_pommes
 + 0.93 aliment_Tofu + 0.33 aliment_Œufs_pochés
Subject To
_C1: 104.9 aliment_Bananes + 73.8 aliment_Broccolis + 141.8 aliment_Bœuf
 + 78.1 aliment_Cookie_au_chocoloat + 81 aliment_Cookie_poire
 + 171.5 aliment_Haricots + 56.4 aliment_Jambon + 2.6 aliment_Laitue_Iceberg
 + 72.2 aliment_Mais + 65 aliment_Pain_blanc + 65 aliment_Pain_complet
 + 81.4 aliment_Pommes + 277.4 aliment_Poulet_grillé
 + 358.2 aliment_Spaghettis_en_sauce + 67.2 aliment_Tarte_aux_pommes
 + 88.2 aliment_Tofu + 99.6 aliment_Œufs_pochés >= 800
_C2: 104.9 aliment_Bananes + 73.8 aliment_Broccolis + 141.8 aliment_Bœuf
 + 78.1 aliment_Cookie_au_chocoloat + 81 aliment_Cookie_poire
 + 171.5 aliment_Haricots + 56.4 aliment_Jambon + 2.6 aliment_Laitue_Iceberg
 + 72.2 aliment_Mais + 65 aliment_Pain_blanc + 65 aliment_Pain_complet
 + 81.4 aliment_Pommes + 277.4 aliment_Poulet_grillé
 + 358.2 aliment_Spaghettis_en_sauce + 67.2 aliment_Tarte_aux_pommes
 + 88.2 aliment_Tofu + 99.6 aliment_Œufs_pochés <= 2500
carbohydratesMaximum: 26.7 aliment_Bananes + 13.6 aliment_Broccolis
 + 0.8 aliment_Bœuf + 9.3 aliment_Cookie_au_chocoloat
 + 12.4 aliment_Cookie_poire + 39.9 aliment_Haricots + 0.3 aliment_Jambon
 + 0.4 aliment_Laitue_Iceberg + 17.1 aliment_Mais + 12.4 aliment_Pain_blanc
 + 11.8 aliment_Pain_complet + 21 aliment_Pommes
 + 58.3 aliment_Spaghettis_en_sauce + 9.6 aliment_Tarte_aux_pommes
 + 2.2 aliment_Tofu + 1.3 aliment_Œufs_pochés <= 200
carbohydratesMinimum: 26.7 aliment_Bananes + 13.6 aliment_Broccolis
 + 0.8 aliment_Bœuf + 9.3 aliment_Cookie_au_chocoloat
 + 12.4 aliment_Cookie_poire + 39.9 aliment_Haricots + 0.3 aliment_Jambon
 + 0.4 aliment_Laitue_Iceberg + 17.1 aliment_Mais + 12.4 aliment_Pain_blanc
 + 11.8 aliment_Pain_complet + 21 aliment_Pommes
 + 58.3 aliment_Spaghettis_en_sauce + 9.6 aliment_Tarte_aux_pommes
 + 2.2 aliment_Tofu + 1.3 aliment_Œufs_pochés >= 130
fibresMaximum: 2.7 aliment_Bananes + 8.5 aliment_Broccolis
 + 0.6 aliment_Cookie_poire + 3.2 aliment_Haricots
 + 0.3 aliment_Laitue_Iceberg + 2 aliment_Mais + 1.3 aliment_Pain_blanc
 + 1.1 aliment_Pain_complet + 3.7 aliment_Pommes
 + 11.6 aliment_Spaghettis_en_sauce + 0.5 aliment_Tarte_aux_pommes
 + 1.4 aliment_Tofu <= 150
fibresMinimum: 2.7 aliment_Bananes + 8.5 aliment_Broccolis
 + 0.6 aliment_Cookie_poire + 3.2 aliment_Haricots
 + 0.3 aliment_Laitue_Iceberg + 2 aliment_Mais + 1.3 aliment_Pain_blanc
 + 1.1 aliment_Pain_complet + 3.7 aliment_Pommes
 + 11.6 aliment_Spaghettis_en_sauce + 0.5 aliment_Tarte_aux_pommes
 + 1.4 aliment_Tofu >= 120
grasMaximum: 0.5 aliment_Bananes + 0.8 aliment_Broccolis + 12.8 aliment_Bœuf
 + 4.5 aliment_Cookie_au_chocoloat + 3.3 aliment_Cookie_poire
 + 0.2 aliment_Haricots + 4.3 aliment_Jambon + 0.6 aliment_Mais
 + aliment_Pain_blanc + aliment_Pain_complet + 0.5 aliment_Pommes
 + 10.8 aliment_Poulet_grillé + 12.3 aliment_Spaghettis_en_sauce
 + 3.1 aliment_Tarte_aux_pommes + 5.5 aliment_Tofu + 7.3 aliment_Œufs_pochés
 <= 80
grasMinimum: 0.5 aliment_Bananes + 0.8 aliment_Broccolis + 12.8 aliment_Bœuf
 + 4.5 aliment_Cookie_au_chocoloat + 3.3 aliment_Cookie_poire
 + 0.2 aliment_Haricots + 4.3 aliment_Jambon + 0.6 aliment_Mais
 + aliment_Pain_blanc + aliment_Pain_complet + 0.5 aliment_Pommes
 + 10.8 aliment_Poulet_grillé + 12.3 aliment_Spaghettis_en_sauce
 + 3.1 aliment_Tarte_aux_pommes + 5.5 aliment_Tofu + 7.3 aliment_Œufs_pochés
 >= 60
legumesMinimum: aliment_Broccolis + aliment_Haricots + aliment_Laitue_Iceberg
 + aliment_Mais + aliment_Pommes + aliment_Tofu >= 3
proteinesMaximum: 1.2 aliment_Bananes + 8 aliment_Broccolis + 5.4 aliment_Bœuf
 + 0.9 aliment_Cookie_au_chocoloat + 1.1 aliment_Cookie_poire
 + 3.7 aliment_Haricots + 3.9 aliment_Jambon + 0.2 aliment_Laitue_Iceberg
 + 2.5 aliment_Mais + 2.2 aliment_Pain_blanc + 2.3 aliment_Pain_complet
 + 0.3 aliment_Pommes + 42.2 aliment_Poulet_grillé
 + 8.2 aliment_Spaghettis_en_sauce + 0.5 aliment_Tarte_aux_pommes
 + 9.4 aliment_Tofu + 6.7 aliment_Œufs_pochés <= 150
proteinesMinimum: 1.2 aliment_Bananes + 8 aliment_Broccolis + 5.4 aliment_Bœuf
 + 0.9 aliment_Cookie_au_chocoloat + 1.1 aliment_Cookie_poire
 + 3.7 aliment_Haricots + 3.9 aliment_Jambon + 0.2 aliment_Laitue_Iceberg
 + 2.5 aliment_Mais + 2.2 aliment_Pain_blanc + 2.3 aliment_Pain_complet
 + 0.3 aliment_Pommes + 42.2 aliment_Poulet_grillé
 + 8.2 aliment_Spaghettis_en_sauce + 0.5 aliment_Tarte_aux_pommes
 + 9.4 aliment_Tofu + 6.7 aliment_Œufs_pochés >= 80
End
