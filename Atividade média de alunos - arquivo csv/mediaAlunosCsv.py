import pandas as pd

df = pd.read_csv("notas_alunos.csv")

media = df["nota_1"] + df["nota_2"] / 2
df["media"] = media

df.loc[df["media"] >= 7 and df["Faltas"] <= 5, "situacao"] = "APROVADO(A)"
df.loc[df["media"] < 7, "situacao"] = "REPROVADO(A)"

faltas = df["Faltas"].max()
print("O maior número de faltas foi ", faltas, ".")
mediaGeral = df["medias"].median()
print("A média geral das notas dos alunos é ", mediaGeral, ".")
mediaMaior = df["media"].max()
print("A maior média é ", mediaMaior, ".")


