import heapq


def lire_labyrinthe(fichier_labyrinthe):
    with open(fichier_labyrinthe + ".txt", "r") as fichier:
        labyrinthe = [list(ligne.strip()) for ligne in fichier.readlines()]
    return labyrinthe


def ecrire_labyrinthe(labyrinthe, fichier_sortie):
    with open(fichier_sortie + ".txt", "w") as fichier:
        for ligne in labyrinthe:
            fichier.write("".join(ligne) + "\n")


def heuristic(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])


def coup_valide(labyrinthe, x, y):
    return (
        0 <= x < len(labyrinthe)
        and 0 <= y < len(labyrinthe[0])
        and labyrinthe[x][y] == "."
    )


def obtenir_voisins(labyrinthe, position):
    x, y = position
    voisins = []
    if coup_valide(labyrinthe, x + 1, y):
        voisins.append((x + 1, y))
    if coup_valide(labyrinthe, x - 1, y):
        voisins.append((x - 1, y))
    if coup_valide(labyrinthe, x, y + 1):
        voisins.append((x, y + 1))
    if coup_valide(labyrinthe, x, y - 1):
        voisins.append((x, y - 1))
    return voisins


def resoudre_labyrinthe(labyrinthe, depart_x, depart_y):
    fin_x, fin_y = len(labyrinthe) - 1, len(labyrinthe[0]) - 1
    depart = (depart_x, depart_y)
    arrivee = (fin_x, fin_y)

    openList = []
    closedList = set()
    heapq.heappush(openList, (0, depart, None))

    chemin = {}
    cout_g = {depart: 0}
    cout_f = {depart: heuristic(depart, arrivee)}

    while openList:
        _, pos_actuelle, parent = heapq.heappop(openList)

        if pos_actuelle in closedList:
            continue

        if parent:
            labyrinthe[pos_actuelle[0]][pos_actuelle[1]] = "*"

        if pos_actuelle == arrivee:
            reconstruire_chemin(labyrinthe, chemin, pos_actuelle)
            labyrinthe[depart_x][depart_y] = "o"
            return True

        closedList.add(pos_actuelle)

        for voisin in obtenir_voisins(labyrinthe, pos_actuelle):
            tentative_cout_g = cout_g[pos_actuelle] + 1

            if voisin in closedList:
                continue

            if voisin not in cout_g or tentative_cout_g < cout_g[voisin]:
                chemin[voisin] = pos_actuelle
                cout_g[voisin] = tentative_cout_g
                cout_f[voisin] = tentative_cout_g + heuristic(voisin, arrivee)
                heapq.heappush(openList, (cout_f[voisin], voisin, pos_actuelle))

    return False


def reconstruire_chemin(labyrinthe, chemin, pos_actuelle):
    while pos_actuelle in chemin:
        labyrinthe[pos_actuelle[0]][pos_actuelle[1]] = "o"
        pos_actuelle = chemin[pos_actuelle]


def main():
    fichier_labyrinthe = input("Entrez le nom du fichier contenant le labyrinthe : ")
    fichier_sortie = input("Entrez le nom du fichier pour sauvegarder la solution : ")

    labyrinthe = lire_labyrinthe(fichier_labyrinthe)

    if resoudre_labyrinthe(labyrinthe, 0, 0):
        print("\nSolution trouvée !")
    else:
        print("\nPas de solution trouvée.")

    ecrire_labyrinthe(labyrinthe, fichier_sortie)
    print(f"\nLabyrinthe résolu enregistré dans {fichier_sortie}")


if __name__ == "__main__":
    main()
