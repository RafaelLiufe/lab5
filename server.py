import threading
import rpyc
from rpyc.utils.server import ThreadedServer

mpass = {}
for i in range(1, 11):
    mpass[f"A{i}"] = "Livre"

lck = threading.Lock()

class SrvRes(rpyc.Service):
    def exposed_lstass(self):
        with lck:
            txt = "\n--- Mapa de Assentos ---\n"
            for i in range(1, 11):
                chv = f"A{i}"
                txt += f"{chv}: {mpass[chv]}\n"
            return txt

    def exposed_resass(self, nmcli, ass):
        ass = ass.upper().strip()
        with lck:
            if ass not in mpass:
                return "Assento inexistente."
            if mpass[ass] == "Livre":
                mpass[ass] = f"Reservado ({nmcli})"
                return f"Confirmado: assento {ass} reservado para {nmcli}."
            return "Assento já ocupado"

print("Servidor ativo na porta 18861...")
srv = ThreadedServer(SrvRes, port=18861)
srv.start()