precoProduto=float(input("Qual é o preço do produto? R$"))
desconto=5
calculoDesconto= precoProduto - (precoProduto * round((desconto / 100),2))
print('O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}.'.format(precoProduto,desconto,calculoDesconto))