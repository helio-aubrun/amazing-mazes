import random

directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
pile = []


def init_labyrinthe(n):
    labyrinthe = [["#"] * (n) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i % 2 != 0 and j % 2 != 0:
                labyrinthe[i][j] = "."

    return labyrinthe


def entree_sortie(labyrinthe, n):
    labyrinthe[0][0] = "."
    labyrinthe[n - 1][n - 1] = "."
    labyrinthe[1][0] = "."
    labyrinthe[n - 2][n - 1] = "."


def non_visite(x, y, n, labyrinthe):
    try:
        return labyrinthe[x][y] == "." and [x, y] not in pile
    except:
        return False


def creuser(labyrinthe, x, y, n):
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if non_visite(nx, ny, n, labyrinthe):
            pile.append([nx, ny])
            labyrinthe[x + dx // 2][y + dy // 2] = "."
            creuser(labyrinthe, nx, ny, n)


def generer_labyrinthe(n):
    labyrinthe = init_labyrinthe(n)
    creuser(labyrinthe, 1, 1, n)
    entree_sortie(labyrinthe, n)

    return labyrinthe


def sauvegarder_labyrinthe(labyrinthe, nom_fichier):
    with open(nom_fichier + ".txt", "w") as f:
        for ligne in labyrinthe:
            f.write("".join(ligne) + "\n")


def main():
    n = 2 * int(input("Entrez la taille du labyrinthe (n): ")) + 1
    nom_fichier = input("Entrez le nom du fichier de sortie: ")

    labyrinthe = generer_labyrinthe(n)

    sauvegarder_labyrinthe(labyrinthe, nom_fichier)
    print(f"Labyrinthe généré et sauvegardé dans {nom_fichier}.")


if __name__ == "__main__":
    main()
