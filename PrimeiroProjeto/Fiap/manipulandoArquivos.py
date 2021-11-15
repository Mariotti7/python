with open ("teste.txt", "a") as arquivo:
    arquivo.write("That's what she said!")
    arquivo.write("\nAwesome")
    
files = open("arquivo.xls", "w")

files.write("Machine Learning")

files.close()