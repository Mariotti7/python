salario=float(input('Qual é o salário do Funcionário? R$'))
aumento= 15
salarioTotal= salario + (salario * round((aumento / 100),2))
print('Um funcionário que ganhava R${}, com {}% de aumento, passa a receber R${:.2f}'.format(salario,aumento,salarioTotal))