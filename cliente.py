import rpyc

con = rpyc.connect("localhost", 18861)
nmcli = input("Digite seu nome: ").strip()

while True:
    print("\n1 - Visualizar mapa de assentos")
    print("2 - Reservar assento")
    print("3 - Sair")
    op = input("Opcao: ").strip()

    if op == "1":
        mp = con.root.lstass()
        print(mp)
    elif op == "2":
        ass = input("Assento desejado (A1 a A10): ").strip()
        res = con.root.resass(nmcli, ass)
        print(f"Resposta: {res}")
    elif op == "3":
        print("Saindo...")
        break
    else:
        print("Opcao invalida.")

con.close()