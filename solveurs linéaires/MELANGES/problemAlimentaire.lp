\* Probleme_alimentaire *\
Minimize
Cout_total_des_ingrédients_par_boite_de_conserve_de_1kg: 10 Ingr_FARINE
 + 30.5 Ingr_MAIS + 90 Ingr_SOJA
Subject To
calciumRequirementMax: 0.38 Ingr_FARINE + 0.001 Ingr_MAIS + 0.002 Ingr_SOJA
 <= 0.012
calciumRequirementMin: 0.38 Ingr_FARINE + 0.001 Ingr_MAIS + 0.002 Ingr_SOJA
 >= 0.008
conservation: Ingr_FARINE + Ingr_MAIS + Ingr_SOJA = 1
fiberRequirementMax: 0.02 Ingr_MAIS + 0.08 Ingr_SOJA <= 0.05
fiberRequirementMin: 0.09 Ingr_MAIS + 0.5 Ingr_SOJA >= 0.22
End
