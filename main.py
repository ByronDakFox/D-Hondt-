# Unión por la Esperanza --> UE
# Partido Social Cristiano --> PSC
# Libertad es Pueblo --> LP
# Partido Fuerza Ec --> PFE
# Movimiento Justicia Social --> MJS
# Izquierda Democrática --> ID
# #Pachakutik --> PACH
# Unión Ecuatoriana --> UE
# Alianza PAIS --> AP
def votos(voto):
    partidos = ["PUE", "PSC", "LP", 'PFE', 'MJS', 'CREO', 'ID', 'PACH', 'UE', 'AP'];
    ind = [0] * len(partidos);
    papel = ['BL', 'N'];
    indP = [0] * len(papel);

    while voto != "T":
        votosParti = voto.upper();
        if votosParti in partidos:
            i = partidos.index(votosParti);
            ind[i] += 1;
        elif votosParti in papel:
            j = papel.index(votosParti);
            indP[j] += 1;
        else:
            print('Voto no valido');
        voto = input('Ingrese el nombre del partido a votar: ');
    cantPart = sum(ind);
    cantPa = sum(indP);
    cantMaxPart = max(ind);
    cantMaxPap = max(indP);
    countPart = ind.index(cantMaxPart);
    countPap = indP.index(cantMaxPap);
    ganador = partidos[countPart];
    totalV = cantPart+cantPa;
    print("*******************************************")
    print("el total de votantes fueron: {}".format(totalV));
    print("el Ganador es el partido: {} con un total de votos {}:".format(ganador, cantMaxPart));
    print("el total de votos en blancos y nulos : {}".format(cantPa));




if __name__ == '__main__':
    print('Elecciones 2021');
    voto = input('Ingrese el nombre del partido a votar: ');
    votos(voto);







