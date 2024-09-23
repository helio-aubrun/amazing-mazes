import random

directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
pile = []
LIBRE = "."
MUR = "#"

class TrouverUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rang = [0] * n

    def trouver_groupe(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.trouver_groupe(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.trouver_groupe(x)
        rootY = self.trouver_groupe(y)

        if rootX != rootY:
            if self.rang[rootX] > self.rang[rootY]:
                self.parent[rootY] = rootX
            elif self.rang[rootX] < self.rang[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rang[rootX] += 1


def init_labyrinthe(n):
    labyrinthe = [[MUR] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i % 2 != 0 and j % 2 != 0:
                labyrinthe[i][j] = LIBRE
    return labyrinthe


def creer_aretes(n):
    aretes = []
    for i in range(1, n, 2):
        for j in range(1, n, 2):
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 < ni < n and 0 < nj < n:
                    aretes.append(((i, j), (ni, nj)))
    random.shuffle(aretes)
    return aretes


def creuser(labyrinthe, n):
    aretes = creer_aretes(n)
    union_trouver_groupe = TrouverUnion((n // 2) * (n // 2))

    for cell1, cell2 in aretes:
        x1, y1 = cell1
        x2, y2 = cell2
        idx1 = (x1 // 2) * (n // 2) + (y1 // 2)
        idx2 = (x2 // 2) * (n // 2) + (y2 // 2)

        if union_trouver_groupe.trouver_groupe(
            idx1
        ) != union_trouver_groupe.trouver_groupe(idx2):
            union_trouver_groupe.union(idx1, idx2)
            labyrinthe[(x1 + x2) // 2][(y1 + y2) // 2] = LIBRE


def entree_sortie(labyrinthe, n):
    labyrinthe[0][0] = LIBRE
    labyrinthe[n - 1][n - 1] = LIBRE
    labyrinthe[1][0] = LIBRE
    labyrinthe[n - 2][n - 1] = LIBRE


def generer_labyrinthe(n):
    labyrinthe = init_labyrinthe(n)
    creuser(labyrinthe, n)
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
