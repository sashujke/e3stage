import success_function # type: ignore
 
def create_vlan(emc_cli, emc_results, vlan_id, vlan_name):
    success = "0" 

    if int(vlan_id) < 2 or int(vlan_id) > 4094:
        print("VLAN ID non valida. Fine esecuzione.")
        success = "NO"
        success_function(emc_results, success) 
        return success

 
    if len(vlan_name) > 32:
        print("VLAN Name troppo lungo. Fine esecuzione.")
        success = "NO"
        success_function(emc_results, success) 
        return success

   
    vlan_exists = emc_cli.send(f"show vlan {vlan_id}")
    vlan_exists_output = vlan_exists.getOutput()

    if "Error: No <vlan_list> found" in vlan_exists_output:
        print("La VLAN ID non esiste, procedo con la creazione.")
        emc_cli.send("create vlan {vlad_name} tag {vlan_id}")
        success = "YES"
    else:
        print("VLAN già esistente!")
        success = "NO"

    print("Operazione completata con stato: {success}")
    success_function(emc_results, success)  
    return success