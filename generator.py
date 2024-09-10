import random

# Directions pour le déplacement (droite, gauche, bas, haut)
directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]

def init_labyrinthe(n):
    # Créer un labyrinthe initial avec des murs partout ('#')
    labyrinthe = [['#'] * n for _ in range(n)]
    
    # On met l'entrée (0, 0) et la sortie (n-1, n-1) comme vides '.'
    labyrinthe[0][0] = '.'
    labyrinthe[n-1][n-1] = '.'
    
    return labyrinthe

def est_valide(x, y, n, labyrinthe):
    # Vérifier si la position (x, y) est valide (dans les bornes et non visitée)
    return 0 <= x < n and 0 <= y < n and labyrinthe[x][y] == '#'

def creuser(labyrinthe, x, y, n):
    # Mélanger les directions pour garantir le caractère aléatoire
    random.shuffle(directions)
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if est_valide(nx, ny, n, labyrinthe):
            # Enlever le mur entre les deux cellules
            labyrinthe[x + dx // 2][y + dy // 2] = '.'
            labyrinthe[nx][ny] = '.'
            # Appel récursif pour creuser à partir de la nouvelle position
            creuser(labyrinthe, nx, ny, n)

def generer_labyrinthe(n):
    # Initialiser le labyrinthe
    labyrinthe = init_labyrinthe(n)
    
    # Commencer à creuser depuis la position (0, 0)
    creuser(labyrinthe, 0, 0, n)
    
    return labyrinthe

def sauvegarder_labyrinthe(labyrinthe, nom_fichier):
    # Écrire le labyrinthe dans un fichier
    with open(nom_fichier + ".txt", 'w') as f:
        for ligne in labyrinthe:
            f.write(''.join(ligne) + '\n')

def main():
    # Demander la taille du labyrinthe et le nom du fichier de sortie
    n = int(input("Entrez la taille du labyrinthe (n): "))
    nom_fichier = input("Entrez le nom du fichier de sortie: ")
    
    # Générer le labyrinthe
    labyrinthe = generer_labyrinthe(n)
    
    # Sauvegarder le labyrinthe dans le fichier
    sauvegarder_labyrinthe(labyrinthe, nom_fichier)
    print(f"Labyrinthe généré et sauvegardé dans {nom_fichier}.")

# Appel de la fonction principale
if __name__ == "__main__":
    main()