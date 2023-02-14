import pandas as pd
tabela = pd.read_excel("Vendas.xlsx")
print(tabela)
print(f"{'-'*100}")
faturamento_total = tabela["Valor Final"].sum()
print("Faturamento Total:")
print(faturamento_total)
print(f"{'-'*10}")
faturamento_por_loja = tabela[["ID Loja","Produto","Valor Final"]].groupby(["ID Loja","Produto"]).sum()
print("Faturamento por Loja")
print(faturamento_por_loja)
print(f"{'-'*70}")
#Observando a tabela, é possível observar que a "Bermuda Liso" em relação á todas as vendas, de todos as lojas, é a com mais faturamento
#Porém, não tem nas outras lojas de menor faturamento, o que poderia indicar que essa "Bermuda Liso" é um ótimo produto de colocar nas outras lojas.
