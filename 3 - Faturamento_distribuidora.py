import json

with open("dados.json", encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)

# para cada item do arquivo json
for i in dados:
    # imprimindo dia e valor
    print("dia:",i['dia']," valor: ",i['valor'])
    
contarDias=0;
somaMensal=0;

for i in dados:
    
    if i['valor'] != None and i['valor']>0:
        somaMensal= somaMensal+i['valor']
        contarDias = contarDias + 1
    
print('Total faturamento %.2f' %(somaMensal))
print('Dias Contados',contarDias)
print('Media faturamento %.2f' %(somaMensal/contarDias))
    
maiorFaturamento = 0;
diaMaiorFaturamento = 0;
for i in dados:
    if (i['valor'] > maiorFaturamento):
        maiorFaturamento=i['valor']
        diaMaiorFaturamento=i['dia']
print('Maior faturamento %.2f'%(maiorFaturamento))       

menorFaturamento = 0;
diaMenorFaturamento=0;
for i in dados:
    if i['valor'] != None and menorFaturamento==0:
        menorFaturamento = i['valor']
        diaMenorFaturamento = i['dia']
        
    if i['valor']> 0 and i['valor'] < menorFaturamento:
        menorFaturamento = i['valor']
        diaMenorFaturamento = i['dia']            
print('Menor faturamento %.2f'%(menorFaturamento))

diasMaiorMedia=0
mediaMensal = (somaMensal/contarDias)
for i in dados:
    if i['valor'] != None and i['valor']>0:
        if mediaMensal > i['valor']:
            diasMaiorMedia= diasMaiorMedia + 1
                  
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal é", diasMaiorMedia)