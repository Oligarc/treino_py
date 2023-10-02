def verif_tri(ladox:float, ladoy:float, basez:float) -> bool:
    if ((ladox + ladoy) >= basez):
        return True
    elif ((basez + ladoy) >= ladox):
        return True
    elif ((ladox + basez) >= ladoy):
        return True
    else:
        return False
    
def ident_tip(ladox:float, ladoy:float, basez:float) -> str:
    if ladox == ladoy == basez:
        print("Triangulo Equilatero")
    elif ladox == ladoy != basez or ladox != ladoy == basez:
        print("Triangulo Isósceles")
    elif ladox != ladoy != basez:
        print("Triangulo Escaleno")


def entrada():
    ladox = float(input("Digite um numero para X: "))
    ladoy = float(input("Digite um numero para Y: "))
    basez = float(input("Digite um numero para Z: "))
    lados = verif_tri(ladox, ladoy, basez)
    print("Isso pode ser um triangulo: ", lados)
    tipos = ident_tip(ladox, ladoy, basez)
    
