# Classe EMC_CLI per simulare l'invio di comandi
class EMC_CLI:
    @staticmethod
    def send(command):
        print("Comando: " + command)

emc_cli = EMC_CLI()

# Funzione per ottenere input dell'utente o valori predefiniti
try:
    vlan_id = raw_input("Inserisci il VLAN ID: ") or "123"  # Valore predefinito se non viene fornito input
    vlan_name = raw_input("Inserisci il VLAN Name: ") or "DefaultVLAN"  # Valore predefinito se non viene fornito input
except EOFError:
    vlan_id = "123"        # Valore predefinito per il VLAN ID in caso di errore di input
    vlan_name = "DefaultVLAN"  # Valore predefinito per il nome VLAN in caso di errore di input

# Funzione principale per chiamare newvlan con emc_cli come parametro
def main(v_id, v_name):
    # Importa createvlan dalla libreria e3
    from e3 import createvlan  # type: ignore
    createvlan.newvlan(v_id, v_name, emc_cli)

# Funzione newvlan per accettare emc_cli come parametro
def newvlan(v_id, v_name, emc_cli):
    # Controllo del VLAN ID e del nome
    try:
        vlan_id_int = int(v_id)
    except ValueError:
        print("Errore: il VLAN ID deve essere un numero intero.")
        return 0

    if vlan_id_int <= 1 or vlan_id_int > 4094:
        print("VLAN ID non valida. Fine esecuzione.")
        return 0
    
    if len(v_name) > 32:
        print("VLAN Name troppo lungo. Fine esecuzione.")
        return 0
    
    # Invio del comando
    emc_cli.send("create vlan " + v_name + " tag " + v_id)

# Richiama la funzione main con i parametri forniti dall'utente o predefiniti
main(vlan_id, vlan_name)
