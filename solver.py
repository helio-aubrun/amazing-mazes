def lire_labyrinthe(fichier_labyrinthe):
    with open(fichier_labyrinthe + ".txt", "r") as fichier:
        labyrinthe = [list(ligne.strip()) for ligne in fichier.readlines()]
    return labyrinthe


def ecrire_labyrinthe(labyrinthe, fichier_sortie):
    with open(fichier_sortie + ".txt", "w") as fichier:
        for ligne in labyrinthe:
            fichier.write("".join(ligne) + "\n")


def est_valide(labyrinthe, x, y):
    if (
        0 <= x < len(labyrinthe)
        and 0 <= y < len(labyrinthe[0])
        and labyrinthe[x][y] == "."
    ):
        return True
    return False


def resoudre_labyrinthe(labyrinthe, x, y):
    if x == len(labyrinthe) - 1 and y == len(labyrinthe[0]) - 1:
        labyrinthe[x][y] = "o"
        return True

    if est_valide(labyrinthe, x, y):
        labyrinthe[x][y] = "o"

        if resoudre_labyrinthe(labyrinthe, x + 1, y):
            return True
        if resoudre_labyrinthe(labyrinthe, x, y + 1):
            return True
        if resoudre_labyrinthe(labyrinthe, x - 1, y):
            return True
        if resoudre_labyrinthe(labyrinthe, x, y - 1):
            return True

        labyrinthe[x][y] = "*"

    return False


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
