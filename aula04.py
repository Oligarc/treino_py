def verif_nota(media: float) -> str:
    if media < 4.9:
        print("Você tirou um D, procure melhorar!")
    elif media < 6.9:
        print("Você tirou um C, muito bem! Mas pode melhorar.")
    elif media < 8.9:
        print("Você tirou um B, parabéns!!")
    else:
        print("Você tirou um A, parabéns!! Bom trbalho!!")

def entrada():
    media = float(input("Digite aqui sua media final: "))
    conceito = verif_nota(media)