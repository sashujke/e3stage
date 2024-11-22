def success_function(emc_results, mystatus):
    emc_results.put("SUCCESS", mystatus)
    print(f"Stato di successo aggiornato: {mystatus}")
