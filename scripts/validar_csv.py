import pandas as pd

df = pd.read_csv("data/clientes.csv")

errorsaldo = df[df["saldo"] < 0]


# cliente vacío
errorvacios = df[df["cliente"].isna()]

# cliente duplicado
errorduplicados = df[df.duplicated("cliente")]


if len(errorsaldo) > 0:
    print("ERROR: Se encontraron saldos negativos")
    print(errorsaldo)
    if len(errorvacios) > 0:
        print("ERROR: ❌ "+ str(len(errorvacios)) + " clientes vacíos")
        print(errorvacios)
        if len(errorduplicados) > 0:
            print("ERROR: ❌ "+ str(len(errorduplicados)) + " clientes duplicados")
            print(errorduplicados)
        else:
            print("Validación exitosa")