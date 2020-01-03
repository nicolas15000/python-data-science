\* TheWhiskasProblem *\
Minimize
Cout: 0.013 PouletPercent + 0.008 SteakPercent
Subject To
FatRequirement: 0.08 PouletPercent + 0.1 SteakPercent >= 10
FibreRequirement: 0.001 PouletPercent + 0.005 SteakPercent <= 2
PercentagesSum: PouletPercent + SteakPercent = 100
ProteinRequirement: 0.1 PouletPercent + 0.2 SteakPercent >= 8
SaltRequirement: 0.002 PouletPercent + 0.005 SteakPercent <= 0.4
Bounds
0 <= PouletPercent
Generals
PouletPercent
End
