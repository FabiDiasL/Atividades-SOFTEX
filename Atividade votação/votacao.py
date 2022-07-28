candidato_x = 0
candidato_y = 0
candidato_z = 0
branco = 0
nulo = 0
votar = "v"

while(votar == "v"):
    try:
        candidato = int(input("Digite o Numero do Candidato:\n- candidato_X = 889 \n- candidato_Y = 847 \n- candidato_Z = 515 \n- branco = 0 \n"))
        
        votar = input("Fim da votação. Digite: v - Votar ou FIM - Resultado da votação \n")
        
        if (candidato == 889):
            candidato_x += 1

        elif (candidato == 847):
            candidato_y += 1

        elif (candidato == 515):
            candidato_z += 1

        elif (candidato == 0):
            branco += 1
            nulo += 1

        else:
            nulo += 1
            if candidato == "":
                nulo += 0 

    except: print("Opção inválida. Vote novamente")

  
    if (votar == "FIM" or votar == "Fim" or votar == "fim"):
        if candidato_x > candidato_y and candidato_x > candidato_z:
            print("Vencedor: Candidato X com ", candidato_x," voto(s)\n")
            print("Candidato Y obteve ", candidato_y, " voto(s)\n")
            print("Candidato Z obteve ", candidato_z, " voto(s)\n")
            print("Votos nulos: ", nulo, "\nVotos em branco: ", branco)
        elif candidato_y > candidato_x and candidato_y > candidato_z:
            print("Vencedor: Candidato Y com ", candidato_y, " voto(s)\n")
            print("Candidato X obteve ", candidato_x, " voto(s)\n")
            print("Candidato Z obteve ", candidato_z, " voto(s)\n")
            print("Votos nulos: ", nulo, "\nVotos em branco: ", branco)
        elif candidato_z > candidato_x and candidato_z > candidato_y:
            print("Vencedor: Candidato Z com ", candidato_z, " voto(s)\n")
            print("Candidato X obteve ", candidato_x, " voto(s)\n")
            print("Candidato Y obteve ", candidato_y, " voto(s)\n")
            print("Votos nulos: ", nulo, "\nVotos em branco: ", branco)
        else:
            print("Não houve vencedor.")
            print("Votos nulos: ", nulo, "\nVotos em branco: ", branco)
    
    