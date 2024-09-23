import random
import time
from affichage_ import print_labyrinthe

directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
pile = []
LIBRE = "."
MUR = "#"

def init_labyrinthe(n):
    labyrinthe = [[MUR] * (n) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i % 2 != 0 and j % 2 != 0:
                labyrinthe[i][j] = LIBRE

    return labyrinthe


def entree_sortie(labyrinthe, n):
    labyrinthe[0][0] = LIBRE
    labyrinthe[n - 1][n - 1] = LIBRE
    labyrinthe[1][0] = LIBRE
    labyrinthe[n - 2][n - 1] = LIBRE


def non_visite(x, y, n, labyrinthe):
    try:
        return labyrinthe[x][y] == LIBRE and [x, y] not in pile
    except:
        return False


def creuser(labyrinthe, x, y, n):
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if non_visite(nx, ny, n, labyrinthe):
            pile.append([nx, ny])
            labyrinthe[x + dx // 2][y + dy // 2] = LIBRE
            print_labyrinthe (labyrinthe)
            creuser(labyrinthe, nx, ny, n)


def generer_labyrinthe(n):
    labyrinthe = init_labyrinthe(n)
    creuser(labyrinthe, 1, 1, n)
    entree_sortie(labyrinthe, n)
    print_labyrinthe (labyrinthe)

    return labyrinthe


def sauvegarder_labyrinthe(labyrinthe, nom_fichier):
    with open(nom_fichier + ".txt", "w") as f:
        for ligne in labyrinthe:
            f.write("".join(ligne) + "\n")


def main():
    n = 2 * int(input("Entrez la taille du labyrinthe (n): ")) + 1
    nom_fichier = input("Entrez le nom du fichier de sortie: ")
    start_time = time.time()

    labyrinthe = generer_labyrinthe(n)

    sauvegarder_labyrinthe(labyrinthe, nom_fichier)
    print(f"Labyrinthe généré et sauvegardé dans {nom_fichier}.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTemps de résolution : {elapsed_time:.2f} secondes")


if __name__ == "__main__":
    main()
