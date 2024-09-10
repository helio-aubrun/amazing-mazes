import random

directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]

def init_labyrinthe(n):
    labyrinthe = [['#'] * n for _ in range(n)]

    labyrinthe[0][0] = '.'
    labyrinthe[n-1][n-1] = '.'
    
    return labyrinthe

def est_valide(x, y, n, labyrinthe):
    return 0 <= x < n and 0 <= y < n and labyrinthe[x][y] == '#'

def creuser(labyrinthe, x, y, n):
    random.shuffle(directions)
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if est_valide(nx, ny, n, labyrinthe):
            labyrinthe[x + dx // 2][y + dy // 2] = '.'
            labyrinthe[nx][ny] = '.'
            creuser(labyrinthe, nx, ny, n)

def generer_labyrinthe(n):
    labyrinthe = init_labyrinthe(n)
    
    creuser(labyrinthe, 0, 0, n)
    
    return labyrinthe

def sauvegarder_labyrinthe(labyrinthe, nom_fichier):
    with open(nom_fichier + ".txt", 'w') as f:
        for ligne in labyrinthe:
            f.write(''.join(ligne) + '\n')

def main():
    n = int(input("Entrez la taille du labyrinthe (n): "))
    nom_fichier = input("Entrez le nom du fichier de sortie: ")
    
    labyrinthe = generer_labyrinthe(n)
    
    sauvegarder_labyrinthe(labyrinthe, nom_fichier)
    print(f"Labyrinthe généré et sauvegardé dans {nom_fichier}.")

if __name__ == "__main__":
    main()