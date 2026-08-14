import pandas as pd

df = pd.read_csv("data/clientes.csv")

errores = df[df["saldo"] < 0]

if len(errores) > 0:
    print("ERROR: Se encontraron saldos negativos")
    print(errores)
else:
    print("Validación exitosa")