import create_vlan # type: ignore
import success_function # type: ignore

def main(emc_cli, emc_results, vlan_id, vlan_name):
    if success_function():
        create_vlan(emc_cli, emc_results, vlan_id, vlan_name)
    else:
        print("Operazione annullata. La VLAN non è stata creata.")

main(emc_cli, emc_results, "99999", "port99999") #type: ignore