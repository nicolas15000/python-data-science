\* MinimiserLpAlliage *\
Minimize
AlliageCost: 1.2 input_mat_al_1 + input_mat_al_2 + 1.3 input_mat_cu_1
 + 1.45 input_mat_cu_2 + 1.2 input_mat_iron_1 + 1.5 input_mat_iron_2
 + 0.9 input_mat_iron_3
Subject To
MaxCarbon: 2.5 input_mat_iron_1 + 3 input_mat_iron_2 <= 150
MaxCu: 0.4 input_mat_al_1 + 0.6 input_mat_al_2 + 90 input_mat_cu_1
 + 96 input_mat_cu_2 + 0.3 input_mat_iron_3 <= 30
MaxMn: 1.2 input_mat_al_1 + 4 input_mat_cu_2 + 1.3 input_mat_iron_1
 + 0.8 input_mat_iron_2 <= 82.5
MinCarbon: 2.5 input_mat_iron_1 + 3 input_mat_iron_2 >= 100
MinCu: 0.4 input_mat_al_1 + 0.6 input_mat_al_2 + 90 input_mat_cu_1
 + 96 input_mat_cu_2 + 0.3 input_mat_iron_3 >= 20
MinMn: 1.2 input_mat_al_1 + 4 input_mat_cu_2 + 1.3 input_mat_iron_1
 + 0.8 input_mat_iron_2 >= 60
RequestedQuantity: input_mat_al_1 + input_mat_al_2 + input_mat_cu_1
 + input_mat_cu_2 + input_mat_iron_1 + input_mat_iron_2 + input_mat_iron_3
 = 5000
End
