equipamento=[]
valor=[]
serial=[]
departamento=[]
resposta="S"
while resposta == "S" :
    equipamento.append(input("Equipamento: "))
    valor.append(float(input("Valor: ")))
    serial.append(int(input("Número Serial: ")))
    departamento.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar: ").upper()

for valores in range(0,len(equipamento)) :
    print("\nEquipamento....: ", (valores+1))
    print("Nome.............: ", equipamento(valores))
    print("Valor............: ", valor(valores))
    print("Serial...........: ", serial(valores))
    print("Departamento.....: ", departamento(valores))
    