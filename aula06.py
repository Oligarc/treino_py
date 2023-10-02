def verif_max(idade1: int, idade2: int, idade3: int, idade4:int) -> int:
    if (idade1 >= idade2 and idade1 >= idade3 and idade1 >= idade4):
        maior: int = idade1

    elif (idade2 >= idade1 and idade2 >= idade3 and idade2 >= idade4):
        maior: int = idade2

    elif (idade3 >= idade1 and idade3 >= idade2 and idade3 >= idade4):
        maior: int = idade3

    else:
        maior: int = idade4
    return maior


def med(idade1: int, idade2: int, idade3: int, idade4:int) -> float:
    media: float = (idade1 + idade2 + idade3 + idade4) /4
    return media


def entrada():
    idade1 = int(input('Digite a idade da pessoa 1: '))
    idade2 = int(input('Digite a idade da pessoa 2: '))
    idade3 = int(input('Digite a idade da pessoa 3: '))
    idade4 = int(input('Digite a idade da pessoa 4: '))
    id_maior = med(idade1, idade2, idade3, idade4)
    print("A media de idade: ", id_maior)
    print("A idade maior: ", verif_max(idade1, idade2, idade3, idade4))



