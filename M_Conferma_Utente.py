def confirm_user_action():
    while True:
        user_input = input("Vuoi procedere con la creazione della VLAN? (PROCEDERE/TERMINARE): ").strip().lower()
        if user_input in ['PROCEDERE']:
            return True
        else:
            print("TERMINARE")
            return False