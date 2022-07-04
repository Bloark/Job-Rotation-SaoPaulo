SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

faturamentoMensal = SP+RJ+MG+ES+Outros

print("Abaixo o percentual de faturamento para cada estado:")
print('SP %.2f'%(SP/faturamentoMensal*100))
print('RJ %.2f'%(RJ/faturamentoMensal*100))
print('MG %.2f'%(MG/faturamentoMensal*100))
print('ES %.2f'%(ES/faturamentoMensal*100))
print('Outros %.2f'%(Outros/faturamentoMensal*100))