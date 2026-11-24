import os 

def busca_dados_arquivo():
    dados = {}

    arquivo = open("banco-temperaturas-julho.txt", mode="r", encoding="utf8")
    try:
        for linha in arquivo:
            partes = linha.split("")
            if len(partes) == 3:
                data = partes[0]
                horario = partes[1]
                capital = partes[2]
                data[horario] = (pais, capital)
    finally: 
        arquivo.close()

    return dados



print("as moedas de cada país e suas conversões")
print()

dados = busca_dados_arquivo()


sigla = input("informe a sigla do país desejado: ").upper()

print()
if sigla in dados:
    print(f"nome do país: {dados[sigla][0]}")
    print(f"capital: {dados[sigla][1]}")
else:
    print("sigla não encontrada")