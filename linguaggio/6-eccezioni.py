def moltiplicatore():
    try:
        a = int(input("Inserisci il valore di a: "))
        b = int(input("Inserisci il valore di b: "))
        risultato = a * b
        print(risultato)
    except ValueError as e: #l'errore lo possiamo prendere dal termianale quando si verifica
        print(f"C'è stato un errore: {e}")
        print("Solo caratteri numerici")
    finally: #esegue sia se si verifica l'errore e sia se non si verifica
        print("Sto chiudendo l'applicazione")

moltiplicatore()