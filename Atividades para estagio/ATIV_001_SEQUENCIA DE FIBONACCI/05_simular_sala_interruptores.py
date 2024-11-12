def identificar_interruptores():
    # Passo 1: Inicializa os interruptores e as lâmpadas
    interruptores = ["Interruptor 1", "Interruptor 2", "Interruptor 3"]
    lampadas = {"Lampada 1": "desconhecido", "Lampada 2": "desconhecido", "Lampada 3": "desconhecido"}

    # Primeira ida
    print("1. Ligue o primeiro interruptor e deixe ligado por alguns minutos.")
    # Simula esperar alguns minutos para a lâmpada aquecer
    lampada_aquecida = "Lampada 1"

    print("2. Desligue o primeiro interruptor e ligue o segundo interruptor.")
    # Segundo interruptor está ligado
    lampada_acesa = "Lampada 2"

    print("3. Vá até a sala das lâmpadas.")

    # Segunda ida
    print("4. Verifique as lâmpadas:")
    # Verificar qual lâmpada está acesa
    print(f"  - A lâmpada acesa ({lampada_acesa}) é controlada pelo segundo interruptor.")

    # Verificar qual lâmpada está quente
    print(f"  - A lâmpada quente, mas apagada ({lampada_aquecida}) é controlada pelo primeiro interruptor.")

    # A lâmpada restante
    lampada_fria = "Lampada 3"
    print(f"  - A lâmpada fria e apagada ({lampada_fria}) é controlada pelo terceiro interruptor.")

    # Atualiza o dicionário das lâmpadas
    lampadas[lampada_aquecida] = "Interruptor 1"
    lampadas[lampada_acesa] = "Interruptor 2"
    lampadas[lampada_fria] = "Interruptor 3"

    print("\nResultado:")
    for lampada, interruptor in lampadas.items():
        print(f"{lampada} é controlada por {interruptor}.")
identificar_interruptores()
